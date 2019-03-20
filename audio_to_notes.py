"""
Convert WAV file to notes
"""
import argparse
from typing import List, Tuple

from aubio import midi2note, notes, source

HOP_SIZE = 512


def convert_wav_to_notes(input_file: str) -> List[Tuple[float, str]]:
    """Convert simple single melody WAV file to notes"""
    melody = source(input_file)
    melody_note = notes(samplerate=melody.samplerate)
    notes_ = []
    total_frames = 0
    while True:
        samples, read = melody()
        note = int(melody_note(samples)[0])
        if note:
            time = total_frames / float(melody.samplerate)
            notes_.append((time, midi2note(note)))
        total_frames += read
        if read < melody_note.hop_size:
            break
    return notes_


def main():
    """Main function"""
    parser = argparse.ArgumentParser()
    parser.add_argument('input', type=str, help='input file')
    args = parser.parse_args()

    notes_ = convert_wav_to_notes(args.input)

    print('Time Note')
    for time, note in notes_:
        print(f'{time:.2f} {note}')


if __name__ == '__main__':
    main()
