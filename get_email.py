import json

def get_email(data:dict) -> list:
    """
    Take the email of the users and return the list.

    Args:
        data(dict): data
    Returns:
        list: users email
    """
    email=[]
    for i in data.get('results'):
        email.append(i.get('email'))
    return email
        

f=open('randomuser_data.json')
data=json.load(f)
print(get_email(data))
f.close()