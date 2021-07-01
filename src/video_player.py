"""A video player class."""

from .video_library import VideoLibrary
import random

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.isPlaying=False
        self.active_video=[]
        self.isPaused = False
        self.video_list = self._video_library.get_all_videos()


    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
       
        all_videos = self._video_library.get_all_videos()
        print("Here's a list of all available videos:")
        vid_list = []

        for vid in all_videos:
            # required tag formats
            tags="["
            for tag in vid.tags:
                tags = tags + tag + " "
            tags = tags + "]"
            if tags!= "[]":
                tags = tags[0:len(tags)-2] + "]"
            else:
                tags=tags

            vid_list +=  [f"{vid.title} ({vid.video_id}) {tags}"]

        new_arr= sorted(vid_list)
        for x in new_arr:
            print(x)



    def play_video(self, video_id):
        videos = self._video_library.get_all_videos()
        for video in videos:
            if video._video_id == video_id:
                if self.isPlaying:
                    print("Stopping video:", self.active_video[0])
                print("Playing video:", video._title)
                self.active_video= [video._title,video._video_id, video._tags]
                self.isPlaying= True
                self.isPaused= False
                return
        print("Cannot play video:Video does not exist")

    def stop_video(self):
        """Stops the current video."""
        if self.isPlaying:
            self.isPlaying = False
            print("Stopping video:", self.active_video[0])
        else:
            print("Cannot stop video: Video does not exist")



    def play_random_video(self):
        """Plays a random video from the video library."""

        video = random.choice(self._video_library.get_all_videos())

        if self.isPlaying is False:
            print("Playing video:" , video.title)
            self.active_video= [video._title,video._video_id, video._tags]
            self.isPlaying = True
        elif self.isPlaying is True:
            print(f"Stopping video:" , self.active_video[0])
            print("Playing video: " + video.title)
            self.active_video= [video._title,video._video_id, video._tags]


    def pause_video(self):
        """Pauses the current video."""
        if self.isPaused :
            self.isPaused= True
            print("Pausing video:", self.active_video[0])
        elif self.isPaused is False:
            self.isPaused = False
            print("Video already paused:",self.active_video[0])
        else:
            if self.isPlaying:
                self.isPlaying = True
                print("Cannot pause video: No video is currently playing")


    def continue_video(self):
        """Resumes playing the current video."""
        if self.isPaused :
            self.isPaused= False
            print("Cannot continue video:", self.active_video[0])
        elif self.isPaused is True:
            self.isPaused = True
            print("Continuing video:",self.active_video[0])
        else:
            if self.isPlaying:
                self.isPlaying = True
                print("Cannot continue video: No video is currently playing")



    def show_playing(self):
        """Displays video currently playing."""

        print("show_playing needs implementation")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

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
