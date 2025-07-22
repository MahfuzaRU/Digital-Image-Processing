''' 
Problem Statement: 
Given an image, this script load the image, convert it from 4D to 3D, print some pixel values
and display the image using matplotlib.
'''


import matplotlib.pyplot as plt

def main():
    img_path = '/home/mahfuza/CSE4161_DIP/Images/MyScreen.png'
    
    img_4D = plt.imread(img_path)
    print(img_4D.shape)
    
    # Convert 4D image into a 3D image
    img_3D = img_4D[:, :, :3]
    print(img_3D.shape)
    
    # Print some pixel values
    print(img_3D[:5:5, 0])
    print(img_3D.max(), img_3D.min())
    
    # Display the loaded 3D image
    plt.imshow(img_3D)
    plt.show()
    plt.close()

if __name__ == "__main__":
    main()

