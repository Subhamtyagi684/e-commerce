from django.core.validators import *
from django.core.exceptions import ValidationError
import re
from django.utils.html import format_html

def validate_mobile(value):
    if str(value).isdigit()==True and len(str(value))==10:
        return value
    else:
        raise ValidationError('Mobile number is invalid')

def validate_password(value):
    if str(value).isalpha()==True:
        raise ValidationError('At least one digit is required')
    elif str(value).isdigit()==True:
        raise ValidationError('At least one alphabet is required')
    elif len(str(value))<5:
        raise ValidationError('Password must have more than 5 characters')
    else:
        return value

def validate_name(value):
    pattern = r'[a-zA-Z ]+'
    if str(value).isdigit()==True:
        raise ValidationError('Only alphabets and minimum 3 characters are allowed ')
    elif re.fullmatch(pattern,str(value)) and len(str(value))>=3:
        return value
    else:
        raise ValidationError('Invalid name')

def validate_username(value):
    if str(value).isalnum()==True and str(value).isalpha()==False and str(value).isdigit()==False and len(str(value))>3:
        return value 
    else:
        raise ValidationError('Invalid username')

def validate_loginuser(value):
    if str(value).strip()=="":
        raise ValidationError('This field is required')
    else:
        return value