from fpdf import FPDF


def main():
    user_input = input("Name: ")
    print_pdf(user_input)


def print_pdf(user_input):
    pdf = FPDF(orientation="portrait", format="A4")
    pdf.add_page()
    pdf.set_margin(0)
    pdf.image("shirtificate.png", x=5, y=20, w=200)
    pdf.set_font('helvetica', size=12)
    pdf.text(92, 10, "CS50 Shirtificate")
    pdf.set_text_color(255, 255, 255)
    pdf.text(100, 100, user_input)
    #pdf.cell(text=user_input, center=True, new_x=XPos.CENTER, new_y=YPos.TMARGIN)
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
