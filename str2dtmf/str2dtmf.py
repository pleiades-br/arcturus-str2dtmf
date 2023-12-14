import wave
import numpy as np
import argparse
import math

dtmf_frequencies = {
    '1': (697, 1209), '2': (697, 1336), '3': (697, 1477),
    '4': (770, 1209), '5': (770, 1336), '6': (770, 1477),
    '7': (852, 1209), '8': (852, 1336), '9': (852, 1477),
    '0': (941, 1336), '*': (941, 1209), '#': (941, 1477),
    'A': (697, 1633), 'B': (770, 1633), 'C': (852, 1633), 
    'D': (941, 1633), ',': (0, 0)
}

def generate_dtmf_tones(input_string, duration=500, sample_rate=8000, silence_duration=25, pcm8=False):
    '''
        This function receive a input string and generate DTMF data sound inside np.array
        based on the content of the string
        
        Any char that doesn't make part of DTMF code will be ignored

    '''
    samples_per_tone = int(duration * sample_rate / 1000)
    samples_per_silence = int(silence_duration * sample_rate / 1000)
    total_samples = len(input_string) * (samples_per_tone + samples_per_silence)
    data = np.zeros(total_samples, dtype=np.int16)

    for i, char in enumerate(input_string):
        if char.upper() in dtmf_frequencies:
            f1, f2 = dtmf_frequencies[char.upper()]

            # Generate DTMF tone
            t = np.arange(samples_per_tone)
            if pcm8:
                tone = np.int8(0.5 * 127.0 * (
                    np.sin(2.0 * math.pi * f1 * t / sample_rate) +
                    np.sin(2.0 * math.pi * f2 * t / sample_rate)
                ))
            else:
                tone = np.int16(0.5 * 32767.0 * (
                    np.sin(2.0 * math.pi * f1 * t / sample_rate) +
                    np.sin(2.0 * math.pi * f2 * t / sample_rate)
                ))


            # Add DTMF tone to data
            start_index = i * (samples_per_tone + samples_per_silence)
            data[start_index:start_index + samples_per_tone] = tone

            # Add silence to data
            end_silence_index = start_index + samples_per_tone
            data[end_silence_index:end_silence_index + samples_per_silence] = 0

    return data

def save_wave_file(data, filename="output.wav", sample_rate=8000, stereo=False):
    '''
        Save the content in .wav file the content generate by generate_dtmf_tones() 
    '''
    with wave.open(filename, 'w') as wf:
        wf.setnchannels(2 if stereo else 1)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        wf.writeframes(data.tobytes())

def main():
    '''
        Argument parsing with argparse and main job
    '''
    parser = argparse.ArgumentParser(description='Generate DTMF tones and save them to a WAV file.')
    parser.add_argument('digits', type=str, help='Sequence of digits to generate DTMF tones.')
    parser.add_argument('--duration', type=int, default=500, help='Duration of each tone in milliseconds (default: 500).')
    parser.add_argument('--silence-duration', type=int, default=25, help='Duration of silence between tones in milliseconds (default: 25).')
    parser.add_argument('--sample-rate', type=int, default=8000, help='Sample rate in Hz (default: 8000).')
    parser.add_argument('--output-file', type=str, default='output.wav', help='Output WAV file name (default: output.wav).')
    parser.add_argument('--stereo', action='store_true', help='Generate stereo audio instead of mono.')
    parser.add_argument('--pcm8', action='store_true', help='Generate PCM-8 bit instead of PCM-16.')

    args = parser.parse_args()

    dtmf_data = generate_dtmf_tones(args.digits, args.duration, sample_rate=args.sample_rate, silence_duration=args.silence_duration, pcm8=args.pcm8)
    save_wave_file(dtmf_data, filename=args.output_file ,sample_rate=args.sample_rate, stereo=args.stereo)

    print(f"DTMF tones generated and saved to {args.output_file}")

if __name__ == "__main__":
    main()