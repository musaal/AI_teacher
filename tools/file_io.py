import os
import subprocess

def save_and_execute(slef):
    """
    Saves the provided result to a file and executes an external script.

    Args:
        result (str): The result content to be saved (this might be raw data or file content).
        output_path (str): The file path where the result will be saved.
    """
    # Save the result to the output file
    with open(self.output_path, 'wb') as file:  # Use 'wb' for binary write if dealing with video data
        file.write(self.result)
    
    # Define the path to the external script that processes the saved video
    produce_video_script = r'C:\Users\PC\Desktop\taj\starter_template\tools\produce_video.py'
    
    # Execute the external script
    try:
        result = subprocess.run(
            ['python', produce_video_script, output_path],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        print(f"Script output: {result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Error running script: {e.stderr}")

# # Example usage
# result = b'Some binary data'  # Replace this with the actual binary data
# output_path = r'C:\Users\PC\Desktop\taj\starter_template\tools\file_out.mp4'
# save_and_execute(result, output_path)
