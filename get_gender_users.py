import json

def get_gender_users(data:dict) -> list:
    """
    Take the gender of the users and return the list.
    
    The list items are as follows:
        If the user is male: {"Male":1}
        If the user is female: {"Female":0}
    
    Args:
        data(dict): data
    Returns:
        list: users get gender list
    """
    # genders=[{"Male":0},{"Female":0}]
    # for i in data['results']:
    #     if i.get('gender')=='male':
    #         genders[0]['Male']+=1
    #     elif i.get('gender')=='female':
    #         genders[1]['Female']+=1
    # return genders
    users_data = []
    user= {}
    for i in data['results']:
        user['first_name']=i['name']['first']
        user['last_name']=i['name']['last']
        user['phone_number']=i['phone']
        if i.get('gender')=='male':
            user["Male"]=1
        else:
            user["Female"]=0
        users_data.append(user)
        user={}
    return users_data


f=open('./randomuser_data.json')
data=json.load(f)
print(get_gender_users(data))
f.close()