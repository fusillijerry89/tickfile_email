import yagmail

receiver = "luke.tych@gmail.com"

def send_mail(contents):
    receiver = "luke.tych@gmail.com"

    yag = yagmail.SMTP("mr.landerson69@gmail.com")
    #yag.send(
    #    to = receiver,
    #    subject = "Tickler File",
    #    contents = contents
    #)

    yag = yagmail.inline("mr.landerson69@gmail.com")

    yag.send(
        to = receiver,
        subject = "Tickler File",
        contents = [
            "Hello Mike! Here is a picture I took last week:",
            {'img.jpg': 'PictureForMike'}
        ]
    )

contents = "Hello Mike! Here is a picture I took last week: {'img.jpg': 'PictureForMike'}. Do you like it?"

contents = yagmail.inline(contents)

send_mail(contents)
