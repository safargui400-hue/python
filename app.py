from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def dashboard():
    kpis = {
        'stock': 120,
        'produits': 250,
        'rupture': 5,
        'clients': 120,
    }

    products = [
        {'name': 'Riz 50kg', 'achat': 20000, 'vente': 22000, 'stock': 10},
        {'name': 'Huile 1L', 'achat': 1000, 'vente': 1300, 'stock': 3},
        {'name': 'Sucre 1kg', 'achat': 2000, 'vente': 3000, 'stock': 2},
        {'name': 'Pâtes 500g', 'achat': 1600, 'vente': 2000, 'stock': 1},
    ]
    return render_template('dashboard.html', kpis=kpis, products=products)


@app.route('/produits')
def produits():
    data = [
        {'name': 'Riz 50kg', 'achat': 20000, 'vente': 22000, 'stock': 2, 'client': 'Mamadou'},
        {'name': 'Huile 1L', 'achat': 1000, 'vente': 1300, 'stock': 3, 'client': 'Aminata'},
        {'name': 'Sucre 1kg', 'achat': 2000, 'vente': 3000, 'stock': 2, 'client': 'Fatou'},
        {'name': 'Pâtes 500g', 'achat': 1600, 'vente': 2000, 'stock': 1, 'client': 'Moussa'},
    ]
    return render_template('produits.html', products=data)


@app.route('/ventes')
def ventes():
    cards = {
        'ventes_total': '3.4M F CFA',
        'benefices_total': '1.1M F CFA',
        'produit_rentable': 'Riz 50kg',
        'clients_fideles': ['Mamadou', 'Aminata', 'Fatou'],
    }
    return render_template('ventes.html', cards=cards)


@app.route('/rapport')
def rapport():
    return render_template('rapport.html')


if __name__ == '__main__':
    app.run(debug=True)
