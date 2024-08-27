from faker import Faker

faker = Faker()


class Payloads:
    create_user = {

        "email": faker.email(),
        "password": faker.password(length=10),
        "name": faker.first_name(),
        "nickname": faker.user_name()

    }

