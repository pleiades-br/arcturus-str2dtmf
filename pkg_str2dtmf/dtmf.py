""" 
    Module providing functions to generate dtmf audio from a given string
"""
import wave
import math
import numpy as np


dtmf_frequencies = {
    '1': (697, 1209), '2': (697, 1336), '3': (697, 1477),
    '4': (770, 1209), '5': (770, 1336), '6': (770, 1477),
    '7': (852, 1209), '8': (852, 1336), '9': (852, 1477),
    '0': (941, 1336), '*': (941, 1209), '#': (941, 1477),
    'A': (697, 1633), 'B': (770, 1633), 'C': (852, 1633), 
    'D': (941, 1633), ',': (0, 0)
}

class DTMF():
    """
        Class representing the dtmf audio object to be created
    """
    def __init__(self,  duration=500, sample_rate=8000, silence_duration=25, pcm8=False) -> None:
        self._duration = duration
        self._sample_rate = sample_rate
        self._silence_duration = silence_duration
        self._pcm8 = pcm8

    @property
    def duration(self) -> int:
        return self._duration
    @duration.setter
    def duration(self, v):
        self._duration = v

    @property
    def sample_rate(self) -> int:
        return self._sample_rate
    @sample_rate.setter
    def sample_rate(self, v):
        self._sample_rate = v

    @property
    def silence_duration(self) -> int:
        return self._silence_duration
    @silence_duration.setter
    def silence_duration(self, v):
        self._silence_duration = v

    @property
    def pcm8(self) -> int:
        return self._pcm8
    @pcm8.setter
    def pcm8(self, v):
        self._pcm8 = v

    def generate_dtmf_tones(self, input_string):
        '''
            This function receive a input string and generate DTMF data sound inside np.array
            based on the content of the string
            
            Any char that doesn't make part of DTMF code will be ignored

        '''
        samples_per_tone = int(self._duration * self._sample_rate / 1000)
        samples_per_silence = int(self._silence_duration * self._sample_rate / 1000)
        total_samples = len(input_string) * (samples_per_tone + samples_per_silence)
        self.data = np.zeros(total_samples, dtype=np.int16)

        for i, char in enumerate(input_string):
            if char.upper() in dtmf_frequencies:
                f1, f2 = dtmf_frequencies[char.upper()]

                # Generate DTMF tone
                t = np.arange(samples_per_tone)
                if self._pcm8:
                    tone = np.int8(0.5 * 127.0 * (
                        np.sin(2.0 * math.pi * f1 * t / self._sample_rate) +
                        np.sin(2.0 * math.pi * f2 * t / self._sample_rate)
                    ))
                else:
                    tone = np.int16(0.5 * 32767.0 * (
                        np.sin(2.0 * math.pi * f1 * t / self._sample_rate) +
                        np.sin(2.0 * math.pi * f2 * t / self._sample_rate)
                    ))


                # Add DTMF tone to data
                start_index = i * (samples_per_tone + samples_per_silence)
                self.data[start_index:start_index + samples_per_tone] = tone

                # Add silence to data
                end_silence_index = start_index + samples_per_tone
                self.data[end_silence_index:end_silence_index + samples_per_silence] = 0
            else:
                print(f'Char \"{char}\" ignored because does not exist as DTMF characters' )     
        return self.data

    def save_wave_file(self, filename="dtmf_output.wav", sample_rate=8000, stereo=False):
        '''
            Save the content in .wav file the content generate by generate_dtmf_tones() 
        '''
        try:
            with wave.open(filename, 'w') as wf:
                wf.setnchannels(2 if stereo else 1)
                wf.setsampwidth(2)
                wf.setframerate(sample_rate)
                wf.writeframes(self.data.tobytes())
        except Exception as error:
            print(f'We could not save the data into {filename}. \
                  Error {type(error).__name__} - {error}')

