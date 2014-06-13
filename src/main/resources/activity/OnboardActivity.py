from interactivespaces.activity.impl.web import BaseWebServerActivity
import os

class OnboardActivity(BaseWebServerActivity):

    def onActivityActivate(self):
        self.log.debug("Onboard activity activated")

    def onActivityDeactivate(self):
        self.log.debug("Onboard activity deactivated")

    def onNewWebSocketConnection(self, connectionId):
        self.log.debug("Got web socket connection from connection " + connectionId)

    def onWebSocketClose(self, connectionId):
        self.log.debug("Got web socket close from connection " + connectionId)

    # dbus-send requires DISPLAY environment variable to be set so that it can
    # discover the bus. Be sure your Controller has been started with an
    # appropriate environment
    def onWebSocketReceive(self, connectionId, data):
        self.log.debug("Got web socket data from connection " + connectionId)
        if data.get('action') == 'showKeyboard':
            os.system('dbus-send --type=method_call --dest=org.onboard.Onboard /org/onboard/Onboard/Keyboard org.onboard.Onboard.Keyboard.Show')
        elif data.get('action') == 'hideKeyboard':
            os.system('dbus-send --type=method_call --dest=org.onboard.Onboard /org/onboard/Onboard/Keyboard org.onboard.Onboard.Keyboard.Hide')

