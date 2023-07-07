import textwrap

import feedparser


def render_entries(url, n): 
    feed = feedparser.parse(url)

    wrap_size = 80

    for entry in feed["entries"][0:1]: 
        print("\n")

        print("~"*wrap_size)

        if "title" in entry.keys(): 
            print(textwrap.fill(entry.title, wrap_size))
        if "published" in entry.keys(): 
            print(textwrap.fill(f"Published: {entry.published}", wrap_size))
        
            if "updated" in entry.keys() and entry.updated != entry.published: 
                print(textwrap.fill(f"Updated: {entry.updated}", wrap_size))

        print("~"*wrap_size)

        try: 
            print(textwrap.fill(entry.description, wrap_size))
        except: 
            pass

        if "link" in entry.keys(): 
            print(textwrap.fill(entry.link, wrap_size))

        print("\n")


def main(): 
    # try to read from file of RSS urls
    with open("rss_list.txt", "r") as f: 
        urls = f.readlines()

    urls = [url for url in urls if url[0] != "#"]

    # if no file available or file
    if len(urls) != 0: 
        print("Latest entries from your feed (rss_list.txt)")
        for url in urls: 
            render_entries(url, 1)
    else: 
        url = input("Enter an RSS feed URL:\n")
        render_entries(url, 3)


if __name__ == "__main__":
    main()
