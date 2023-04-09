import webbrowser


def search_google():
    search_term = input("Enter search term: ").replace(" ", "+")
    webbrowser.open(f"https://google.com/search?q={search_term}")

if __name__ == '__main__':
    search_google()