def create_single_text_message(message):
    return [{"type": "text", "text": message}]


def create_single_message(message):
    print(message)
    if message["type"] == "text":
        return [{"type": "text", "text": message["value"]}]
    if message["type"] == "stamp":
        return [
            {
                "type": "sticker",
                "packageId": stamp_data[message["value"]]["package"],
                "stickerId": stamp_data[message["value"]]["sticker"],
            }
        ]


stamp_data = {
    "ok": {"package": "789", "sticker": "10858"},
    "yes": {"package": "789", "sticker": "10859"},
    "no": {"package": "789", "sticker": "10860"},
    "enjoy": {"package": "789", "sticker": "10855"},
    "stargazing": {"package": "789", "sticker": "10881"},
    "sad": {"package": "789", "sticker": "10879"},
}
