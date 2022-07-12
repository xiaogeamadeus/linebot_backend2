def create_single_text_message(message):
    if message == 'Thank you':
        message = 'You are welcome!'
    test_message = [
                {
                   'type': 'text',
                   'text': message
                }
            ]
    return test_message