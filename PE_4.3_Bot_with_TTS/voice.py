from elevenlabs import play
from elevenlabs.client import ElevenLabs
import config

client = ElevenLabs(
 api_key=config.elevenlabs_api_key,
)

audio = client.generate(
  text="Привет! Меня зовут Дейв.",
  voice="Dave",
  model="eleven_multilingual_v2"
)
play(audio)