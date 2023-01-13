import lyricsgenius as lg
import pandas as pd
import csv
import constants

data = pd.read_csv('MoodyLyricsPN.csv')

file = open("./train-data_extended.csv", "w")

genius = lg.Genius(constants.ACCESS_TOKEN, skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"], remove_section_headers=True)

def get_lyrics():
    writer = csv.writer(file)
    header = ['index', 'artist', 'title', 'mood', 'lyrics']
    writer.writerow(header)
    for i, row in data.iterrows():

        try:
            # song = genius.search_song("To You", "Andy Shauf") # song title, artist name
            # song = genius.search_song("West Coast", "Lana Del Rey")
            song = genius.search_song(row[2], row[1])
            ly = song.lyrics.replace('Embed', '')
            # print(ly.splitlines(keepends=True))
            d = [row[0], row[1], row[2], row[3], "".join(ly.splitlines(keepends=True)[1:])]
            # file.write("".join(ly.splitlines(keepends=True)[1:]))
            writer.writerow(d)
            # file.write("".join(ly.splitlines(keepends=True)[2:]))

        except:
            print(f"some exception")
        # file.write('\n----new song')

get_lyrics()
