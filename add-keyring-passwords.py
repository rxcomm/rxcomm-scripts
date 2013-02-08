#!/usr/bin/python

import gtk
import gnomekeyring as gkey
import getpass

class Keyring(object):
    def __init__(self, name, server, protocol):
        self._name = name
        self._server = server
        self._protocol = protocol
        self._keyring = gkey.set_default_keyring_sync('login')

    def has_credentials(self):
        try:
            attrs = {"server": self._server, "protocol": self._protocol}
            items = gkey.find_items_sync(gkey.ITEM_NETWORK_PASSWORD, attrs)
            return len(items) > 0
        except gkey.DeniedError:
            return False

    def get_credentials(self):
        attrs = {"server": self._server, "protocol": self._protocol}
        items = gkey.find_items_sync(gkey.ITEM_NETWORK_PASSWORD, attrs)
        return (items[0].attributes["user"], items[0].secret)

    def set_credentials(self, (user, pw)):
        attrs = {
                "user": user,
                "server": self._server,
                "protocol": self._protocol,
            }
        gkey.item_create_sync(gkey.get_default_keyring_sync(),
                gkey.ITEM_NETWORK_PASSWORD, self._name, attrs, pw, True)

application = raw_input('Application Name: ')
server = raw_input("Server: ")
username = raw_input("Username: ")
protocol = raw_input("Protocol: ")
password = getpass.getpass(prompt="Password: ")
print

keyring = Keyring(application, server, protocol)

keyring.set_credentials((username, password))
