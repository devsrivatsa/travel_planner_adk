from typing import List
from google.genai import types
from pydantic import BaseModel, Field

json_response_config = types.GenerateContentConfig(
    response_mime_type='application/json'
)

class Destination(BaseModel):
    """A destination recommendation"""
    name:str = Field(description="The name of the destination")
    country:str = Field(description="The country of the destination")
    image_url:str =  Field(description="The image url of the destination")
    highlights:str = Field(description="A short description of the destination highlighting key attractions")
    rating:str = Field(description="The numerical rating of the destination. Ex: 4.5")

class DestinationIdeas(BaseModel):
    """A list of destination recommendations"""
    places:List[Destination] = Field(description="A list of destination recommendations")


class POI(BaseModel):
    """A point of interest recommended by the agent"""
    place_name:str = Field(description="The name of the point of interest")
    address:str = Field(description="The address with sufficient information to geocode for a Lat/Lon")
    lat:str = Field(description="A numerical representation of Latitude of the location (e.g., 20.6843)")
    long:str = Field(description="A numerical representation of Longitude of the location (e.g., 103.2195)")
    review_ratings:str = Field(description="A numerical representation of rating (e.g. 4.8 , 3.0 , 1.0 etc)")
    highlights:str = Field(description="A short description highlighting key features")
    image_url:str = Field(description="Verified url to the image of the destination")
    map_url:str = Field(description="Verified url to the google map")
    place_id:str = Field(description="Google map place id")

class POISuggestions(BaseModel):
    """A list of point of interest recommendations"""
    places:List[POI] = Field(description="A list of point of interest recommendations")

    