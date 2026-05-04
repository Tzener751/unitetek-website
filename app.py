from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/products/solvent-recovery')
def product_detail():
    return render_template('product_detail.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/history')
def history():
    return render_template('history.html')

@app.route('/news')
def news():
    return render_template('news.html')


@app.route('/products/utfr-nal')
def product_nal():
    return render_template('product_detail.html', 
                           title="UTFR-NAL 產品規格書", 
                           pdf_file="pdf/product_NAL.pdf")

if __name__ == '__main__':
    app.run(debug=True, port=5502)