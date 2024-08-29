import unittest
import os
import numpy as np
import wave

from pkg_str2dtmf import generate_dtmf_tones, save_wave_file, dtmf_frequencies

class TestDTMFGenerator(unittest.TestCase):
    def test_generate_dtmf_tones(self):
        input_string = "123"
        duration = 200
        sample_rate = 44100
        silence_duration = 50

        samples_per_tone = int(duration * sample_rate / 1000)
        samples_per_silence = int(silence_duration * sample_rate / 1000)
        total_samples = len(input_string) * (samples_per_tone + samples_per_silence)
        expected_samples = np.zeros(total_samples, dtype=np.int16)

        for i, char in enumerate(input_string):
            f1, f2 = dtmf_frequencies[char.upper()]
            t = np.arange(duration * sample_rate / 1000)
            tone = np.int16(0.5 * 32767.0 * (
                np.sin(2.0 * np.pi * f1 * t / sample_rate) +
                np.sin(2.0 * np.pi * f2 * t / sample_rate)
            ))

            start_index = i * (samples_per_tone + samples_per_silence)
            expected_samples[start_index:start_index + samples_per_tone] = tone

        actual_samples = generate_dtmf_tones(input_string, duration, sample_rate, silence_duration)

        self.assertTrue(np.array_equal(actual_samples, expected_samples))

    def test_save_wave_file(self):
        data = np.zeros(44100, dtype=np.int16)
        filename = "test_output.wav"
        sample_rate = 44100

        save_wave_file(data, filename, sample_rate)
        self.assertTrue(os.path.exists(filename))

        # Verify the content of the saved file
        with wave.open(filename, 'r') as wf:
            self.assertEqual(wf.getnchannels(), 1)
            self.assertEqual(wf.getsampwidth(), 2)
            self.assertEqual(wf.getframerate(), sample_rate)
            self.assertEqual(wf.getnframes(), len(data))

        # Clean up
        os.remove(filename)

if __name__ == "__main__":
    unittest.main()