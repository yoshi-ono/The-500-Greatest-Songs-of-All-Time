import json

files = [
    "500-451.json",
    "450-401.json",
    "400-351.json",
    "350-301.json",
    "300-251.json",
    "250-201.json",
    "200-151.json",
    "150-101.json",
    "100-51.json",
    "50-1.json"]

fw = open("list.txt", "w")

for file in files:
    fp = open(file)
    songs = json.load(fp)

    for song in songs["gallery"]:
        line = f"{song['positionDisplay']}, {song['title']}"
        print(line)
        fw.write(line + '\n')

fw.close()
