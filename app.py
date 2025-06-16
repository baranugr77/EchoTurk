from flask import Flask, render_template, request
from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer
from gtts import gTTS
import os
import uuid
import x.lmr as xlm  # DUYGU ANALİZİ MODÜLÜ

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static'

# Çeviri modeli
model_name = "facebook/m2m100_418M"
tokenizer = M2M100Tokenizer.from_pretrained(model_name)
model = M2M100ForConditionalGeneration.from_pretrained(model_name)

# HTML sayfası
@app.route("/", methods=["GET", "POST"])
def index():
    input_text = ""
    translated_text = ""
    source_lang = "tr"
    target_lang = "en"
    input_audio_path = ""
    output_audio_path = ""
    duygu = ""

    if request.method == "POST":
        input_text = request.form.get("input_text")
        source_lang = request.form.get("source_lang")
        target_lang = request.form.get("target_lang")

        if input_text.strip():
            # Çeviri işlemi
            tokenizer.src_lang = source_lang
            encoded = tokenizer(input_text, return_tensors="pt")
            generated_tokens = model.generate(
                **encoded,
                forced_bos_token_id=tokenizer.get_lang_id(target_lang)
            )
            translated_text = tokenizer.decode(generated_tokens[0], skip_special_tokens=True)

            # Duygu analizi
            duygu = xlm.analyze_emotion(input_text)

            # Giriş dili ses dosyası oluştur
            input_audio_filename = f"{uuid.uuid4()}.mp3"
            input_audio_path = os.path.join(app.config['UPLOAD_FOLDER'], input_audio_filename)
            gTTS(text=input_text, lang=source_lang).save(input_audio_path)

            # Çeviri dili ses dosyası oluştur
            output_audio_filename = f"{uuid.uuid4()}.mp3"
            output_audio_path = os.path.join(app.config['UPLOAD_FOLDER'], output_audio_filename)
            gTTS(text=translated_text, lang=target_lang).save(output_audio_path)

    return render_template("index.html",
                           input_text=input_text,
                           translated_text=translated_text,
                           source_lang=source_lang,
                           target_lang=target_lang,
                           input_audio=input_audio_path,
                           output_audio=output_audio_path,
                           duygu=duygu)

if __name__ == "__main__":
    app.run(debug=True)
