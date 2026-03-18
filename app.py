from flask import Flask, render_template_string, url_for

app = Flask(__name__)

# ব্যবসার তথ্য
biz = {
    "name": "Unique Urban Arc",
    "tagline": "The Arc of Urban Discovery",
    "phone": "01909-671889",
    "fb": "https://www.facebook.com/uniqueurbanarc"
}

@app.route('/')
def home():
    # url_for ব্যবহার করে ছবির পাথ নির্ধারণ করা হলো
    logo_path = url_for('static', filename='logo.png')
    product_path = url_for('static', filename='wall_board_combo.jpg')
    
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="bn">
    <head>
        <meta charset="UTF-8">
        <title>{{ biz.name }}</title>
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap" rel="stylesheet">
        <style>
            :root { --primary: #0d3d2a; --accent: #d4af37; --success: #25d366; }
            body { font-family: 'Poppins', sans-serif; margin: 0; background: #f4f4f4; text-align: center; }
            header { background: var(--primary); color: white; padding: 25px; border-bottom: 5px solid var(--accent); }
            .container { max-width: 600px; margin: 20px auto; background: white; padding: 25px; border-radius: 15px; box-shadow: 0 10px 20px rgba(0,0,0,0.1); }
            .product-img { width: 100%; border-radius: 10px; margin-bottom: 15px; }
            .price-tag { font-size: 24px; color: #e74c3c; font-weight: bold; margin: 15px 0; }
            .calc-box { background: #f9f9f9; padding: 20px; border-radius: 10px; border: 1px solid #ddd; margin: 20px 0; }
            select, input { width: 100%; padding: 10px; margin: 5px 0; border: 1px solid #ccc; border-radius: 5px; }
            .total-bill { font-size: 22px; color: var(--primary); font-weight: bold; margin-top: 15px; border-top: 2px solid var(--accent); padding-top: 10px; }
            .btn { display: block; background: var(--success); color: white; padding: 15px; text-decoration: none; border-radius: 8px; font-weight: bold; margin-top: 20px; }
        </style>
    </head>
    <body>
        <header>
            <img src="{{ logo_path }}" height="60">
            <h1>{{ biz.name }}</h1>
        </header>
        <div class="container">
            <img src="{{ product_path }}" class="product-img">
            <h2>৯ পিসের এক্সক্লুসিভ ওয়াল বোর্ড কম্বো</h2>
            <div class="price-tag">৳ ৫৪০</div>
            <div class="calc-box">
                <label>পরিমাণ: </label>
                <input type="number" id="qty" value="1" min="1" oninput="updateTotal()">
                <label>ডেলিভারি এরিয়া: </label>
                <select id="delivery" onchange="updateTotal()">
                    <option value="60">ঢাকার ভিতরে (৳ ৬০)</option>
                    <option value="120">ঢাকার বাইরে (৳ ১২০)</option>
                </select>
                <div class="total-bill" id="bill_text">মোট বিল: ৳ ৬০০</div>
            </div>
            <a href="#" id="wa_btn" class="btn" target="_blank">হোয়াটসঅ্যাপে অর্ডার করুন</a>
        </div>
        <script>
            function updateTotal() {
                let qty = document.getElementById('qty').value;
                let delivery = parseInt(document.getElementById('delivery').value);
                let total = (qty * 540) + delivery;
                document.getElementById('bill_text').innerText = "মোট বিল: ৳ " + total;
                let msg = "আমি " + qty + " সেট ওয়াল বোর্ড অর্ডার করতে চাই। মোট বিল: ৳ " + total;
                document.getElementById('wa_btn').href = "https://wa.me/8801909671889?text=" + encodeURIComponent(msg);
            }
            window.onload = updateTotal;
        </script>
    </body>
    </html>
    ''', biz=biz, logo_path=logo_path, product_path=product_path)

if __name__ == '__main__':
    app.run(debug=True)