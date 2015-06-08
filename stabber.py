from ctypes import *

class Stabber:
    def __init__(self, loglevel, port, httpport):
        self.libstabber = CDLL("libstabber.so.0")
        self.loglevel = loglevel
        self.port = port
        self.httpport = httpport

    def start(self):
        self.libstabber.stbbr_start(self.loglevel, self.port, self.httpport)

    def set_timeout(self, timeout):
        self.libstabber.stbbr_set_timeout(timeout)

    def auth_password(self, password):
        self.libstabber.stbbr_auth_password(password)

    def for_id(self, idattr, stream):
        self.libstabber.stbbr_for_id(idattr, stream)

    def for_query(self, query, stream):
        self.libstabber.stbbr_for_query(query, stream)

    def wait_for(self, idattr):
        self.libstabber.stbbr_wait_for(idattr)

    def received(self, stanza):
        self.libstabber.stbbr_received(stanza)

    def last_received(self, stanza):
        self.libstabber.stbbr_last_received(stanza)

    def send(self, message):
        self.libstabber.stbbr_send(message)

    def stop(self):
        self.libstabber.stbbr_stop()
