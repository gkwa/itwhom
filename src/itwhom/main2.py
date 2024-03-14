import frontmatter

def get_frontmatter(file_path):
    with open(file_path, 'r') as file:
        post = frontmatter.load(file)
    return post

def update_frontmatter(file_path, key, value):
    post = get_frontmatter(file_path)
    post[key] = value
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(frontmatter.dumps(post))

