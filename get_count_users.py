import json

def get_count_users(data:dict) -> int:
    """
    You are given dictionary. Find the number of users.

    Args:
        data(dict): data
    Returns:
        int: number of users
    """
    return len(data['results'])
f=open("randomuser_data.json")
data=json.load(f)
print(get_count_users(data))
f.close()