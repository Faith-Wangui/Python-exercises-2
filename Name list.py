def get_names():
    names = input("Enter a list of names ").strip()
    name_list = [name.strip() for name in names.split(",") if name.strip()]
    return name_list

def process_names(name_list):
    unique_names = sorted(set(name_list))  # Remove duplicates and sort
    return unique_names

def main():
    name_list = get_names()
    if not name_list:
        print("No names entered. Please try again.")
        return
    
    unique_sorted_names = process_names(name_list)
    
    print("\nFinal sorted list of names:")
    for name in unique_sorted_names:
        print(name)
    
    print(f"\nTotal number of names entered: {len(unique_sorted_names)}")

if __name__ == "__main__":
    main()


