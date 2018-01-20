import cv2
import matplotlib.pyplot as plt

def load_image(path):
    """Load an image
    
    Arguments:
        path {String} -- Path to source location
    
    Returns:
        Array -- Image RGB content in Matplot Array
    """

    image = cv2.imread(path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    return image


def display_image(image):
    plt.imshow(image)
    plt.show()
