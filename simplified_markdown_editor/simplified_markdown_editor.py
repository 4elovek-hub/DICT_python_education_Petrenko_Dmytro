def print_help():
    print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line")
    print("Special commands: !help !done")

def format_plain(text):
    return text

def format_bold(text):
    return f"**{text}**"

def format_italic(text):
    return f"*{text}*"

def format_header(level, text):
    return f"{'#' * level} {text}\n"

def format_link(label, url):
    return f"[{label}]({url})"

def format_inline_code(text):
    return f"`{text}`"

def format_ordered_list(rows):
    formatted_rows = '\n'.join([f"{i + 1}. {row}" for i, row in enumerate(rows)])
    return f"{formatted_rows}\n"

def format_unordered_list(rows):
    formatted_rows = '\n'.join([f"* {row}" for row in rows])
    return f"{formatted_rows}\n"

def main():
    formatted_text = ""
    while True:
        user_input = input("Choose a formatter: > ")

        if user_input == "!help":
            print_help()
        elif user_input == "!done":
            print("Final Markdown text:")
            print(formatted_text)
            with open("output.md", "w") as file:
                file.write(formatted_text)
            print("Markdown text saved to output.md")
            print("Exiting the program...")
            break
        elif user_input == "new-line":
            formatted_text += "\n"
            print(formatted_text)
        elif user_input in ["plain", "bold", "italic", "inline-code"]:
            text = input("Text: > ")
            if user_input == "plain":
                formatted_text += format_plain(text)
            elif user_input == "bold":
                formatted_text += format_bold(text)
            elif user_input == "italic":
                formatted_text += format_italic(text)
            elif user_input == "inline-code":
                formatted_text += format_inline_code(text)
            print(formatted_text)
        elif user_input == "header":
            level = int(input("Level: > "))
            if 1 <= level <= 6:
                text = input("Text: > ")
                formatted_text += format_header(level, text)
                print(formatted_text)
            else:
                print("The level should be within the range of 1 to 6.")
        elif user_input == "link":
            label = input("Label: > ")
            url = input("URL: > ")
            formatted_text += format_link(label, url)
            print(formatted_text)
        elif user_input == "ordered-list":
            num_rows = int(input("Number of rows: > "))
            if num_rows > 0:
                rows = [input(f"Row #{i + 1}: > ") for i in range(num_rows)]
                formatted_text += format_ordered_list(rows)
                print(formatted_text)
            else:
                print("The number of rows should be greater than zero.")
        elif user_input == "unordered-list":
            num_rows = int(input("Number of rows: > "))
            if num_rows > 0:
                rows = [input(f"Row #{i + 1}: > ") for i in range(num_rows)]
                formatted_text += format_unordered_list(rows)
                print(formatted_text)
            else:
                print("The number of rows should be greater than zero.")
        else:
            print("Unknown formatting type or command")

if __name__ == "__main__":
    main()