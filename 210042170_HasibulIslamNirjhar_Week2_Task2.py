import cv2 as cv2
import numpy as np



def detect_red_and_white_regions(image):
    img = cv2.imread(image, cv2.IMREAD_UNCHANGED)
    original_image = cv2.resize(img, (0, 0), fx=0.8, fy=0.8)
    cv2.imshow("Original image", original_image)

    hsvImg = cv2.cvtColor(original_image, cv2.COLOR_BGR2HSV)

    red_lower = np.array([160, 50, 50], dtype=np.uint8)
    red_upper = np.array([180, 255, 255], dtype=np.uint8)
    red_mask = cv2.inRange(hsvImg, red_lower, red_upper)
    res_red = cv2.bitwise_and(original_image, original_image, mask=red_mask)
    cv2.imshow("Red", res_red)

    white_lower = np.array([0, 0, 200], dtype=np.uint8)
    white_upper = np.array([180, 30, 255], dtype=np.uint8)
    white_mask = cv2.inRange(hsvImg, white_lower, white_upper)
    res_white = cv2.bitwise_and(original_image, original_image, mask=white_mask)
    cv2.imshow("White", res_white)

    return original_image, res_red, res_white

def analyze_goat(image_array):
    min_pixel = np.min(image_array)
    max_pixel = np.max(image_array)
    average_pixel = np.mean(image_array)
    num_foreground_pixels = np.count_nonzero(image_array)
    num_background_pixels = image_array.size - num_foreground_pixels

    font = cv2.FONT_HERSHEY_TRIPLEX
    bottom_left_corner = (10, 30)
    font_scale = 1
    font_color = (255, 255, 255)
    line_type = 2

    image_with_info = cv2.merge((image_array, image_array, image_array))

    cv2.putText(image_with_info, f"Min Pixel Value: {min_pixel}", bottom_left_corner, font, font_scale, font_color, line_type)
    cv2.putText(image_with_info, f"Max Pixel Value: {max_pixel}", (10, 60), font, font_scale, font_color, line_type)
    cv2.putText(image_with_info, f"Avg Pixel Value: {average_pixel:.2f}", (10, 90), font, font_scale, font_color, line_type)
    cv2.putText(image_with_info, f"Foreground Pixels: {num_foreground_pixels}", (10, 120), font, font_scale, font_color, line_type)
    cv2.putText(image_with_info, f"Background Pixels: {num_background_pixels}", (10, 150), font, font_scale, font_color, line_type)

    cv2.imshow("Processed Image", image_with_info)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


pic = r'C:\Users\hasib\Downloads\GOAT.jpg'


original_image, res_red, res_white = detect_red_and_white_regions(pic)


grayscale_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
analyze_goat(grayscale_image)
