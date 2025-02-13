import pyperclip  # pip install pyperclip (if not installed)

def generate_table(filename):
    """
    Converts lines from a file into a markdown table format.
    - Sorts entries alphabetically
    - Handles game/platform formatting
    - Copies result to clipboard
    """
    try:
        # Read and process file
        with open(filename, 'r', encoding='utf-8') as file:
            lines = [line.strip() for line in file.readlines()]
            lines = [line for line in lines if line]  # Remove empty lines
            lines = sorted(lines, key=lambda x: x.lower())  # Case-insensitive sort

        # Create table headers
        table = [
            "| GAME | PLATFORM |",
            "| ---- | -------- |"
        ]

        # Process each line
        for line in lines:
            # Split into game and platform
            if "/" in line:
                game, platform = line.split("/", 1)
                game = game.strip()
                platform = platform.strip()
            else:
                game, platform = line.strip(), ""
            
            # Add formatted row to table
            table.append(f"| {game} | {platform} |")

        # Finalize output
        result = '\n'.join(table)
        print(result)
        pyperclip.copy(result)
        print("\nOutput copied to clipboard!")

    except FileNotFoundError:
        error_msg = f"Error: File '{filename}' not found!"
        print(error_msg)
        pyperclip.copy(error_msg)
    except ModuleNotFoundError:
        print("Error: pyperclip module not installed. Install with: pip install pyperclip")
    except Exception as e:
        error_msg = f"Unexpected error: {str(e)}"
        print(error_msg)
        pyperclip.copy(error_msg)

# Run the program
if __name__ == "__main__":
    filename = input("Please enter the filename to process: ")
    generate_table(filename)