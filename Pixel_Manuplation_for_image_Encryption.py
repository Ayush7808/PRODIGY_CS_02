from PIL import Image
import os

def encrypt_image(image_path, shift_value=50):
    img = Image.open(image_path)
    img = img.convert("RGB")
    pixels = img.load()

    for i in range(img.width):
        for j in range(img.height):
            r, g, b = pixels[i, j]
            # Swap red and blue, and apply shift with wrap-around (mod 256)
            r_new = (b + shift_value) % 256
            g_new = (g + shift_value) % 256
            b_new = (r + shift_value) % 256
            pixels[i, j] = (r_new, g_new, b_new)

    encrypted_path = "encrypted_image.png"
    img.save(encrypted_path)
    print(f"Encrypted image saved as {encrypted_path}")
    return encrypted_path

def decrypt_image(image_path, shift_value=50):
    img = Image.open(image_path)
    img = img.convert("RGB")
    pixels = img.load()

    for i in range(img.width):
        for j in range(img.height):
            r, g, b = pixels[i, j]
            # Reverse the previous transformation
            r_orig = (b - shift_value) % 256
            g_orig = (g - shift_value) % 256
            b_orig = (r - shift_value) % 256
            pixels[i, j] = (r_orig, g_orig, b_orig)

    decrypted_path = "decrypted_image.png"
    img.save(decrypted_path)
    print(f"Decrypted image saved as {decrypted_path}")
    return decrypted_path

def main():
    print("Image Encryption & Decryption Tool")
    path = input("Enter the path to your image file: ")
    if not os.path.exists(path):
        print("File not found.")
        return

    try:
        shift = int(input("Enter shift value (e.g., 50): "))
    except ValueError:
        print("Invalid shift value.")
        return

    choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()
    if choice == 'e':
        encrypt_image(path, shift)
    elif choice == 'd':
        decrypt_image(path, shift)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
