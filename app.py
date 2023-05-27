import gradio as gr
from yt_dlp import YoutubeDL
import os
import subprocess
    
def download_video(url):
  ydl_opts = {'overwrites':True, 'format':'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4', 'outtmpl':'/tmp/video.mp4'}
  with YoutubeDL(ydl_opts) as ydl:
    ydl.download(url)
    return f"/tmp/video.mp4"

def generate(audio_in, video_in):
    print(audio_in, video_in)
    if video_in is not None:
      command = f"python Wav2Lip/inference.py --checkpoint_path Wav2Lip/checkpoints/wav2lip_gan.pth --face '{video_in}' --audio '{audio_in}'"
    else:
      command = f"python Wav2Lip/inference.py --checkpoint_path Wav2Lip/checkpoints/wav2lip_gan.pth --face '/tmp/video.mp4' --audio '{audio_in}'"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    print("stdout:", result.stdout)
    print("stderr:", result.stderr)

    # os.system(f"python inference.py --checkpoint_path checkpoints/wav2lip_gan.pth --face '/content/video.mp4' --audio '{audio_in}'")
    return f"Wav2Lip/results/result_voice.mp4"

app = gr.Blocks()
with app:
  gr.Markdown("""!Made a cool AI song? Bring it to life.""")
  with gr.Row():
    with gr.Column():
      input_text = gr.Textbox(show_label=False, value="https://www.youtube.com/watch?v=FAyKDaXEAgc")
      video_in = gr.Video(show_label=False, type='filepath')
      input_download_button = gr.Button(value="Download from YouTube or Upload video")
      audio_in = gr.Audio(show_label=False, type='filepath')
      input_generate_button = gr.Button(value="Generate")
    with gr.Column():
        video_out = gr.Video(label="Output Video")
    input_download_button.click(download_video, inputs=[input_text], outputs=[video_out])
    input_generate_button.click(generate, inputs=[audio_in, video_in], outputs=[video_out])
  
# app.queue().launch(debug=True, share=True)

# run the app
# app.launch(server_port=8080, enable_queue=False)
app.launch()
