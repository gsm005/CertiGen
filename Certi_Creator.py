from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import qrcode

def main():
    print("----- GSM's Certificate Creator -----")

    # Accept participant's name
    name = input("Enter Participant's Name:\n")
    
    # Accept event name
    event_name = input("Enter Event Name:\n")
    
    # Accept output directory path
    output_dir_path = r'C:\Users\Hp\Desktop\STinternship\CertiGen\CertificateGenerator_QR\Output\\'

    # Accept date from user
    date = input("Enter Date:\n")

    basewidth = 100
    hsize = 100

    # Use a default font
    selectFont = ImageFont.load_default()

    # Load the certificate template image
    template_path = r'C:\Users\Hp\Desktop\STinternship\CertiGen\CertificateGenerator_QR\template.jpg'
    img = Image.open(template_path)
    draw = ImageDraw.Draw(img)
    draw.text((270, 280), "Participation In " + event_name + " competition", (0, 0, 0), font=selectFont)
    draw.text((350, 410), name, (0, 0, 0), font=selectFont)
    draw.text((200, 500), date, (0, 0, 0), font=selectFont)
    
    # Generate QR Code for the file path
    QR_img = qrcode.make('https://erp.indira.com/use_name/certificate/' + name + '.pdf')
    QR_img = QR_img.resize((basewidth, hsize), Image.Resampling.LANCZOS)
    
    # Paste the QR code on the certificate image
    img.paste(QR_img, (0, 600))
    
    # Save the certificate
    img.save(output_dir_path + name + ".pdf", "PDF", resolution=100.0)
    
    print("Certificate Generated Successfully")
    input("Press Enter to Exit")

if __name__ == "__main__":
    main()
