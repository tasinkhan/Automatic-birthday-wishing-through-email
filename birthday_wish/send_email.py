class SendEmail:
    @classmethod
    def send_mail(cls, name=None, email=None):
        from_email = "admin@admin.com"
        subject = f"Happy Birthday {name} 🥧"
        recipient = email
        body = f"Dear {name},\n We value your special day just as much as we value you. On your birthday, we send you our warmest and most heartfelt wishes. \n Regards,\n Admin"

        email_template = f"from: {from_email} \n to:{recipient} \n subject:{subject} \n {body}"
        print(email_template)

        return email_template