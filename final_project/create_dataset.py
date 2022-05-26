import csv
import random

def main():
    dic = dict()

    with open("tweets.csv", "rt") as f:
        spamreader = csv.reader(f)
        for row in spamreader:
            name = row[0]
            if name not in ("katyperry", "justinbieber"):
                continue
            name = name + ("_known" if random.random() < 0.9 else "_question")
            dic.setdefault(name, []).append(row)
    for key, value in dic.items():
        with open(key + ".csv", "wt") as f:
            f.write("author,content,country,date_time,id,language,latitude,longitude,number_of_likes,number_of_shares\n")
            spamwriter = csv.writer(f)
            for row in value:
                spamwriter.writerow(row)

if __name__ == "__main__":
    main()
