from deep_translator import GoogleTranslator
import difflib

def translate(text, source, target):
    try:
        return GoogleTranslator(source=source, target=target).translate(text)
    except Exception as e:
        return f"Çeviri başarısız: {e}"

def similarity_score(text1, text2):
    return round(difflib.SequenceMatcher(None, text1, text2).ratio() * 100, 2)
