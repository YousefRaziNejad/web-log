import sys
from controller import Files, Videos


if __name__ == "__main__":
    path = sys.argv[1]

    file = Files(path)

    video = Videos(file.browse_files())

    check_format = video.check_audio_format()

    if not len(check_format) == 0:
        for file in check_format:
            print(file)
    else:
        print("No video in Dolby 5.1 format was found in this directory")