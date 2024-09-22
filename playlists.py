import sys
from pytube import Playlist

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python playlists.py <playlist_url>", file=sys.stderr)
        sys.exit(1)

    playlist_url = sys.argv[1]
    playlist = Playlist(playlist_url)

    for index, item in enumerate(playlist.videos, 1):
        playlist_url = f"{item.watch_url}&list={playlist.playlist_id}&index={index}"
        print(f"{playlist.title}\t{index}\t{item.title}\t{playlist_url}")
