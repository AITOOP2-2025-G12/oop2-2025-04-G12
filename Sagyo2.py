import mlx_whisper
from pydub import AudioSegment
import numpy as np

class Sagyo2:
    """音声ファイルを指定して文字起こしをするクラス。
    Returns:
        result: 文字起こしの結果を含む関数。
    """

    def transcribe_audio(self):

    # 音声ファイルを指定して文字起こし
        audio_file_path  = "python-audio-output.wav"

        result = mlx_whisper.transcribe(audio_file_path, path_or_hf_repo="./whisper-base-mlx")
        print(result)

        return result["text"]

