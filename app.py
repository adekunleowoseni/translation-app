from flask import Flask, render_template, request, jsonify, url_for
from googletrans import Translator

app = Flask(__name__, static_url_path='/static')
translator = Translator()

@app.route('/', methods=['GET', 'POST'])
def translate_text():
    translated_text = ""
    source_text = ""
    
    if request.method == 'POST':
        try:
            source_text = request.form.get('text', '')
            target_lang = request.form.get('target_lang', 'en')
            
            if source_text:
                translation = translator.translate(source_text, dest=target_lang)
                translated_text = translation.text
                
        except Exception as e:
            print(f"Translation error: {e}")
            translated_text = "Error during translation"
    
    return render_template('index.html', 
                         translated_text=translated_text, 
                         source_text=source_text)

if __name__ == '__main__':
    app.run(debug=True) 