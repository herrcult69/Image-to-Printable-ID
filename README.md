# Image-to-Printable-ID

## Overview

ID Card Image Processor is a Python-based tool designed to warp and crop images, specifically for preparing ID card photos for printing. This project ease the process of extracting an ID card from a warped image using a photo editing tool.
## Features
- **Image Rotating**: Adjusts the rotation of the image for easy rewarping process.
- **Image Cropping**: Crops the image to the required dimensions for ID cards.
- **Image Warping**: Adjusts the perspective of the image to ensure proper alignment.
- **User-Friendly Interface**: Simple and intuitive interface for easy use.
- **High-Quality Output**: Ensures that the processed images are of high quality, suitable for printing.

## Installation

To install the necessary dependencies, run:

```bash
pip install -r requirements.txt
```

## Usage

1. **Prepare Your Image**: Ensure your image is in a supported format (e.g., JPEG, PNG).
2. **Run the Script**: Use the following command to process your image:

    ```bash
    python run.py
    ```

3. **Pre-Editing stage**:
    - `Load Image`: Open the image you want to process.
    - `Rotate Image`: Rotate the image 90 degrees if needed.
    - `Choose image`: Submit the pre-edited image.
3. **Magic Croping stage**:
   - Using for individual pointers to match the corners of the ID cards
   - `Crop image`: Submit the magic-cropped image. 

## Example
![image](https://github.com/user-attachments/assets/22c441df-761c-4f66-85e9-465e2a95c379)

*The pre-editing GUI

![image](https://github.com/user-attachments/assets/63ac612a-bc51-4d22-a7c1-b2915b049836)

*File Selection

![image](https://github.com/user-attachments/assets/00713f2f-3d2e-4f40-a4f9-ac611604f768)

*Rotating

![image](https://github.com/user-attachments/assets/ac94992c-b643-4500-85f0-a70efbe4801c)

*Magic Cropping

![image](https://github.com/user-attachments/assets/e8552255-ca5e-455d-aa63-3b08ba2d57d0)

*Magic Cropping after configuration

![image](https://github.com/user-attachments/assets/386d8ce7-2ed1-45f8-a36e-e7242817bcfc)

*Ouput file



## Dependencies

- Python 3.12
- OpenCV
- NumPy

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, please contact herrcult69 at hoalehuynhvan@gmail.com.


