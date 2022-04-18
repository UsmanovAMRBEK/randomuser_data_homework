import json

def get_users_data(data:dict) -> list:
    """
    Take the data of the first name, last name and phone number. Return the list.
    
    The list items are as follows:
        {"first_name": "Dominic", "last_name":"Warholm", "phone_number": "27707465"}

    Args:
        data(dict): data
    Returns:
        list: users data list
    """
    users_data = []
    user= {}
    for i in data['results']:
        user['first_name']=i['name']['first']
        user['last_name']=i['name']['last']
        user['phone_number']=i['phone']
        users_data.append(user)
        user={}
    return users_data


f=open("./randomuser_data.json")
data=json.load(f)
print(get_users_data(data))
f.close()