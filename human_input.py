def human_edit(text):
    print("Original AI-reviewed content:\n")
    print(text)
    print("\nPlease enter your final edits (or press Enter to keep same):\n")
    user_input = input()
    return user_input if user_input.strip() else text

with open("final_output.txt", "r", encoding="utf-8") as f:
    reviewed_text = f.read()

final_version = human_edit(reviewed_text)

with open("final_version.txt", "w", encoding="utf-8") as f:
    f.write(final_version)

print("Final version saved with human edits.")