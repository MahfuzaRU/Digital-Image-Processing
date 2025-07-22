'''  
Given an image, this script load the image, convert it from 4D to 3D, perform the given transformations:
g(x, y, c) = max(f(x, y, c)) - f(x, y, c) 

here, f(x, y, c) is the pixel value at position (x, y) for channel c = 3.
'''


import matplotlib.pyplot as plt

def main():
    img_path = '/home/mahfuza/CSE4161_DIP/Images/ColourImage.png'
    img_4D = plt.imread(img_path)
    print(img_4D.shape)

    # Convert to 3D by removing alpha channel
    img_3D = img_4D[:, :, :3]
    print(img_3D.shape)
    
    # Prepare negative of loaded image
    negative_img = img_3D.max() - img_3D

    # Print RGB values of top-left corner
    print(img_3D[:5, :5, 0])
    print(img_3D.max(), img_3D.min())

    # Show the image and its channels
    plt.figure(figsize=(10, 10))
    plt.subplot(2, 3, 1)
    plt.imshow(img_3D)
    plt.subplot(2, 3, 2)
    plt.imshow(img_3D[:, :, 0], cmap='Reds')
    plt.subplot(2, 3, 3)
    plt.imshow(img_3D[:, :, 1], cmap='Greens')
    plt.subplot(2, 3, 4)
    plt.imshow(img_3D[:, :, 2], cmap='Blues')
    plt.subplot(2, 3, 5)
    plt.imshow(img_3D[:, :, 0], cmap='gray')
    plt.subplot(2, 3, 6)
    plt.imshow(negative_img)
    plt.show()

if __name__ == "__main__":
    main()

