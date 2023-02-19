from tkinter import *
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk, ImageFont, ImageDraw

img_data = None
displayed_photo = None
show_image = None
filepath = ""


# ---------------------------- FUNCTIONS ------------------------------- #
def upload_image():
    global img_data
    global displayed_photo
    global filepath
    global show_image

    f_types = [('Jpg Files', '*.jpg')]
    filepath = filedialog.askopenfilename(filetypes=f_types)
    img_data = Image.open(filepath)

    displayed_photo = ImageTk.PhotoImage(file=filepath)
    show_image = ttk.Button(window, image=displayed_photo)
    show_image.grid(column=0, row=2, columnspan=3)

    # UI
    canvas.grid_forget()

    add_watermark_button = ttk.Button(text="Add watermark", width=23, command=add_watermark)
    add_watermark_button.grid(column=2, row=0)

    close_app_button = ttk.Button(text="Close App", width=23, command=close_app)
    close_app_button.grid(column=0, row=0)
    add_watermark_button = ttk.Button(text="Add watermark", width=23, command=add_watermark)
    add_watermark_button.grid(column=2, row=0)

    close_app_button = ttk.Button(text="Close App", width=23, command=close_app)
    close_app_button.grid(column=0, row=0)

    label.destroy()
    import_button.grid(column=1, row=0)


def add_watermark():
    global displayed_photo
    global show_image
    photo = Image.open(filepath)
    w, h = photo.size

    drawing = ImageDraw.Draw(photo)
    font = ImageFont.truetype("CarryYouRegular-3z71M.ttf", 30)

    text = " © Gregory Freen   "
    text_w, text_h = drawing.textsize(text, font)

    pos = w - text_w, (h - text_h) - 20

    c_text = Image.new('RGB', (text_w, text_h), color='#000000')
    drawing = ImageDraw.Draw(c_text)

    drawing.text((0, 0), text, fill="#ffffff", font=font)
    c_text.putalpha(100)

    # Saving photo
    photo.paste(c_text, pos, c_text)
    new_filepath = f"{filepath.strip('.jpg')}_watermarked.jpg"
    photo.save(new_filepath)

    # Display watermarked photo
    displayed_photo = ImageTk.PhotoImage(file=new_filepath)
    show_image.config(image=displayed_photo)

    messagebox.showinfo("Notice", "Images saved on your disk.")


def close_app():
    window.quit()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Image Watermarking App")
window.config(pady=15, padx=20)


label = ttk.Label(text="Select the photo you want to add a watermark.")
label.grid(column=1, row=0)

import_button = ttk.Button(text="Select Image", width=23, command=upload_image)
import_button.grid(column=1, row=1, pady=10)

logo_img = PhotoImage(file="icon.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=0, row=2, columnspan=3, pady=10, padx=10)


window.mainloop()
