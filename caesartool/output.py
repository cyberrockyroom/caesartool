from datetime import datetime

def print_result(mode, input_text, output_text, shift=None):
    print("\n" + "=" * 45)
    print(f"[+] Tool      : CAESARTOOL")
    print(f"[+] Operation : {mode.upper()}")
    if shift is not None:
        print(f"[+] Shift     : {shift}")
    print(f"[+] Input     : {input_text}")
    print(f"[+] Output    : {output_text}")
    print(f"[+] Time      : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"[+] Status    : SUCCESS")
    print("=" * 45 + "\n")


def print_bruteforce(results):
    print("\n" + "=" * 45)
    print("[+] Tool      : CAESARTOOL")
    print("[+] Mode      : BRUTE FORCE ATTACK")
    print("=" * 45)

    for shift, text in results.items():
        print(f"[Shift {shift:02}] => {text}")

    print("=" * 45 + "\n")
