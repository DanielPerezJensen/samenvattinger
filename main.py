import summarizer as sm
import os


directory = os.listdir('data/og-text')

for file in directory:
    if ".txt" in file:
        with open(f"data/og-text/{file}", "r") as f:
            data = f.read()
            summary = sm.summarize(data)
            with open(f"data/summaries/{file}-sm.txt", "w") as f:
                f.write(summary)
