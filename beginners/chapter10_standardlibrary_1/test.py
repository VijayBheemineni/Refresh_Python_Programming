from urllib.request import urlopen
with urlopen("https://huggingface.co/") as response:
     for line in response:
        line_decode = line.decode()
        print(line_decode)