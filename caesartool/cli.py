from caesartool.banner import show_banner
from caesartool.cipher import encrypt, decrypt, hash_text
from caesartool.output import print_result
from caesartool.helptext import show_help


def main():
    show_banner()

    while True:
        print("[1] Caesar Cipher (Encrypt / Decrypt)")
        print("[2] Hash Generator (MD5 / SHA1 / SHA256)")
        print("[3] Help")
        print("[4] Exit")

        choice = input("\nSelect option: ").strip()

        # =============================
        # CAESAR CIPHER
        # =============================
        if choice == "1":
            print("\n[1] Encrypt")
            print("[2] Decrypt")
            action = input("Enter choice: ").strip()

            text = input("Enter text: ")
            try:
                shift = int(input("Enter shift value: "))
            except ValueError:
                print("[-] Shift must be a number")
                continue

            if action == "1":
                result = encrypt(text, shift)
                print_result("caesar encryption", text, result, shift)

            elif action == "2":
                result = decrypt(text, shift)
                print_result("caesar decryption", text, result, shift)

            else:
                print("[-] Invalid Caesar option")

        # =============================
        # HASH GENERATOR
        # =============================
        elif choice == "2":
            print("\nSelect hash type:")
            print("[1] MD5")
            print("[2] SHA1")
            print("[3] SHA256")

            h_choice = input(
                "Enter hash option (1=MD5, 2=SHA1, 3=SHA256): "
            ).strip()

            text = input("Enter text to hash: ")

            algo_map = {
                "1": "md5",
                "2": "sha1",
                "3": "sha256"
            }

            if h_choice not in algo_map:
                print("[-] Invalid hash option")
                continue

            result = hash_text(text, algo_map[h_choice])
            print_result(
                f"{algo_map[h_choice].upper()} hashing",
                text,
                result
            )

        # =============================
        # HELP SECTION
        # =============================
        elif choice == "3":
            show_help()

        # =============================
        # EXIT
        # =============================
        elif choice == "4":
            print("Exiting CAESARTOOL...")
            break

        else:
            print("[-] Invalid option selected")


if __name__ == "__main__":
    main()
