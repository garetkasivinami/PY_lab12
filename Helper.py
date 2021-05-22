import string
import random
import hashlib


def CreateTemplateFileName(template_name):
    return f'{template_name}.html'

def SetAdminViewsFolder(template_name):
    return f'Admin/{template_name}'

def GenerateSalt():
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(10))

def HashPassword(password):
    salt=GenerateSalt()
    hashedPassword = HashPasswordWithSalt(password, salt)
    return (hashedPassword, salt)

def HashPasswordWithSalt(password, salt):
    m = hashlib.sha256()
    m.update((password + salt).encode('utf-8'))
    return m.hexdigest()