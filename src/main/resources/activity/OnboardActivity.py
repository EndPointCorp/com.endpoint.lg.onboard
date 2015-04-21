# Copyright (C) 2015 Google Inc.
# Copyright (C) 2015 End Point Corporation
# 
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at
# 
# http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.

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

