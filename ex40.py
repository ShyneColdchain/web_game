def random_lyrics(numb):
    bday_lyrics = ["\nHappy birthday to you", 
                        "I don't want to get sued",
                    "So I'll stop right there\n"]
                
    bulls_lyrics = ["\nThey rally around tha family", 
                            "With pockets full of shells\n"]
    lyrics = []
    
    if numb == 1:
        lyrics = bday_lyrics
    else:
        lyrics = bulls_lyrics
        
    return lyrics

class Song(object):
    
    def __init__(self, lyrics):
        self.lyrics = lyrics
        
    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

bday_lyrics = ["\nHappy birthday to you", 
                    "I don't want to get sued",
                "So I'll stop right there\n"]
                
bulls_lyrics = ["\nThey rally around tha family", 
                        "With pockets full of shells\n"]
            
happy_bday = Song(bday_lyrics)
                
bulls_on_parade = Song(bulls_lyrics)
                        
syhne_coldchain = Song(["\nAs a kid all I wanted", 
                        "was to kill a man",
                        "cus my daddy did it\n"])
                        
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

syhne_coldchain.sing_me_a_song()

random_song = Song(random_lyrics(0))
random_song.sing_me_a_song()