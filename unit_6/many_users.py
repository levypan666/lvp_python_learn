users = {
    'aeinstein': {
      'first': 'albert',
      'last': 'einstein',
      'location': 'princeton',
      'codes': ['0','1'],
    },
    'mcurie': {
      'first': 'marie',
      'last': 'curie',
      'location': 'pairs',
      'codes': ['5','9'],
    },
    'levx':{
    'first': 'sb',
    'last': 'genus',
    'location': 'heaven',
    'codes': ['60','66'],
    },

}

for username, user_info, in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    code = user_info['codes']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
    print("\tCode:" + str(code))