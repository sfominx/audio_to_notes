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
    notes_o = notes(samplerate=melody.samplerate)

    print("%8s" % "time", "note")

    total_frames = 0
    while True:
        samples, read = melody()
        note = notes_o(samples)
        if note[0]:
            time = total_frames / float(melody.samplerate)
            print("%.6f" % time, midi2note(int(note[0])))
        total_frames += read
        if read < notes_o.hop_size:
            break


if __name__ == '__main__':
    main()
