"""A video player class."""

from .video_library import VideoLibrary


class Playlist(object):
    """A class used to represent a Playlist."""
    name = ' '
    videos = ' '


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        videos = self._video_library.get_all_videos()
        print("Here's a list of all available videos:")
        temp_list = []

        for vid in videos:

            # Convoluted way to display tags in required format
            tags ="["
            for tag in vid.tags:
                tags = tags + tag + " "
            tags = tags + "]"

            if tags != "[]":
                tags = tags[0:len(tags)-2] + "]"

            # Put all videos in a list for sorting
            temp_list += [f"{vid.title} ({vid.video_id}) {tags}"]

        # Sort the list and display
        sorted_list = sorted(temp_list)
        for x in sorted_list:
            print("  "+x)

    def play_video(self, video_id):
        global value
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        videos = self._video_library.get_all_videos()
        counter=0
        for vid in videos:
            if video_id==vid.video_id:
                counter=1
                global name
                name=vid.title
                global value
                value=1
                print(f"Playing video: {name}")
        if counter==0:
            print("Cannot play video: Video does not exist")
            #print("play_video needs implementation")

    def stop_video(self):
        """Stops the current video."""
        global value
        if value>0:
            value=0
            print(f"Stopping video: {name}")
        else:
            print("Cannot stop video: No video is currently playing")

    def play_random_video(self):
        """Plays a random video from the video library."""

        print("play_random_video needs implementation")

    def pause_video(self):
        """Pauses the current video."""
        global value
        if value==1:
            value=2
            print(f"Pausing video: {name}")
        elif value==0:
            print(f"Cannot pause video: No video is currently playing")
        else:
            print(f"Video already paused: {name}")



    def continue_video(self):
        """Resumes playing the current video."""
        global value
        if value==2:
            global name
            value=1
            print(f"Continuing video: {name}")
        elif value==1:


            print(f"Cannot continue video: Video is not paused")


    def show_playing(self):
        def converttostr(input_seq, seperator):
            # Join all the strings in list
            final_str = seperator.join(input_seq)
            return final_str
        """Displays video currently playing."""
        videos = self._video_library.get_all_videos()
        for vid in videos:
            global name
            if vid.title==name and value==1:
                print(f"Currently playing: {vid.title} ({vid.video_id}) [{converttostr(list(vid.tags),' ')}]")
            elif vid.title==name and value==2:
                print(f"Currently playing: {vid.title} ({vid.video_id}) [{converttostr(list(vid.tags),' ')}] - PAUSED")
            elif value==0:
                print("No video is currently playing")
                break
            else:

                pass

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """

        global playlist
        playlist = Playlist()
        playlist.name = playlist_name
        print(f"Successfully created new playlist: {playlist.name}")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """

        #import csv
        #import numpy as np
        #video_id_list=list(np.loadtxt("/Users/Linda/google-code-sample/python/src/videos.txt")[:, 1])
        token = open("/Users/Linda/google-code-sample/python/src/videos.txt", 'r')
        linestoken = token.readlines()
        tokens_column_number = 1
        resulttoken = []
        for x in linestoken:
            resulttoken.append(x.split()[tokens_column_number])
        token.close()
        #with open("/Users/Linda/google-code-sample/python/src/videos.txt") as f:
            #video_id_list = list(zip(*[line.split() for line in f])[1])
        if video_id in resulttoken:
            playlist.videos += f'{video_id}'
            print(f'Added video to {playlist.name}: {playlist.videos}, {video_id_list}')
        else:
            print(f'Cannot add video to [: Video does not exist')

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
