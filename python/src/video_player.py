"""A video player class."""

from .video_library import VideoLibrary
from .video_playlist import Playlist

#class Playlist(object):
    #"""A class used to represent a Playlist."""
    #name = ' '
    #videos = ' '


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self._video_playlist = Playlist(name=' ', caseless=' ')
        #self.videoplaying = None
        self.playlists={}
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
        value=3
        for vid in videos:
            if video_id==vid.video_id:
                if value==3:
                    counter=1
                    global name
                    name=vid.title

                    value=1
                    print(f"Playing video: {name}")
                    break
                elif value==1:
                    print(f"Stopping video: {name}")
                    name=vid.title
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
        #self._video_playlist.name=playlist_name
        #self._video_playlist.caseless=playlist_name.lower()
        #print(f"Successfully created new playlist: {self._video_playlist.name}")
        if playlist_name.lower() not in self.playlists:
            self.playlists[playlist_name.lower()]=[]
            print("Successfully created new playlist: {0}".format(playlist_name))
        else:
            print("Cannot create playlist: A playlist with the same name already exists")
    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        vid = self._video_library.get_video(video_id)
        if vid and (playlist_name.lower() in self.playlists):
            if video_id not in self.playlists[playlist_name.lower()]:
                print("Added video to {0}: {1}".format(playlist_name, vid.title))
                self.playlists[playlist_name.lower()].append(video_id)
            else:
                print("Cannot add video to {0}: Video already added".format(playlist_name))
        elif playlist_name not in self.playlists:
            print("Cannot add video to {0}: Playlist does not exist".format(playlist_name))
        elif not vid:
            print("Cannot add video to {0}: Video does not exist".format(playlist_name))
        #print(f"Added video to {self._video_playlist.name}: {video_id}")

            #print(f'Added video to {playlist.name}: {playlist.videos}, {video_id_list}')
        #else:
            #print(f'Cannot add video to [: Video does not exist')

    def show_all_playlists(self):
        """Display all playlists."""
        names=self.playlists.keys()
        print("Showing all playlists")
        for item in names:
            print(item)

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if self.playlists[playlist_name.lower()]!=[]:
            print(f"Showing playlist: {playlist_name}")
            for i in self.playlists[playlist_name.lower()]:
                videos = self._video_library.get_all_videos()
                templist = []

                def converttostr(input_seq, seperator):
                    # Join all the strings in list
                    final_str = seperator.join(input_seq)
                    return final_str

                for vid in videos:
                    if i == vid.video_id:
                        templist.append([vid.title,vid.video_id,vid.tags])

                print(f"  {templist[0][0]} ({templist[0][1]}) [{converttostr(list(templist[0][2]), ' ')}]")
        else:
            print(f"Showing playlist: {playlist_name}")
            print("  No videos here yet")
        #print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        if playlist_name.lower() in self.playlists:
            for i in self.playlists[playlist_name.lower()]:
                videos = self._video_library.get_all_videos()
                templist = []

                def converttostr(input_seq, seperator):
                    # Join all the strings in list
                    final_str = seperator.join(input_seq)
                    return final_str

                for vid in videos:
                    if i == vid.video_id:

                        temptitle=vid.title
                        print(f"Removed video from {playlist_name}: {temptitle}")
                        self.playlists[playlist_name.lower()].remove(video_id)


        if playlist_name not in self.playlists:
            print(f"Cannot remove video from {playlist_name}: Playlist does not exist")
        elif video_id not in self.playlists[playlist_name.lower()]:
            print("Cannot remove video from my_playlist: Video does not exist")
        #self.playlists[playlist_name.lower()].remove(video_id)



        #print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.lower() in self.playlists:
            self.playlists[playlist_name.lower()] = []
            print(f'Successfully removed all videos from {playlist_name}')
        else:
            print(f"Cannot clear playlist {playlist_name}: Playlist does not exist")


    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.lower() in self.playlists:
            self.playlists.pop(playlist_name.lower())
            print(f"Deleted playlist: {playlist_name}")
        else:
            print(f"Cannot delete playlist {playlist_name}: Playlist does not exist")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        videos = self._video_library.get_all_videos()

        temp_list = []
        for vid in videos:

            # Convoluted way to display tags in required format
            tags = "["
            for tag in vid.tags:
                tags = tags + tag + " "
            tags = tags + "]"
            print(f"{vid.title}")
            if tags != "[]":
                tags = tags[0:len(tags) - 2] + "]"
            if str(search_term.lower()) in str(vid.title):
                temp_list += [f"{vid.title} ({vid.video_id}) {tags}"]

            # Sort the list and display
        sorted_list = sorted(temp_list)
        print(f"Here are the results for {search_term}:")
        for x in sorted_list:
            print("  " + f"{sorted_list.index(x) + 1}) " + x)

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        videos = self._video_library.get_all_videos()

        temp_list = []
        for vid in videos:

            # Convoluted way to display tags in required format
            tags ="["
            for tag in vid.tags:
                tags = tags + tag + " "
            tags = tags + "]"

            if tags != "[]":
                tags = tags[0:len(tags)-2] + "]"
            if video_tag.lower() in tags:
                temp_list += [f"{vid.title} ({vid.video_id}) {tags}"]

            # Sort the list and display
        sorted_list = sorted(temp_list)
        print(f"Here are the results for {video_tag}:")
        numberlist=[]
        for x in sorted_list:
            numberlist.append(sorted_list.index(x)+1)
            print("  " + f"{sorted_list.index(x)+1}) " + x)
        print("Would you like to play any of the above? If yes, specify the number of the video.")
        print("If your answer is not a valid number, we will assume it's a no.")







    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        object=self._video_library.get_video(video_id)
        
        print(f"{object}")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
