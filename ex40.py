class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "with a pocket full of shells"])
                        
tessellate = Song(["Triangles are my favorite shape",
                  "Three points where two lines meet.",
                  "Toe to toe back to back, let's go.",  
                  "My love; It's very late.",  
                  "\'till morning comes...Let\'s tessellate."])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

tessellate.sing_me_a_song()
