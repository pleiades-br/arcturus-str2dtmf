# String to DTMF tone generator :sound:

## Overview

This Python script generates DTMF (Dual-Tone Multi-Frequency) tones and allows users to save the audio either to a WAV file or ~~play it through an I2S interface~~ (**still in progress**). DTMF tones are commonly used in telephony for dialing on a telephone keypad.

## Features
- Generate DTMF tones for a sequence of digits.
- Option to save the tones to a WAV file or play them through an I2S interface.
- Adjustable parameters such as tone duration, silence duration, sample rate, and mono/stereo output.

## Usage

### Generating DTMF Tones and Saving to WAV

```bash
python str2dtmf.py <sequence_of_digits> --duration <tone_duration_ms> --silence-duration <silence_duration_ms> --sample-rate <sample_rate_hz> --output-file <output_filename.wav>
```

## Configuration
Adjustable parameters in the script:

--duration: Duration of each DTMF tone. *(default: 500 ms)* <br>
--silence-duration: Duration of silence between tones. *(default: 25 ms)* <br>
--sample-rate: Sample rate for audio generation. *(default: 8000 hz)* <br>
--output-file: Output file name for WAV file generation. *(default: "output.wav")* <br>
--stereo: Flag for generating stereo audio instead of mono. <br>
--pcm8: Flag for generating audio on PCM-8 bit instead of PCM-16. <br>
~~--i2s: Flag for playing through I2S interface.~~ (**still in progress**) <br>


## Testing
The script includes unit tests to ensure the correctness of the DTMF tone generation and WAV file saving. Run the tests using:

```bash
python -m unittest test_dtmf_generator.py
```

## Dependencies

NumPy: For numerical operations. <br>
wave (standard library): For WAV file handling. <br>

For easyly install dependencies with pip, just use the command below
```bash
pip install -r requirements.txt
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License 
This project is licensed under the MIT License - see the LICENSE file for details.