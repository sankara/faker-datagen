from faker import Faker

fake = Faker()
data = {
    'name': fake.name(),
    'address': fake.address()
}

print(data)
