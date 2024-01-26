# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#

from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder

def get_time_zone(lad, dispatcher): 
    dispatcher.utter_message(text="Location address: {}".format(lad)) 
    # getting Latitude and Longitude 
    location = geolocator.geocode(lad) 
    
    dispatcher.utter_message(text="Latitude is {} and Longitude is {}".format(location.latitude, location.longitude))
    
    # pass the Latitude and Longitude 
    # into a timezone_at 
    # and it return timezone 
    obj = TimezoneFinder() 
    
    # returns 'Europe/Berlin' 
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude) 
    # dispatcher.utter_message(text="Time Zone : ", result)
    return result


class ActionFindTimeZone(Action):

    def name(self) -> Text:
        return "action_show_time_zone"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        city = tracker.get_slot("city")
        if city:
            time_zone = get_time_zone(city, dispatcher)
            dispatcher.utter_message(text="The time zone is : {}".format(time_zone))
        else:
            dispatcher.utter_message(text="Time zone could not be found because city is : {}".format(city))
        return []
