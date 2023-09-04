# Flask File Upload and Download Service

This is a simple Flask application that allows you to upload and download files. It uses the Transfer.sh service for temporary file storage.

## Prerequisites

Make sure you have Python and Flask installed on your system. You can install Flask using pip: pip install Flask


## Getting Started

1. Clone this repository to your local machine.

2. Run the Flask application: python main.py

4. The application will be running at `http://localhost:8081`.

## Usage

### Uploading a File

To upload a file, make a POST request to `/api/upload`. Use a tool like `curl` or Postman, or integrate it into your own application.

Example using `curl`: curl -F "file=@your_file.txt" http://localhost:8081/api/upload

You will receive a JSON response with a download URL and the deletion date for the uploaded file.

### Downloading a File

To download a file, make a GET request to `/download` with the `filename` query parameter.

Example: http://localhost:8081/download?filename=your_file.txt


Replace `your_file.txt` with the name of the file you want to download.

## Configuration

- `globalUrl`: The base URL for file downloads.
- `MAX_FILE_STORAGE_DAYS`: The number of days a file should be stored before deletion.

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.




