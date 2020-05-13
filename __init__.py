from mycroft import MycroftSkill, intent_file_handler


class Walking(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('walking.intent')
    def handle_walking(self, message):
        self.speak_dialog('walking')


def create_skill():
    return Walking()

