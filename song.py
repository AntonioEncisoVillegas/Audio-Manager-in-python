class Song:

    def __init__(self,id,title,length_secs,author):
        self.id = id
        self.title = title 
        self.lenght_secs = length_secs
        self.author = author
    def __str__(self):
        return f"{self.id} {self.title} {self.lenght_secs}secs"