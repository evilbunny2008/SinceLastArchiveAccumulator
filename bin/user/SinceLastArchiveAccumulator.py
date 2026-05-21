import logging
import weewx
import weewx.engine

log = logging.getLogger(__name__)

log.info("SinceLastArchiveAccumulatorService running...")

class SinceLastArchiveAccumulatorService(weewx.engine.StdService):

    def __init__(self, engine, config_dict):

        super(SinceLastArchiveAccumulatorService, self).__init__(engine, config_dict)

        self.bind(weewx.NEW_ARCHIVE_RECORD, self.handle_archive_record)
        self.bind(weewx.NEW_LOOP_PACKET, self.new_loop_packet)

        self.rain = 0
        self.ET = 0

    def handle_archive_record(self, event):
      """ Handle archive records """
      log.info(f"New archive record! {event.record}")

    def new_loop_packet(self, event):
      """ Handle loop packets """

      updated_record = weewx.units.to_std_system(event.packet, topic_dict['unit_system'])
      log.info(f"New loop packet {updated_record}")
