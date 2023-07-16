def text_to_binary(text):
    binary = ""
    for char in text:
        binary += bin(ord(char))[2:].zfill(8) + " "
    return binary.strip()

# Example usage
english_text = "Hello World"
binary_text = text_to_binary(english_text)
print(binary_text)
