def main():
    original_str = "python programming"

    # Extracting "Python" and "programming" using index slicing
    sub1 = original_str[:6].capitalize()  # Convert the first letter to uppercase
    sub2 = original_str[7:].capitalize()  # Convert the first letter to uppercase

    # Merging the substrings in the order sub2 + sub1 with a space
    merged_str = sub2 + " " + sub1

    return sub1, sub2, merged_str

if __name__ == '__main__':
    sub1, sub2, merged_str = main()

    # Test the values
    expected_sub1 = "Python"
    expected_sub2 = "Programming"
    expected_merged_str = "Programming Python"

    assert sub1 == expected_sub1, f"Expected: {expected_sub1}, Got: {sub1}"
    assert sub2 == expected_sub2, f"Expected: {expected_sub2}, Got: {sub2}"
    assert merged_str == expected_merged_str, f"Expected: {expected_merged_str}, Got: {merged_str}"
