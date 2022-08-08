"""This module houses all the models used in main.py"""

from pydantic import BaseModel, Field

class User(BaseModel):
    name:str = Field(default = "Kieran",example="Kieran")
    age:int = Field(default = 23,example=23)
    country: str = Field(default = "Canada",example="Canada") 
    user_id:int = Field(default =1,example=1)