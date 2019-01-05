import sys
import source
import os


def main():
    if len(sys.argv) != 2:
        print("Usage: samenvattinger <filename>.txt")
        sys.exit(1)
    elif not sys.argv[1].endswith(".txt"):
        print("Usage: samenvattinger <filename>.txt")
        sys.exit(1)

    filename = os.path.splitext(sys.argv[1])[0]

    with open(sys.argv[1], "r") as r:
        summarization = source.summarize(r.read())
        with open(filename + "-summarization.txt", "w") as w:
            w.write(summarization)

    print(f"File summarized and written to: {filename + '-summarization.txt'}")
    sys.exit(0)


if __name__ == "__main__":
    main()
