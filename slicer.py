email = input("What is your email?: ").strip()
user = email[:email.index("@")]
domain = email[email.index("@")+1:]
output = "My username is {} and the domain is {}".format(user,domain);
print(output)
