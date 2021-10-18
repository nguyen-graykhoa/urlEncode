def urlEncode(text):
    text = text.strip()
    final_text = ''
    words = text.split(' ')
     
    for word in words:
        final_text = final_text + word + '%'
    return final_text[0: (len(final_text) - 1)]
