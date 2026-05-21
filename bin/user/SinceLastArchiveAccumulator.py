import logging
import weewx
import weewx.engine

log = logging.getLogger(__name__)

log.info("ArchiveListenerService running...")

class Service(weewx.engine.StdService):

    def __init__(self, engine, config_dict):

        super(ArchiveListenerService, self).__init__(engine, config_dict)

        self.bind(weewx.NEW_ARCHIVE_RECORD, self.handle_archive_record)
        self.bind(weewx.NEW_LOOP_PACKET, self.new_loop_packet)

    def handle_archive_record(self, event):
      """ Handle archive records """
      log.info(f"New archive record! {event.record}")

    def new_loop_packet(self, event):
      """ Handle loop packets """
      log.info(f"New loop packets! {event.packet}")
