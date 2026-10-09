# 8-8. User Albums

def make_album(artist, title, songs=None):
    album = {
        'artist': artist,
        'title': title,
    }
    if songs is not None:
        album['songs'] = songs
    return album


while True:
    artist = input("Enter the artist name (or 'quit' to stop): ")
    if artist.lower() == 'quit':
        break

    title = input("Enter the album title: ")
    songs = input("Enter the number of songs (press Enter to skip): ")

    if songs:
        album = make_album(artist, title, int(songs))
    else:
        album = make_album(artist, title)

    print(album)
