from fakergpt import GPTFaker


class People(GPTFaker):
    def name(self):
        prompt = "Generate a fake name:"
        return self.call_gpt(prompt)

    def address(self):
        prompt = "Generate a fake address:"
        return self.call_gpt(prompt)

    def email(self):
        prompt = "Generate a fake email address:"
        return self.call_gpt(prompt)


if __name__ == "__main__":
    faker = People()
    print(faker.name())
    print(faker.address())
    print(faker.email())
