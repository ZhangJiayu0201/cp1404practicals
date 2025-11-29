import wikipedia


def main():
    """Prompt user for Wikipedia page titles and display page details."""
    title = input("Enter page title: ")

    while title != "":
        try:
            page = wikipedia.page(title, auto_suggest=False)
            print(page.title)
            print(page.summary)
            print(page.url)

        except wikipedia.DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options)

        except wikipedia.PageError:
            print(f'Page id "{title}" does not match any pages. Try another id!')

        title = input("\nEnter page title: ")

    print("Thank you.")


if __name__ == "__main__":
    main()
