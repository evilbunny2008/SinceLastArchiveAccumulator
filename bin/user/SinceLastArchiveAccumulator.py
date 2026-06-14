import logging
import weewx
import weewx.engine

log = logging.getLogger(__name__)

log.info("SinceLastArchiveAccumulatorService running...")

weewx.units.obs_group_dict["rain_since_last_archive"] = "group_rain"
weewx.units.obs_group_dict["ET_since_last_archive"] = "group_rain"

class SinceLastArchiveAccumulatorService(weewx.engine.StdService):

    def __init__(self, engine, config_dict):

        super(SinceLastArchiveAccumulatorService, self).__init__(engine, config_dict)

        self.bind(weewx.NEW_ARCHIVE_RECORD, self.handle_archive_record)
        self.bind(weewx.NEW_LOOP_PACKET, self.new_loop_packet)

        self.rain = 0
        self.ET = 0
        self.values_loop = {}
        self.values_archive = {}

    def handle_archive_record(self, event):
      """ Handle archive records """

      self.ET = 0
      self.rain = 0

      self.values_archive.update(event.record)
      event.record = self.values_archive

      #log.info(f"New archive record! {event.record}")

    def new_loop_packet(self, event):
      """ Handle loop packets """

      final_record = event.packet

      ET = final_record.get("ET")
      if ET is None:
          ET = 0

      rain = final_record.get("rain")
      if rain is None:
          rain = 0

      self.ET += ET
      self.rain += rain
      final_record["ET_since_last_archive"] = self.ET
      final_record["rain_since_last_archive"] = self.rain

      self.values_loop.update(final_record)
      event.packet = self.values_loop
