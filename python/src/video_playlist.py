"""A video playlist class."""


class Playlist:
    """A class used to represent a Playlist."""
    def __init__(self,name, caseless, videos = []):
        self.name=name
        self.caseless=caseless
        self.videos=videos
