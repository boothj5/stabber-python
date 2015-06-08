from stabber import *

stabber = Stabber(0, 5230, 0)

stabber.start()

stabber.for_query("jabber:iq:roster",
    '<iq type="result" to="stabber@localhost/profanity">'
        '<query xmlns="jabber:iq:roster" ver="362">'
            '<item jid="buddy1@localhost" subscription="both" name="Buddy1"/>'
            '<item jid="buddy2@localhost" subscription="both" name="Buddy2"/>'
        '</query>'
    '</iq>')

raw_input("Press enter to send message...")

stabber.send('<message id="mesg10" to="stabber@localhost/profanity" from="buddy1@localhost/laptop" type="chat">'
                '<body>Here is a message sent from stabber, using the Python bindings</body>'
             '</message>')

raw_input("Press enter to stop stabber...")

stabber.stop()
