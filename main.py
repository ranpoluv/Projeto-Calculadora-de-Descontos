from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    discount_amount = None
    final_price = None

    if request.method == 'POST':
        try:
            # Obtém os valores do formulário
            original_price = float(request.form['original_price'])
            discount_percentage = float(request.form['discount_percentage'])

            # Calcula o valor do desconto e o preço final
            discount_amount = (original_price * discount_percentage) / 100
            final_price = original_price - discount_amount
        except ValueError:
            # Se os dados forem inválidos
            discount_amount = "Invalid input. Please enter numerical values."

    # Renderiza o template com os valores calculados
    return render_template('index.html', discount_amount=discount_amount, final_price=final_price)

if __name__ == '__main__':
    # Inicia o servidor Flask
    app.run(debug=True, host='0.0.0.0')