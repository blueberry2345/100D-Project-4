from PIL import Image, ImageDraw, ImageFont
import tkinter

# List of possible options
placement_options = ["Center", "Top left", "Top right", "Bottom left", "Bottom right"]

# Function that takes in desired location of the watermark, the file location of the image and the watermark text and produces the image with the watermark
def implement_watermark(location, image_path, watermark_text):

    # Open the image and allow it to be edited
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)

    # Get the horizontal and vertical size of the image
    x, y = image.size

    # Choose the lesser of x or y for what we'll use for the font size
    f_size = min(x,y)


    # Set the font and size for the watermark text
    font = ImageFont.truetype("arial.ttf", round(f_size / 12))

    # Set watermark location to center unless fulfills one of the if conditions
    watermark_xy = (x/2, y/2)
    if location == "Top left":
        watermark_xy = (0,0)
    elif location == "Top right":
        watermark_xy = (x-(x/4),0)
    elif location == "Bottom left":
        watermark_xy = (0,y-(y/4))
    elif location == "Bottom right":
        watermark_xy = (x-(x/4),y-(y/4))


    # Place watermark in image
    draw.text(watermark_xy, watermark_text, fill=(255, 255, 255, 64), font=font)


    # Puts 'watermarked' at the end of file name to save
    end_of_file_name = image_path.rfind(".")
    image.save(image_path[:end_of_file_name] + "watermarked" + image_path[end_of_file_name:])


# Creates a new window with title and minimum size
window = tkinter.Tk()
window.title("Watermark program")
window.minsize(width=500, height=300)


# Creates a grid to place displayed objects
window.grid()


# Creation of empty label
empty_label = tkinter.Label(text="")
empty_label.grid(row=0, column=0)


# Creation of header label
top_label = tkinter.Label(window, text="Where do you want the watermark to be?", font=("Arial", 12, "bold"))
top_label.grid(column = 1,row = 0)


# Creation of label and input box for user to put in their desired watermark text
watermark_text_label = tkinter.Label(window, text="Watermark text")
watermark_text_label.grid(column=0, row=1)

watermark_text_box = tkinter.Entry(window)
watermark_text_box.grid(column=1, row=1)


# Creation of label and input box for user to put file path of source image
file_path_label = tkinter.Label(window, text="Image file path")
file_path_label.grid(column=0, row=2)

file_path_box = tkinter.Entry(window)
file_path_box.grid(column=1, row=2)


# Creation of option menu for where you want the placement of the watermark
selected_option = tkinter.StringVar(window)
selected_option.set(placement_options[0])

option_list = tkinter.OptionMenu(window, selected_option, *placement_options)
option_list.grid(column=1, row=3)


# Button to implement watermark
button = tkinter.Button(window, command= lambda: implement_watermark(selected_option.get(), file_path_box.get(), watermark_text_box.get()), width=6, height=1, text="Submit")
button.grid(column=1, row=4)


window.mainloop()
