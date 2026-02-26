# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 15:58:18 2026

@author: BusRmutt
"""

import pickle
from streamlit_option_menu import option_menu
import streamlit as st

used_car_model = pickle.load(open('Used_cars_model.sav','rb'))
riding_model = pickle.load(open('RidingMowers_model.sav','rb'))
bmi_model = pickle.load(open('bmi_model.sav','rb'))


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
with st.sidebar:
    selected = option_menu('Prediction',
                           ['Ridingmower','Used_cars','bmi'])

if selected== 'Ridingmower':
    st.title('Riding Mower Classification')
    
    Income = st.text_input('Income')
    LotSize = st.text_input('LotSize')
    Riding_prediction = ''
    if st.button('Predict'):
        Riding_prediction = riding_model.predict([[
            float(Income),
            float(LotSize)
            ]])
        if Riding_prediction[0]==1:
            Riding_prediction = 'Owner'
        else:
            Riding_prediction = 'Non Owner'
    st.success(Riding_prediction)
    
if selected == 'Used_cars':
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
    
if selected == 'bmi':
    st.title('ประเมิน BMI')
    
    # 1. สร้างตัวเลือกสำหรับเพศ (0 หรือ 1 ตามข้อมูลในตาราง)
    gender_input = st.selectbox('เพศ', ['หญิง', 'ชาย'])
    gender_val = 1 if gender_input == 'ชาย' else 0
    
    # 2. รับค่าส่วนสูงและน้ำหนัก
    height_val = st.text_input('ส่วนสูง (cm)')
    weight_val = st.text_input('น้ำหนัก (kg)')
    
    bmi_prediction_result = ''
    
    if st.button('Predict'):
        # ตรวจสอบว่ากรอกข้อมูลครบถ้วนหรือไม่
        if height_val and weight_val:
            # 3. ใช้ bmi_model ในการทำนาย
            # ส่งค่า [Gender, Height, Weight] ตามลำดับในรูปภาพข้อมูลของคุณ
            prediction = bmi_model.predict([[
                float(gender_val),
                float(height_val),
                float(weight_val)
            ]])
            
            # 4. แปลงผลลัพธ์ที่เป็นตัวเลข (Index) ให้เป็นคำอ่าน (อ้างอิงตามเกณฑ์มาตรฐาน)
            bmi_index = prediction[0]
            bmi_labels = {
                0: 'Extremely Weak (ผอมมาก)',
                1: 'Weak (ผอม)',
                2: 'Normal (ปกติ)',
                3: 'Overweight (น้ำหนักเกิน)',
                4: 'Obesity (อ้วน)',
                5: 'Extreme Obesity (อ้วนอันตราย)'
            }
            
            bmi_prediction_result = bmi_labels.get(bmi_index, f'Index: {bmi_index}')
            st.success(f'ผลการประเมิน: {bmi_prediction_result}')
        else:
            st.error('กรุณากรอกข้อมูลให้ครบถ้วน')
