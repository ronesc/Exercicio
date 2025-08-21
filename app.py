# -*- coding: utf-8 -*-
import requests

response = requests.get("https://api.frankfurter.app/latest")
print(response)

import streamlit as st

st.header('Jogando uma moeda')

st.write('Ainda não é um aplicativo funcional. Em construção.')

pip install streamlit