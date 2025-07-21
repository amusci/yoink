# Yoink Video Downloader

A simple, user-friendly GUI application for downloading videos from various platforms such as YouTube, X (Twitter), and Newgrounds.

## Features

- **Multi-Platform Support**: Download videos from YouTube, X (Twitter), and Newgrounds
- **Organized Downloads**: Automatically creates platform-specific subfolders
- **Folder Selection**: Choose your preferred download location

## Requirements

- Python 3.7 or higher
- Required Python packages:
  - `tkinter` 
  - `customtkinter`
  - `yt-dlp`

## Installation

1. **Clone or download** this repository to your local machine

2. **Install required dependencies**:
   ```bash
   pip install customtkinter yt-dlp
   ```

3. **Run the application**:
   ```bash
   python yoink.py
   ```

## Usage

1. **Launch the application** by running the Python script
2. **Select Platform**: Choose from YouTube, X, or Newgrounds using the dropdown menu
3. **Choose Download Folder**: Click "Browse" to select where you want videos saved
4. **Enter Video Link**: Paste the URL of the video you want to download
5. **Click "Yoink Video"** to start the download

### Download Organization

Videos are automatically organized into platform-specific subfolders:
- `your_download_folder/YouTube/`
- `your_download_folder/X/`
- `your_download_folder/Newgrounds/`

## Supported Platforms

- **YouTube**: Full video and audio download support
- **X (Twitter)**: Video tweets and media content
- **Newgrounds**: Flash animations and video content

## Error Handling

The application provides clear feedback for common issues:
- Missing video link
- No download folder selected
- Network errors
- Invalid URLs
- Platform-specific download failures

## File Naming

Downloaded files use the original video title with the appropriate file extension (e.g., `.mp4`, `.webm`).

## Technical Details

- Built with Python's `tkinter` and `customtkinter` for the GUI
- Uses `yt-dlp` as the download engine (a more actively maintained fork of youtube-dl)
- Automatically handles various video formats and quality options
- Creates necessary directories if they don't exist

## Troubleshooting

**Common Issues:**

1. **"Please enter a valid link"**: Make sure you've pasted a complete URL
2. **"Please select a download folder"**: Use the Browse button to choose a destination
3. **Download failures**: Check your internet connection and ensure the video URL is accessible

**Dependencies Issues:**
```bash
# If you encounter import errors, try:
pip install --upgrade customtkinter yt-dlp

# For macOS users with tkinter issues:
brew install python-tk
```

## License

This project is for educational and personal use.

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve the application.

---

**Disclaimer**: This tool is intended for personal use and downloading content you have permission to access.
