from elevenlabs import play
from elevenlabs.client import ElevenLabs
from config import elevenlabs_api_key
from pydub import AudioSegment
from pydub.playback import play as pydub_play

client = ElevenLabs(
 api_key=elevenlabs_api_key,
)
print(f"config.elevenlabs_api_key: {elevenlabs_api_key}")
audio = client.generate(
  text="Привет! Меня зовут Дейв.",
  voice="Dave",
  model="eleven_multilingual_v2"
)

# play(audio)

# Сохраняем аудио в файл
with open("output.mp3", "wb") as f:
    f.write(audio)

# Воспроизводим аудио через pydub
audio_segment = AudioSegment.from_file("output.mp3")
pydub_play(audio_segment)