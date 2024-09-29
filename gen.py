import sys
import argparse
import os

def create_folder(folder_name):
    try:
        os.makedirs(folder_name, exist_ok=True)
        print(f"Folder '{folder_name}' created successfully.")
    except OSError as e:
        print(f"Error creating folder '{folder_name}': {e}")
        sys.exit(1)

def create_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"File '{file_path}' created successfully.")

def generate_files(folder_name, html_name='index.html', css_name='style.css', js_name='script.js'):
    create_folder(folder_name)

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Generated Page</title>
    <link rel="stylesheet" href="{css_name}">
    <script src="{js_name}" defer></script>
</head>
<body>
    <h1>Welcome to the Generated Page</h1>
    <p>This page was generated using a Python script.</p>
</body>
</html>
"""

    css_content = """body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: #333;
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
}

h1 {
    color: #2c3e50;
}
"""

    js_content = """document.addEventListener('DOMContentLoaded', (event) => {
    console.log('DOM fully loaded and parsed');
    // Add your JavaScript code here
});
"""

    create_file(os.path.join(folder_name, html_name), html_content)
    create_file(os.path.join(folder_name, css_name), css_content)
    create_file(os.path.join(folder_name, js_name), js_content)

    print(f"\nAll files have been generated in the '{folder_name}' folder.")

def main():
    parser = argparse.ArgumentParser(description='Generate an HTML file with CSS and JavaScript in a new folder.')
    parser.add_argument('folder_name', help='Name of the folder to create')
    parser.add_argument('--html', default='index.html', help='Name of the HTML file (default: index.html)')
    parser.add_argument('--css', default='style.css', help='Name of the CSS file (default: style.css)')
    parser.add_argument('--js', default='script.js', help='Name of the JavaScript file (default: script.js)')

    args = parser.parse_args()

    generate_files(args.folder_name, args.html, args.css, args.js)

if __name__ == "__main__":
    main()
