import signal
import logging

logger = logging.getLogger("__main__")

class SignalHandler():
    """ Signal Handler to catch Signal """
    running = True
    config_chge = False

    def __init__(self, handler):
        signal.signal(signal.SIGINT, self.catch_interupt_flag)
        signal.signal(signal.SIGTERM, self.catch_terminate_flag)
        #signal.signal(signal.SIGHUP, self.catch_config_flag)
        self.handler = handler

    def catch_terminate_flag(self, signum, frame):
        self.running = False
        logger.info("SIGTERM detected. Stopping program")
        self.handler(signum, frame)
        
    def catch_interupt_flag(self, signum, frame):
        self.running = False
        logger.info("SIGINT detected. Stopping program")
        self.handler(signum, frame)

    def catch_config_flag(self, signum, frame):
        self.config_chge = True
        logger.info("SIGHUP detected. Reparse config file.")
    
    def set_config_chge_false(self):
        self.config_chge = False