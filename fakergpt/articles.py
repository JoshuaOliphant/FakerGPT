from fakergpt import GPTFaker


class Articles(GPTFaker):
    def tech_article(self):
        prompt = """Write a fake blog post about
            the latest advancements in technology."""
        return self.call_gpt(prompt)


if __name__ == "__main__":
    faker = Articles()
    print(faker.tech_article())
