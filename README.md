# An automatic summarizer written in Python3

Based on [cosine similarity](https://en.wikipedia.org/wiki/Cosine_similarity). Every sentence is compared to every other sentence to allocate points to the sentences that are most similar to all other sentences in the string. The sentences with the most points are then put into the summarization in the order they are found within the string. 

Usage: 
```bash
python summarizer.py <filename>.txt
```
Alternatively:

You can import the summarizer function into your own programming like so.
```python
import summarizer as sm

string = "<some text>"
# language is the language of the original string, english is used by default
# value is the length of the summarization as a percentage of the original string.
summarized-string = sm.summarize(string, language=<some language>, value=<some float between 0.1 and 1>)

```
