#首先，创建一个待验证用户列表
#和一个用于存储已验证用户的空列表
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# 验证每个用户， 直到没有未验证用户为止
# 将每个经过验证的列表都已到已验证用户列表中
while unconfirmed_users:
    confirmed_user = unconfirmed_users.pop()

    print("Verifying user:" + confirmed_user.title())
    confirmed_users.append(confirmed_user)

# 显示所有已验证的用户
print ("\nTHe following uses have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())