"""
Wimbledon_simple_funcs.py
Time estimate: 60 minutes
Actual time: 71 minutes
"""


def main():
    filename = "wimbledon.csv"
    lines = read_lines(filename)
    rows = process_rows(lines)
    champion_counts, countries = process_data(rows)
    print("Wimbledon Champions:")
    for name in champion_counts.keys():
        print(name, champion_counts[name])
    sorted_countries = sorted(list(countries))
    print("These", len(sorted_countries), "countries have won Wimbledon:")
    print(", ".join(sorted_countries))


def read_lines(filename):
    lines = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            line = line.strip()
            if line != "":
                lines.append(line)
    return lines


def process_rows(lines):
    rows = []
    for line in lines:
        words = line.split(",")
        word = []
        for w in words:
            word.append(w.strip())
        rows.append(word)
    return rows


def process_data(rows):
    number_of_champions = {}
    countries = set()
    for words in rows:
        champion = words[2]
        country = words[1]
        if champion in number_of_champions:
            number_of_champions[champion] += 1
        else:
            number_of_champions[champion] = 1
        countries.add(country)
    return number_of_champions, countries


main()
