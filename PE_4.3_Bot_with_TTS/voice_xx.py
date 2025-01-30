from elevenlabs.client import ElevenLabs
import config
from playsound import playsound

# Инициализация клиента ElevenLabs
client = ElevenLabs(
    api_key=config.elevenlabs_api_key,
)

# Генерация аудио
audio = client.generate(
    text="Привет! Меня зовут Дейв.",
    voice="Dave",
    model="eleven_multilingual_v2"
)

# Сохраняем аудио в файл
with open("output.mp3", "wb") as f:
    f.write(audio)

# Воспроизводим аудио через playsound
playsound("output.mp3")м