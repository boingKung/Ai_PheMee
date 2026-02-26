# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 14:43:02 2026

@author: BusRmutt
"""

import pickle

import streamlit as st

used_car_model = pickle.load(open('C:/Users/BusRmutt/Desktop/ML/Used_cars_model.sav','rb'))

fuel_map = {
    'Diesel': 0,
    'Electric': 1,
    'Petrol': 2
}

engine_map = {
    '800': 0,
    '1000': 1,
    '1200': 2,
   '1500': 3,
    '1800': 4,
    '2000': 5,
    '2500': 6,
    '3000': 7,
    '4000': 8,
    '5000': 9
}

brand_map = {
    'BMW': 0,
    'Chevrolet': 1,
    'Ford': 2,
    'Honda': 3,
    'Hyundai': 4,
    'Kia': 5,
    'Nissan': 6,
    'Tesla': 7,
    'Toyota': 8,
    'Volkswagen': 9
}

transmission_map = {
    'Automatic': 0,
    'Manual': 1
}


def main():
    st.title('ประเมินราคารถมือ 2')
    make_year = st.text_input('ปีที่ผลิต')
    mileage_kmpl = st.text_input('กินน้ำมันกี่ KM/L')
    engine_cc = st.selectbox('ขนาดเครื่องยนต์ (CC)', engine_map)
    fuel_type = st.selectbox('ประเภทน้ำมัน', fuel_map)
    owner_count = st.text_input('จำนวนเจ้าของเดิม')
    brand = st.selectbox('ยี่ห้อรถ', brand_map)
    transmission = st.selectbox('ประเภทเกียร์', transmission_map)
    accidents_reported = st.text_input('จำนวนอุบัติเหตุที่เคยเกิด')
    Price_predict = ''
    if st.button('Predict'):
        Price_predict = used_car_model.predict([[
            float(make_year),
            float(mileage_kmpl),
            engine_map[engine_cc],
            fuel_map[fuel_type],
            float(owner_count),
            brand_map[brand],
            transmission_map[transmission],
            float(accidents_reported)
            ]])
        Price_predict = round(Price_predict[0],2)
    st.success(Price_predict)
if __name__=="__main__":
    main()