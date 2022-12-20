import lyricsgenius as lg

# file = open("./lyrics.csv", "w")
file = open("./test.txt", "w")

genius = lg.Genius('s4lDBOpUf--GgM1ydzt7yQUWLLUofE96OHBEhFvhhuCJ5ni0rd3yqoC9FuhrZDIn', skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"], remove_section_headers=True)

def get_lyrics():
    c = 0
    # for name in arr:
    try:
        # songs = (genius.search_artist(name, sort='popularity')).songs
        song = genius.search_song("To You", "Andy Shauf") # song title, artist name
        file.write("".join(song.lyrics))
        c += 1
        # print(f"Songs grabbed:{len(s)}")
    except:
        print(f"some exception")

get_lyrics()