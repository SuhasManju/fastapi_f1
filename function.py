import base64
import mimetypes
import os
from datetime import datetime
from model import *

def convert_img_base64(file_name:str):
    if not os.path.exists(file_name):
        return None
    
    mime_type,_=mimetypes.guess_type(file_name)
    if mime_type is None:
        mime_type = 'application/octet-stream'

    with open(file_name,"rb") as image:
        encoded_string=base64.b64encode(image.read())

    base64_string=encoded_string.decode('utf-8')
    padded_base64 = f"data:{mime_type};base64,{base64_string}"
    return padded_base64

def create_datetime(date_str, time_str):
    datetime_str = f"{date_str} {time_str}"
    date_format='%Y-%m-%d'
    time_format='%H:%M:%S'
    datetime_format = f"{date_format} {time_format}"
    
    try:
        return datetime.strptime(datetime_str, datetime_format)
    except ValueError as e:
        raise ValueError(f"Error parsing date and time: {e}")
    
def retrive_name(first_name,last_name):
    if last_name:
        first_name+=" "+last_name
    return first_name

def retrive_status(db,statusId):
    return db.query(Status.status).filter(Status.statusId==statusId).first()[0]

