import base64

try:
    import base64
except ImportError:
    print("The 'base64' module is not available. Please make sure it is installed.")
    exit(1)


def encrypt_base64(text):
    try:
        # Convert the text to bytes
        bytes_text = text.encode('utf-8')

        # Perform Base64 encoding
        encrypted_bytes = base64.b64encode(bytes_text)

        # Convert the encrypted bytes back to a string
        encrypted_text = encrypted_bytes.decode('utf-8')

        return encrypted_text
    except Exception as e:
        print("Encryption failed:", str(e))
        return None

def decrypt_base64(encrypted_text):
    try:
        # Convert the encrypted text to bytes
        encrypted_bytes = encrypted_text.encode('utf-8')

        # Perform Base64 decoding
        decrypted_bytes = base64.b64decode(encrypted_bytes)

        # Convert the decrypted bytes back to a string
        decrypted_text = decrypted_bytes.decode('utf-8')

        return decrypted_text
    except Exception as e:
        print("Decryption failed:", str(e))
        return None

# User interaction
print("---------------------------------------------")
print("Welcome to Base64 Text Encryption/Decryption")
print("---------------------------------------------")

while True:
    print("\nOptions:")
    print("\n")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")

    print("\n")
    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == '1':
        print("\n-----------------------")
        print("Enter the text to encrypt")
        print("-----------------------")
        text = input("Input here: ")

        encrypted_text = encrypt_base64(text)
        if encrypted_text:
            print("\nEncrypted Text:", encrypted_text)

    elif choice == '2':
        print("\n-----------------------")
        print("Enter the text to decrypt")
        print("--------------------------")
        encrypted_text = input("Input here: ")

        decrypted_text = decrypt_base64(encrypted_text)
        if decrypted_text:
            print("\nDecrypted Text:", decrypted_text)

    elif choice == '3':
        print("\nThank you for using Base64 Text Encryption/Decryption!")
        print("Dev: code205")
        print("-----------------------")
        break

    else:
        print("Invalid choice. Please try again.")

