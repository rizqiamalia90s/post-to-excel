from flask import request, jsonify
import pandas as pd
import os

class NilaiController:
    @staticmethod
    def save_data():
        try:
            # Mendapatkan data dari request
            data = request.get_json()
    
            # Membuat DataFrame dari data baru
            new_df = pd.DataFrame(data)
            
            # Memastikan folder assets ada
            if not os.path.exists('assets'):
                os.makedirs('assets')
            
            file_path = os.path.join('assets', 'data_nilai.xlsx')
            
            # Cek apakah file Excel sudah ada
            if os.path.exists(file_path):
                # Baca data yang sudah ada
                existing_df = pd.read_excel(file_path)
                # Gabungkan data lama dengan data baru
                final_df = pd.concat([existing_df, new_df], ignore_index=True)
            else:
                final_df = new_df
            
            # Simpan gabungan data ke Excel
            final_df.to_excel(file_path, index=False, engine='openpyxl')
    
            return jsonify({"message": "Data berhasil ditambahkan ke assets/data_nilai.xlsx"}), 200
    
        except Exception as e:
            return jsonify({"error": str(e)}), 500
