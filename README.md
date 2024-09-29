# WebInitializer
WebInitializer is a Python script that quickly sets up a basic web project structure. It creates a new folder and generates starter HTML, CSS, and JavaScript files within it.

[web initializer](https://private-user-images.githubusercontent.com/98550/371869216-f60a9951-5c5b-45bb-8d9d-397442911185.webm)

# WebInitializer

WebInitializer is a Python script that quickly sets up a basic web project structure. It creates a new folder and generates starter HTML, CSS, and JavaScript files within it.

## Features

- Creates a new project folder
- Generates basic HTML, CSS, and JavaScript files
- Allows customization of file names
- Provides a simple starting point for web development projects

## Usage

Run the script from the command line:

```
python3 web_initializer.py <folder_name> [--html <html_file>] [--css <css_file>] [--js <js_file>]
```

### Arguments:

- `folder_name`: Name of the folder to create (required)
- `--html`: Name of the HTML file (default: index.html)
- `--css`: Name of the CSS file (default: style.css)
- `--js`: Name of the JavaScript file (default: script.js)

### Example:

```
python3 web_initializer.py my_project --html custom.html --css custom.css --js custom.js
```

This will create a folder named `my_project` containing `custom.html`, `custom.css`, and `custom.js` files.

## Requirements

- Python 3.6 or higher

## Contributing

Feel free to fork this project and submit pull requests with improvements or additional features!

## License

This project is open source and available under the [MIT License](LICENSE).
