import webbrowser


def search_google():
    search_term = input("Enter search term: ").replace(" ", "+")
    webbrowser.open(f"https://google.com/search?q={search_term}")


search_google()