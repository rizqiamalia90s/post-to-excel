from flask import Flask, render_template, request, jsonify
import pandas as pd
import os

app = Flask(__name__, template_folder='views')

EXCEL_FILE = os.path.join('assets', 'data_nilai.xlsx')

def load_excel():
    if os.path.exists(EXCEL_FILE):
        return pd.read_excel(EXCEL_FILE)
    df = pd.DataFrame(columns=['nama', 'nilai'])
    os.makedirs('assets', exist_ok=True)
    df.to_excel(EXCEL_FILE, index=False)
    return df

def save_excel(df):
    os.makedirs('assets', exist_ok=True)
    df.to_excel(EXCEL_FILE, index=False)

@app.route('/nilai')
def nilai():
    return render_template('nilaiView.html')

@app.route('/get_data')
def get_data():
    df = load_excel()
    return jsonify(df.to_dict('records'))

@app.route('/save_data', methods=['POST'])
def save_data():
    data = request.json
    df = load_excel()
    new_data = pd.DataFrame(data)
    df = pd.concat([df, new_data], ignore_index=True)
    save_excel(df)
    return jsonify({"message": "Data berhasil disimpan"})

@app.route('/update_data', methods=['POST'])
def update_data():
    data = request.json
    index = data['index']
    new_data = data['data']
    
    df = load_excel()
    if 0 <= index < len(df):
        df.loc[index] = new_data
        save_excel(df)
        return jsonify({"message": "Data berhasil diupdate"})
    return jsonify({"message": "Index tidak valid"}), 400

@app.route('/delete_data', methods=['POST'])
def delete_data():
    data = request.json
    index = data['index']
    
    df = load_excel()
    if 0 <= index < len(df):
        df = df.drop(index)
        df = df.reset_index(drop=True)
        save_excel(df)
        return jsonify({"message": "Data berhasil dihapus"})
    return jsonify({"message": "Index tidak valid"}), 400

if __name__ == '__main__':
    app.run(debug=True)
