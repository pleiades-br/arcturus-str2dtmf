# String to DTMF tone generator :sound:

## Overview

This Python script generates DTMF (Dual-Tone Multi-Frequency) tones and allows users to save the audio either to a WAV file o DTMF tones are commonly used in telephony for dialing on a telephone keypad.

## Features
- Generate DTMF tones for a sequence of digits.
- Option to save the tones to a WAV file.
- Adjustable parameters such as tone duration, silence duration, sample rate, and mono/stereo output.

## Usage

### Generating DTMF Tones and Saving to WAV

```bash
python str2dtmf.py <sequence_of_digits> --duration <tone_duration_ms> --silence-duration <silence_duration_ms> --sample-rate <sample_rate_hz> --output-file <output_filename.wav>
```

## Configuration
Adjustable parameters in the script:

--output-file: Output file name for WAV file generation. *(default: "output.wav")* <br>
--dtmf-duration: Duration of each DTMF tone. *(default: 500 ms)* <br>
--dtmf-silence-duration: Duration of silence between tones. *(default: 25 ms)* <br>
--dtmf-sample-rate: Sample rate for audio generation. *(default: 8000 hz)* <br>

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