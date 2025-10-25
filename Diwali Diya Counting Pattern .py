"""
Diwali Diya Counting Pattern
=============================
Advanced pattern printing with multiple features
- Input validation
- Multiple pattern styles
- User choice menu
"""

def print_diya_pattern_basic(n):
    """Basic increasing pattern."""
    print("\n✨ Basic Diya Pattern ✨")
    for i in range(1, n + 1):
        print("★ " * i)


def print_diya_pattern_pyramid(n):
    """Pyramid centered pattern."""
    print("\n🪔 Pyramid Diya Pattern 🪔")
    for i in range(1, n + 1):
        spaces = " " * (n - i) * 2
        diyas = "★ " * i
        print(spaces + diyas)


def print_diya_pattern_diamond(n):
    """Diamond shaped pattern."""
    print("\n💎 Diamond Diya Pattern 💎")
    # Upper half
    for i in range(1, n + 1):
        spaces = " " * (n - i) * 2
        diyas = "★ " * i
        print(spaces + diyas)
    # Lower half
    for i in range(n - 1, 0, -1):
        spaces = " " * (n - i) * 2
        diyas = "★ " * i
        print(spaces + diyas)


def print_diya_pattern_colorful(n):
    """Pattern with border and colors (ANSI)."""
    print("\n🌟 Colorful Diya Pattern 🌟")
    colors = ['\033[91m', '\033[93m', '\033[92m', '\033[94m', '\033[95m', '\033[96m']
    reset = '\033[0m'
    
    # Top border
    print("═" * (n * 3 + 4))
    
    for i in range(1, n + 1):
        color = colors[i % len(colors)]
        diyas = f"{color}★{reset} " * i
        print(f"║ {diyas} ║")
    
    # Bottom border
    print("═" * (n * 3 + 4))


def print_diya_pattern_numbered(n):
    """Pattern with row numbers."""
    print("\n🔢 Numbered Diya Pattern 🔢")
    for i in range(1, n + 1):
        row_num = f"Row {i}: "
        diyas = "★ " * i
        print(row_num + diyas)


def main():
    """Main function with menu-driven interface."""
    print("=" * 60)
    print("🪔 DIWALI DIYA COUNTING PATTERN GENERATOR 🪔")
    print("=" * 60)
    
    # Input validation with exception handling
    while True:
        try:
            n = int(input("\nEnter number of rows (1-20): "))
            if 1 <= n <= 20:
                break
            else:
                print("❌ Please enter a number between 1 and 20!")
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")
    
    # Menu for pattern selection
    print("\n" + "─" * 60)
    print("Choose Pattern Style:")
    print("─" * 60)
    print("1. Basic Pattern (Simple increasing)")
    print("2. Pyramid Pattern (Centered)")
    print("3. Diamond Pattern (Full diamond)")
    print("4. Colorful Pattern (With borders)")
    print("5. Numbered Pattern (Row numbers)")
    print("6. ALL PATTERNS (Show all at once)")
    print("─" * 60)
    
    while True:
        try:
            choice = int(input("\nEnter your choice (1-6): "))
            if 1 <= choice <= 6:
                break
            else:
                print("❌ Please choose between 1-6!")
        except ValueError:
            print("❌ Invalid choice!")
    
    print("\n" + "=" * 60)
    
    # Execute based on choice
    if choice == 1:
        print_diya_pattern_basic(n)
    elif choice == 2:
        print_diya_pattern_pyramid(n)
    elif choice == 3:
        print_diya_pattern_diamond(n)
    elif choice == 4:
        print_diya_pattern_colorful(n)
    elif choice == 5:
        print_diya_pattern_numbered(n)
    elif choice == 6:
        print_diya_pattern_basic(n)
        print_diya_pattern_pyramid(n)
        print_diya_pattern_diamond(n)
        print_diya_pattern_colorful(n)
        print_diya_pattern_numbered(n)
    
    print("\n" + "=" * 60)
    print("✨ Happy Diwali! May your life be filled with light! ✨")
    print("=" * 60)


if __name__ == "__main__":
    main()
