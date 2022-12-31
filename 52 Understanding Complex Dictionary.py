users = [
{
    'username':'jakir',
    'password':'123456',
    'role':'admin'
},
{
    'username':'jahidul',
    'password':'124545',
    'role':'admin'
}
]

for user in users:
    print(user.get('username'))