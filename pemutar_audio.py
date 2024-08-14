from pydub import AudioSegment
import simpleaudio as sa

# Memuat file audio
audio = AudioSegment.from_file('neffex.mp3')

# Mengonversi ke WAV (opsional, jika formatnya bukan WAV)
audio.export('result.wav', format='wav')

# Memutar audio
wave_obj = sa.WaveObject.from_wave_file('result.wav')
play_obj = wave_obj.play()

# Menunggu sampai audio selesai diputar
play_obj.wait_done()