import openai
import webvtt
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.environ.get("OPENAI")

def generate(message):
  completion = openai.ChatCompletion.create(model = "gpt-3.5-turbo", messages=[{"role": "user", "content":
                f"Please summarize the following chunk of dialog in a professional tone:\n{message}"}])
  completion_text = completion.choices[0].message.content
  print(completion_text)
  return completion_text

def divide_chunks(list, n):
  for i in range (0, len(list), n):
    yield list[i : i+n]

def summarize(captions, final_summary_count, chunk_size):
  #summarize in chunks of n captions until there is only like a paragraph remaining.
  while len(captions) > final_summary_count:
    #seperate the current captions into chunks
    chunks = list(divide_chunks(captions, chunk_size))
    print("CHUNK COUNT: ", len(chunks))
    captions = []
    #for each chunk, put it in a string
    for i, chunk in enumerate(chunks):
      print("Chunk: ", i)
      chunk_string = ""
      for cap in chunk:
        chunk_string += cap
      #summarize that string
      summary = generate(chunk_string)
      captions.append(summary)
    #put all the summaries back into the captions var and repeat.
  return captions

captions_file = webvtt.read("./example.vtt")
captions = [caption.text for caption in captions_file]
final_summary_count = 3
chunk_size = len(captions) // (final_summary_count ** 2)
print(captions, final_summary_count, chunk_size)
print(summarize(captions, final_summary_count, chunk_size))