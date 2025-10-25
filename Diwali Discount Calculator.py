"""
Diwali Discount Calculator
===========================
Advanced shopping bill calculator with multiple discount tiers
- Multiple items support
- Tiered discount system
- GST calculation
- Receipt generation
"""

from datetime import datetime


def calculate_discount(total, discount_rate):
    """Calculate discount amount."""
    return total * (discount_rate / 100)


def calculate_gst(amount, gst_rate=18):
    """Calculate GST on amount."""
    return amount * (gst_rate / 100)


def get_discount_tier(total):
    """Determine discount tier based on total."""
    if total >= 2000:
        return 20, "PLATINUM"
    elif total >= 1000:
        return 15, "GOLD"
    elif total >= 500:
        return 10, "SILVER"
    else:
        return 0, "NONE"


def print_receipt(items, prices, subtotal, discount_rate, discount_amt, gst_amt, final_total, tier):
    """Print formatted receipt."""
    print("\n" + "=" * 60)
    print("🪔 DIWALI SPECIAL SHOPPING RECEIPT 🪔".center(60))
    print("=" * 60)
    print(f"Date: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")
    print("─" * 60)
    
    # Items list
    print(f"{'Item':<30} {'Price (₹)':>15}")
    print("─" * 60)
    for item, price in zip(items, prices):
        print(f"{item:<30} ₹{price:>14.2f}")
    
    print("─" * 60)
    print(f"{'Subtotal':<30} ₹{subtotal:>14.2f}")
    
    if discount_amt > 0:
        print(f"{'Discount (' + str(discount_rate) + '% - ' + tier + ')':<30} -₹{discount_amt:>13.2f}")
    
    amount_before_gst = subtotal - discount_amt
    print(f"{'GST (18%)':<30} +₹{gst_amt:>13.2f}")
    print("─" * 60)
    print(f"{'FINAL TOTAL':<30} ₹{final_total:>14.2f}")
    print("=" * 60)
    
    if discount_amt > 0:
        savings = discount_amt
        print(f"🎉 You saved ₹{savings:.2f} with {tier} discount! 🎉".center(60))
    
    print(f"Thank you for shopping! Happy Diwali! 🪔".center(60))
    print("=" * 60)


def simple_calculator():
    """Simple single-list input calculator."""
    print("\n📝 SIMPLE MODE")
    print("─" * 60)
    
    prices = []
    print("Enter item prices (enter 0 to finish):")
    
    item_num = 1
    while True:
        try:
            price = float(input(f"Item {item_num} price: ₹"))
            if price == 0:
                break
            if price < 0:
                print("❌ Price cannot be negative!")
                continue
            prices.append(price)
            item_num += 1
        except ValueError:
            print("❌ Invalid price! Enter a number.")
    
    if not prices:
        print("❌ No items entered!")
        return
    
    subtotal = sum(prices)
    discount_rate, tier = get_discount_tier(subtotal)
    discount_amt = calculate_discount(subtotal, discount_rate)
    amount_after_discount = subtotal - discount_amt
    gst_amt = calculate_gst(amount_after_discount)
    final_total = amount_after_discount + gst_amt
    
    items = [f"Item {i+1}" for i in range(len(prices))]
    print_receipt(items, prices, subtotal, discount_rate, discount_amt, gst_amt, final_total, tier)


def detailed_calculator():
    """Detailed mode with item names."""
    print("\n📝 DETAILED MODE")
    print("─" * 60)
    
    items = []
    prices = []
    
    print("Enter items (type 'done' when finished):")
    
    while True:
        item_name = input("\nItem name: ").strip()
        if item_name.lower() == 'done':
            break
        if not item_name:
            print("❌ Item name cannot be empty!")
            continue
        
        while True:
            try:
                price = float(input(f"Price for {item_name}: ₹"))
                if price < 0:
                    print("❌ Price cannot be negative!")
                    continue
                break
            except ValueError:
                print("❌ Invalid price!")
        
        items.append(item_name)
        prices.append(price)
        print(f"✓ Added: {item_name} - ₹{price:.2f}")
    
    if not items:
        print("❌ No items entered!")
        return
    
    subtotal = sum(prices)
    discount_rate, tier = get_discount_tier(subtotal)
    discount_amt = calculate_discount(subtotal, discount_rate)
    amount_after_discount = subtotal - discount_amt
    gst_amt = calculate_gst(amount_after_discount)
    final_total = amount_after_discount + gst_amt
    
    print_receipt(items, prices, subtotal, discount_rate, discount_amt, gst_amt, final_total, tier)


def discount_tiers_info():
    """Display discount tier information."""
    print("\n💎 DIWALI DISCOUNT TIERS 💎")
    print("=" * 60)
    print(f"{'Tier':<15} {'Min Amount':<15} {'Discount':<15}")
    print("─" * 60)
    print(f"{'PLATINUM':<15} {'₹2000+':<15} {'20%':<15}")
    print(f"{'GOLD':<15} {'₹1000-1999':<15} {'15%':<15}")
    print(f"{'SILVER':<15} {'₹500-999':<15} {'10%':<15}")
    print(f"{'NONE':<15} {'Below ₹500':<15} {'0%':<15}")
    print("=" * 60)
    print("📌 GST (18%) applies to all purchases after discount")
    print("=" * 60)


def quick_calculator():
    """Quick single-line calculator."""
    print("\n⚡ QUICK MODE")
    print("─" * 60)
    
    try:
        prices_input = input("Enter all prices separated by spaces: ₹")
        prices = [float(p) for p in prices_input.split()]
        
        if not prices:
            print("❌ No prices entered!")
            return
        
        subtotal = sum(prices)
        discount_rate, tier = get_discount_tier(subtotal)
        discount_amt = calculate_discount(subtotal, discount_rate)
        amount_after_discount = subtotal - discount_amt
        gst_amt = calculate_gst(amount_after_discount)
        final_total = amount_after_discount + gst_amt
        
        items = [f"Item {i+1}" for i in range(len(prices))]
        print_receipt(items, prices, subtotal, discount_rate, discount_amt, gst_amt, final_total, tier)
        
    except ValueError:
        print("❌ Invalid input! Enter numbers only.")


def main():
    """Main function with menu."""
    print("=" * 60)
    print("🎊 DIWALI DISCOUNT CALCULATOR 🎊")
    print("=" * 60)
    
    while True:
        print("\n" + "─" * 60)
        print("Choose Calculator Mode:")
        print("─" * 60)
        print("1. Simple Mode (Enter prices only)")
        print("2. Detailed Mode (Item names + prices)")
        print("3. Quick Mode (All prices at once)")
        print("4. View Discount Tiers")
        print("5. Exit")
        print("─" * 60)
        
        try:
            choice = int(input("\nEnter your choice (1-5): "))
            
            if choice == 1:
                simple_calculator()
            elif choice == 2:
                detailed_calculator()
            elif choice == 3:
                quick_calculator()
            elif choice == 4:
                discount_tiers_info()
            elif choice == 5:
                print("\n" + "=" * 60)
                print("Thank you! Happy Diwali! 🪔".center(60))
                print("=" * 60)
                break
            else:
                print("❌ Choose between 1-5!")
                
        except ValueError:
            print("❌ Invalid choice!")


if __name__ == "__main__":
    main()
