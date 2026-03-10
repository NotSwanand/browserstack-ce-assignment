from deep_translator import GoogleTranslator


def translate_titles(titles):
    translated = []

    for t in titles:
        english = GoogleTranslator(
            source='auto',
            target='en'
        ).translate(t)

        translated.append(english)

    return translated