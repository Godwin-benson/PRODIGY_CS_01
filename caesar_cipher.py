def caesar_cipher(text, shift, mode):
    """
    Encrypts or decrypts a message using the Caesar Cipher algorithm.

    Parameters:
    text (str): The input message to process.
    shift (int): The shift value for the cipher.
    mode (str): 'encrypt' or 'decrypt' to determine the operation.

    Returns:
    str: The processed message after encryption or decryption.
    """
    result = ""
    if mode.lower() == "decrypt":
        shift = -shift  # Reverse the shift for decryption

    for char in text:
        if char.isalpha():  # Process alphabetic characters
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char  # Keep non-alphabetic characters as-is
    return result


def main():
    print("=== Welcome to the Caesar Cipher Program ===")
    while True:
        # Ask the user for the mode of operation
        mode = input("Would you like to 'encrypt' or 'decrypt' a message? (or type 'exit' to quit): ").strip().lower()
        if mode == "exit":
            print("Goodbye!")
            break
        if mode not in ['encrypt', 'decrypt']:
            print("Invalid option! Please type 'encrypt', 'decrypt', or 'exit'.")
            continue

        # Get the message and shift value from the user
        text = input("Enter your message: ").strip()
        try:
            shift = int(input("Enter the shift value (integer): ").strip())
        except ValueError:
            print("Invalid input! The shift value must be an integer.")
            continue

        # Process the message
        result = caesar_cipher(text, shift, mode)
        print(f"The {mode}ed message is: {result}")
        print("-" * 50)


if __name__ == "__main__":
    main()
