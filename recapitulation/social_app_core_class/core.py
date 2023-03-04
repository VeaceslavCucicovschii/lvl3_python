class App():

    def __init__(self, name, version, author, year, raiting):
        self.name = name
        self.version = version
        self.author_name = author['name']
        self.author_email = author['email']
        self.year = year
        self.raiting = raiting

    def  __str__(self):
        return f"App: {self.name} v-{self.version}\nAuthor: name-{self.author_name} email-{self.author_email}\nAdditional info: year-{self.year} raiting-{self.raiting} stars"