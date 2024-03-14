from . import main2

__project_name__ = "itwhom"

def main() -> int:
    file_path = "test.md"

    # Query the frontmatter
    post = main2.get_frontmatter(file_path)
    print("Title:", post.get("title", "N/A"))
    print("Author:", post.get("author", "N/A"))
    print("Date:", post.get("date", "N/A"))
    print("Tags:", post.get("tags", []))

    # Update the frontmatter
    main2.update_frontmatter(file_path, "author", "Jane Smith")
    main2.update_frontmatter(file_path, "tags", ["test", "example", "updated"])

    # Query the updated frontmatter
    updated_post = main2.get_frontmatter(file_path)
    print("\nUpdated frontmatter:")
    print("Title:", updated_post.get("title", "N/A"))
    print("Author:", updated_post.get("author", "N/A"))
    print("Date:", updated_post.get("date", "N/A"))
    print("Tags:", updated_post.get("tags", []))

    return 0
