import eml_parser
import base64

def main(req):
    eml_content = req.get_body()
    parsed_eml = eml_parser.eml_parser.decode_email_bytes(eml_content)

    subject = parsed_eml['header']['subject']
    attachments = parsed_eml['attachments']

    return {
        "subject": subject,
        "attachments": [
            {
                "filename": att['filename'],
                "content": base64.b64encode(att['raw']).decode()
            } for att in attachments
        ]
    }
