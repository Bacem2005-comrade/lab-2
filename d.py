import csv

def count_long_names(file_path):
    count = 0
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file, delimiter=';')  # Specify the delimiter
        for row in reader:
            if len(row['Book-Title']) > 30:  # Use the correct header
                count += 1
    return count

def search_books_by_author(file_path, author_name, limit=None):
    results = []
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file, delimiter=';')  # Specify the delimiter
        for row in reader:
            if author_name.lower() in row['Book-Author'].lower():  # Use the correct header
                results.append(row)
                if limit and len(results) >= limit:
                    break
    return results

def generate_bibliographic_references(file_path, output_file_path):
    references = []
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file, delimiter=';')  # Specify the delimiter
        for row in reader:
            if row['Year-Of-Publication'] not in ['1991', '1996']:  # Use the correct header
                references.append(f"{row['Book-Author']}. {row['Book-Title']} - {row['Year-Of-Publication']}")
    
    import random
    selected_references = random.sample(references, min(20, len(references)))
    
    with open(output_file_path, mode='w') as output_file:
        for i, reference in enumerate(selected_references, start=1):
            output_file.write(f"{i}. {reference}n")

# Example usage
file_path = 'books-en.csv'  # Path to your CSV file
output_file_path = 'bibliographic_references.txt'  # Output file path

# Count long book titles
long_titles_count = count_long_names(file_path)
print(f"Number of books with titles longer than 30 characters: {long_titles_count}")

# Search for books by a specific author
author_name = "Mark P. O. Morford"
books_by_author = search_books_by_author(file_path, author_name)
print(f"Books by {author_name}: {books_by_author}")

# Generate bibliographic references
generate_bibliographic_references(file_path, output_file_path)
print(f"Bibliographic references generated in {output_file_path}.")
