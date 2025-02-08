from TTS.api import TTS
from langchain.tools import tool
import logging

class Speech:
    # Set the fixed output path
    default_output_path = r'C:\Users\PC\Desktop\taj\starter_template\tools\Text_speech.wav'

    @tool("This tool converts text to speech so you can use the speech when you make the video.")
    def text_to_speech(self, text):
        """
        Converts text to speech and saves it to the specified output path.
        
        Args:
            text (str): The text to be converted to speech.

        Returns:
            str: The path where the speech audio is saved.
        """
        audio_path = self.default_output_path

        try:
            # Initialize TTS with a transformer-based model
            tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=True, gpu=False)
            
            # Convert text to speech
            tts.tts_to_file(text=text, file_path=audio_path)
            
            logging.info(f"Text to speech conversion successful. File saved at: {audio_path}")
            return audio_path

        except Exception as e:
            logging.error(f"An error occurred during text to speech conversion: {e}")
            return None
