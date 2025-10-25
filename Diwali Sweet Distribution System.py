"""
Diwali Sweet Distribution System
=================================
Advanced sweet distribution calculator with multiple features
- Multiple distribution methods
- Statistics and analytics
- Fair distribution algorithms
"""

import math


def basic_distribution(total_sweets, num_friends):
    """Basic equal distribution."""
    sweets_per_friend = total_sweets // num_friends
    remaining = total_sweets % num_friends
    
    print("\n🍬 BASIC DISTRIBUTION 🍬")
    print("─" * 50)
    print(f"Total Sweets: {total_sweets}")
    print(f"Number of Friends: {num_friends}")
    print(f"Each Friend Gets: {sweets_per_friend} sweets")
    print(f"Remaining Sweets: {remaining}")
    print("─" * 50)
    
    return sweets_per_friend, remaining


def fair_distribution(total_sweets, num_friends):
    """Fair distribution with remainder handling."""
    base_sweets = total_sweets // num_friends
    remaining = total_sweets % num_friends
    
    print("\n⚖️ FAIR DISTRIBUTION (First friends get +1) ⚖️")
    print("─" * 50)
    
    distribution = []
    for i in range(num_friends):
        if i < remaining:
            sweets = base_sweets + 1
            distribution.append(sweets)
            print(f"Friend {i+1}: {sweets} sweets ⭐")
        else:
            distribution.append(base_sweets)
            print(f"Friend {i+1}: {base_sweets} sweets")
    
    print("─" * 50)
    print(f"Total Distributed: {sum(distribution)}")
    print(f"Remaining: 0 (All distributed fairly)")
    
    return distribution


def percentage_distribution(total_sweets, num_friends):
    """Show percentage each friend gets."""
    sweets_per_friend = total_sweets // num_friends
    remaining = total_sweets % num_friends
    
    percentage = (sweets_per_friend / total_sweets) * 100
    
    print("\n📊 PERCENTAGE DISTRIBUTION 📊")
    print("─" * 50)
    print(f"Each Friend Gets: {percentage:.2f}% of total sweets")
    print(f"That's {sweets_per_friend} sweets out of {total_sweets}")
    print(f"Remaining: {remaining} ({(remaining/total_sweets)*100:.2f}%)")
    print("─" * 50)


def custom_distribution(total_sweets, num_friends):
    """Custom weighted distribution."""
    print("\n🎯 CUSTOM WEIGHTED DISTRIBUTION 🎯")
    print("─" * 50)
    print("Assign priority (1=Low, 2=Medium, 3=High) for each friend:")
    
    priorities = []
    for i in range(num_friends):
        while True:
            try:
                priority = int(input(f"Friend {i+1} priority (1-3): "))
                if 1 <= priority <= 3:
                    priorities.append(priority)
                    break
                else:
                    print("❌ Enter 1, 2, or 3 only!")
            except ValueError:
                print("❌ Invalid input!")
    
    total_priority = sum(priorities)
    
    print("\n📋 Distribution Results:")
    print("─" * 50)
    
    distributed = []
    for i, priority in enumerate(priorities):
        share = int((priority / total_priority) * total_sweets)
        distributed.append(share)
        print(f"Friend {i+1} (Priority {priority}): {share} sweets")
    
    remaining = total_sweets - sum(distributed)
    print("─" * 50)
    print(f"Total Distributed: {sum(distributed)}")
    print(f"Remaining: {remaining}")


def statistics_report(total_sweets, num_friends):
    """Generate detailed statistics."""
    sweets_per_friend = total_sweets // num_friends
    remaining = total_sweets % num_friends
    
    print("\n📈 STATISTICAL ANALYSIS 📈")
    print("=" * 50)
    print(f"Total Sweets: {total_sweets}")
    print(f"Number of Friends: {num_friends}")
    print(f"Average per Friend: {total_sweets/num_friends:.2f}")
    print(f"Median Distribution: {sweets_per_friend}")
    print(f"Distribution Efficiency: {((total_sweets-remaining)/total_sweets)*100:.2f}%")
    print(f"Waste (Remaining): {remaining} ({(remaining/total_sweets)*100:.2f}%)")
    print("=" * 50)


def main():
    """Main function with menu system."""
    print("=" * 60)
    print("🍬 DIWALI SWEET DISTRIBUTION SYSTEM 🍬")
    print("=" * 60)
    
    # Input with validation
    while True:
        try:
            total_sweets = int(input("\nEnter total number of sweets: "))
            if total_sweets > 0:
                break
            else:
                print("❌ Please enter a positive number!")
        except ValueError:
            print("❌ Invalid input! Enter a number.")
    
    while True:
        try:
            num_friends = int(input("Enter number of friends: "))
            if num_friends > 0:
                break
            else:
                print("❌ Please enter a positive number!")
        except ValueError:
            print("❌ Invalid input! Enter a number.")
    
    # Menu
    print("\n" + "─" * 60)
    print("Choose Distribution Method:")
    print("─" * 60)
    print("1. Basic Distribution (Equal shares)")
    print("2. Fair Distribution (Distribute all sweets)")
    print("3. Percentage View (See percentages)")
    print("4. Custom Weighted (Priority-based)")
    print("5. Statistical Report (Complete analysis)")
    print("6. ALL METHODS (Show everything)")
    print("─" * 60)
    
    while True:
        try:
            choice = int(input("\nEnter your choice (1-6): "))
            if 1 <= choice <= 6:
                break
            else:
                print("❌ Choose between 1-6!")
        except ValueError:
            print("❌ Invalid choice!")
    
    print("\n" + "=" * 60)
    
    # Execute based on choice
    if choice == 1:
        basic_distribution(total_sweets, num_friends)
    elif choice == 2:
        fair_distribution(total_sweets, num_friends)
    elif choice == 3:
        percentage_distribution(total_sweets, num_friends)
    elif choice == 4:
        custom_distribution(total_sweets, num_friends)
    elif choice == 5:
        statistics_report(total_sweets, num_friends)
    elif choice == 6:
        basic_distribution(total_sweets, num_friends)
        fair_distribution(total_sweets, num_friends)
        percentage_distribution(total_sweets, num_friends)
        statistics_report(total_sweets, num_friends)
    
    print("\n" + "=" * 60)
    print("🎉 Happy Diwali! Share the sweetness! 🎉")
    print("=" * 60)


if __name__ == "__main__":
    main()
