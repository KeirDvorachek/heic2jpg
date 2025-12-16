# heic2jpg
An application that takes HEIC formatted images and converts them to JPG format.

## The Problem
When transferring photos from iPhone to Windows, iOS automatically converts HEIC images to JPEG - a process that can take hours for large photo libraries.

## The Solution
This tool lets you transfer photos in their native HEIC format (fast), then batch convert them to JPEG on your PC in minutes instead of hours.

## Features 
- ✅ HEIC to JPG conversion
- ✅ Batch directory processing
- ✅ EXIF metadata preservation
- ✅ Automatic image orientation correction
- 🚧 Face detection and tagging (planned)

## Installation

### Requirements
- Python 3.8 or higher
- Windows 10/11

### Setup
1. Clone the repository:
```bash
   git clone https://github.com/KeirDvorachek/heic2jpg.git
   cd heic2jpg
```

2. Install dependencies:
```bash
   pip install -r requirements.txt
```

## Usage

### Method 1: Drag and Drop (Easiest)
1. Drag a folder containing HEIC images onto `convert.bat`
2. The script will create two subfolders:
   - `ProcessedImages/` - your converted JPEGs
   - `HEICImages/` - your original HEIC files (moved here after conversion)
3. Watch the progress indicator as files are converted

### Method 2: Command Line
```bash
python HEIC2JPG.py <folder_with_heic_files>
```

Example:
```bash
python HEIC2JPG.py C:\iPhone_Photos
```

The script will process all `.HEIC` files in the specified folder and organize them into subfolders.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.