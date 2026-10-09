# 8-7. Album

def make_album(artist, title, songs=None):
    album = {
        'artist': artist,
        'title': title,
    }
    if songs is not None:
        album['songs'] = songs
    return album


print(make_album('Taylor Swift', '1989'))
print(make_album('Ed Sheeran', 'Divide'))
print(make_album('Adele', '25', 11))
