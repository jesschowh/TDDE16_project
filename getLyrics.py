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
            song = genius.search_song(row[2], row[1])
            ly = song.lyrics.replace('Embed', '')
            d = [row[0], row[1], row[2], row[3], "".join(ly.splitlines(keepends=True)[1:])]
            writer.writerow(d)
        except:
            print(f"some exception")
            
get_lyrics()