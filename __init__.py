from mycroft import MycroftSkill, intent_file_handler


class VocalTrainer(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('trainer.vocal.intent')
    def handle_trainer_vocal(self, message):
        self.speak_dialog('trainer.vocal')
        
    @intent_file_handler('male.vocal.intent')
    def handle_male_vocal(self, message):
        self.speak_dialog('male.vocal')


def create_skill():
    return VocalTrainer()

