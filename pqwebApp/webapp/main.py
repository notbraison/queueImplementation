from flask import Flask, render_template, request

app = Flask(__name__)

def process_text(input_text):
    # Add your text manipulation logic here
    # For demonstration, let's convert the text to uppercase
    processed_text = input_text.upper()
    return processed_text

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_text = request.form['input_text']
        processed_text = process_text(input_text)
        return render_template('index.html', input_text=input_text, processed_text=processed_text)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
