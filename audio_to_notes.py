"""
Convert WAV file to notes
"""
import argparse

from aubio import midi2note, notes, source

HOP_SIZE = 512


def main():
    """Main function"""
    parser = argparse.ArgumentParser()
    parser.add_argument('input', type=str, help='input file')
    args = parser.parse_args()

    melody = source(args.input)
    melody_note = notes(samplerate=melody.samplerate)

    print("%5s" % "time", "note")

    total_frames = 0
    while True:
        samples, read = melody()
        note = int(melody_note(samples)[0])
        if note:
            time = total_frames / float(melody.samplerate)
            print("%.3f" % time, midi2note(note))
        total_frames += read
        if read < melody_note.hop_size:
            break


if __name__ == '__main__':
    main()
