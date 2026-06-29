from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sabor Express | Restaurante</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
        
        * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Poppins', sans-serif; }
        body { background-color: #f9f9f9; color: #333; }
        
        header { background-color: #ff4757; color: white; padding: 20px; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
        header h1 { font-weight: 700; font-size: 2.5rem; }
        header p { font-size: 1rem; opacity: 0.9; margin-top: 5px; }

        .container { max-width: 1200px; margin: 40px auto; padding: 0 20px; }
        .menu-title { text-align: center; margin-bottom: 30px; font-size: 2rem; color: #2f3542; }

        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 30px; }
        .card { background: white; border-radius: 15px; overflow: hidden; box-shadow: 0 10px 15px rgba(0,0,0,0.05); transition: transform 0.3s; }
        .card:hover { transform: translateY(-5px); }
        
        .card-img { height: 200px; background-size: cover; background-position: center; }
        .img-burger { background-image: url('https://images.unsplash.com/photo-1568901346375-23c9450c58cd?q=80&w=500'); }
        .img-pizza { background-image: url('https://images.unsplash.com/photo-1513104890138-7c749659a591?q=80&w=500'); }
        .img-papas { background-image: url('https://images.unsplash.com/photo-1573080496219-bb080dd4f877?q=80&w=500'); }

        .card-body { padding: 20px; }
        .card-body h3 { font-size: 1.3rem; margin-bottom: 10px; color: #2f3542; }
        .card-body p { color: #747d8c; font-size: 0.9rem; margin-bottom: 15px; line-height: 1.4; }
        .price { font-weight: 700; color: #ff4757; font-size: 1.2rem; }

        footer { text-align: center; padding: 30px; background: #2f3542; color: white; margin-top: 60px; font-size: 0.9rem; }
    </style>
</head>
<body>

    <header>
        <h1>🍔 SABOR EXPRESS 🍕</h1>
        <p>¡La mejor comida rápida directo a tu pantalla!</p>
    </header>

    <div class="container">
        <h2 class="menu-title">Nuestro Menú Destacado</h2>
        
        <div class="grid">
            <div class="card">
                <div class="card-img img-burger"></div>
                <div class="card-body">
                    <h3>Hamburguesa Monster</h3>
                    <p>Carne de res premium, queso cheddar derretido, tocino crujiente y salsa de la casa.</p>
                    <span class="price">$5.99</span>
                </div>
            </div>

            <div class="card">
                <div class="card-img img-pizza"></div>
                <div class="card-body">
                    <h3>Pizza Pepperoni Suprema</h3>
                    <p>Masa artesanal delgada, salsa de tomate premium, abundante queso mozzarella y pepperoni.</p>
                    <span class="price">$8.50</span>
                </div>
            </div>

            <div class="card">
                <div class="card-img img-papas"></div>
                <div class="card-body">
                    <h3>Papas rústicas con Queso</h3>
                    <p>Papas cortadas a mano, sazonadas con especias finas y bañadas en salsa de queso caliente.</p>
                    <span class="price">$3.25</span>
                </div>
            </div>
        </div>
    </div>

    <footer>
        <p>&copy; 2026 Sabor Express - Todos los derechos reservados.</p>
    </footer>

</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)