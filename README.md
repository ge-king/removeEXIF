
# Batch EXIF Data Remover

Batch EXIF Data Remover is a simple Python application that allows users to remove all EXIF data from a batch of selected JPEG images. The app comes with a user-friendly graphical interface built using the Tkinter library and ttk theme.

## Dependencies

This application depends on the following libraries:

-   tkinter
-   ttk
-   PIL (Pillow)
-   os
-   sv_ttk (custom ttk theme)

Ensure that you have these libraries installed before running the application.

## Installation via Release

Download the latest release from Github. Run the exe.


## Installation via Clone

To get started with the Batch EXIF Data Remover, follow these steps:

1.  Clone this repository:

    `git clone https://github.com/yourusername/batch-exif-data-remover.git` 
    
2.  Change to the project directory:

    `cd batch-exif-data-remover` 
    
3.  Install the required libraries using pip:

    `pip install -r requirements.txt` 
   
   
4.  Run the main script:

    `python main.py` 
    

## Usage

To use the Batch EXIF Data Remover, follow these steps:

1.  Click on the "Add images" button to select the JPEG images you want to remove EXIF data from.
2.  Review the list of selected images and their current EXIF data status in the table.
3.  (Optional) Use the "Remove selected" button to remove any unwanted images from the list.
4.  Click on the "Delete EXIF data from all listed images" button to start the batch removal process.
5.  Monitor the progress bar as the application processes each image.
6.  Once the process is complete, the table will be updated with the new EXIF data status for each image.

**Note:** It's recommended to backup your original images before using this application, as the removal process is irreversible.

## License

This project is released under the [MIT License](https://chat.openai.com/LICENSE).
