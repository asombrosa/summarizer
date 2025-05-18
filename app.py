from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    summary = None
    if request.method == 'POST':
        text = request.form.get('text', '')
        if text:
            # This is a simple example - in a real app, you would use a proper summarization model
            summary = summarize_text(text)
    return render_template('index.html', summary=summary)

def summarize_text(text):
    # This is a very basic summarization method
    # In a real application, you would use a proper NLP model
    words = text.split()
    if len(words) > 30:
        return ' '.join(words[:30]) + '...'
    return text

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)