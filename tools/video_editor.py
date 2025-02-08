from moviepy.editor import VideoFileClip, AudioFileClip, CompositeVideoClip
from langchain.tools import tool
import os

class VideoEditor:
    # Define paths as class attributes
    VIDEO_PATH = r'C:\Users\PC\Desktop\taj\starter_template\tools\file.mp4'
    AUDIO_PATH = r'C:\Users\PC\Desktop\taj\starter_template\tools\Text_speech.wav'
    OUTPUT_PATH = r'C:\Users\PC\Desktop\taj\starter_template\tools\file_out.mp4'
    THREEJS_PATH = r'C:\Users\PC\Desktop\taj\starter_template\tools\three.js'
    
    @tool("This tool combines video and audio to create the final video with sound and text and graph animation.")
    def combine_video_and_audio(self):
        """
        Combines a video file and an audio file into a single output video file.
        """
        # Validate input files
        if not os.path.exists(self.VIDEO_PATH):
            print(f"Error: Video file not found at {self.VIDEO_PATH}")
            return None
        
        if not os.path.exists(self.AUDIO_PATH):
            print(f"Error: Audio file not found at {self.AUDIO_PATH}")
            return None
        
        # Ensure output directory exists
        output_dir = os.path.dirname(self.OUTPUT_PATH)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        try:
            # Load video and audio
            video_clip = VideoFileClip(self.VIDEO_PATH)
            audio_clip = AudioFileClip(self.AUDIO_PATH)
            
            # Combine video and audio
            final_clip = video_clip.set_audio(audio_clip)
            
            # Write the output file
            final_clip.write_videofile(self.OUTPUT_PATH, codec="libx264", audio_codec="aac")
            
            print(f"Video and audio successfully combined and saved to {self.OUTPUT_PATH}")

        except FileNotFoundError as e:
            print(f"File not found: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
        
        return self.OUTPUT_PATH

