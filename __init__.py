from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler, intent_file_handler
from mycroft.util.log import LOG
from mycroft.util.parse import extract_number, normalize

import random
import re


class VocalTrainer(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('trainer.vocal.intent')
    def handle_trainer_vocal(self, message):
        self.speak_dialog('trainer.vocal')
        
    @intent_file_handler('male.vocal.intent')
    def handle_male_vocal(self, message):
        self.speak_dialog('male.vocal')
        
    @intent_file_handler('trainer.vocal.pitch')
    def handle_trainer_vocal(self, message):
        range = random.randint(1, 200)
        self.speak_dialog('trainer.pitch', data={"result" : range})


def create_skill():
    return VocalTrainer()

