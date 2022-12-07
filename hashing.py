import bcrypt

password = b"jett parekh"
hashed = bcrypt.hashpw(password, bcrypt.gensalt())

print(hashed)

