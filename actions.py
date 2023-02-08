# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from typing import Any, List, Dict, Text
import random

class RandomResponseAction(Action):
    def name(self) -> Text:
        return "action_random_response"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        random_responses = ["What else would you like to know about?",
                           "Is there anything else I can help you with?",
                           "Would you like to know more about anything else?"]
        
        random_response = random.choice(random_responses)
        dispatcher.utter_message(text=random_response)
        return []


class EntityResponseAction(Action):
    def name(self) -> Text:
        return "action_entity_out_of_bounds"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        topic = tracker.get_slot("subject")
        if topic not in ['FCR', 'Action Pack', 'Learning Set', 'Resources', 'Forms', 'Coach']:
            dispatcher.utter_template("utter_default",tracker)
        return []