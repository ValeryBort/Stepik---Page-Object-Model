import random
import string

import faker


def creating_fake_email():
    f = faker.Faker()
    email = f.email()
    return email


def creating_fake_password():
    password = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(10))
    return password
