#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!pip install streamlit


# In[2]:





# In[4]:


import streamlit as st

def sumar(x,y):
    return x+y

def main():
    st.title("Interfaz de Mi Función Específica")

    # Entrada de datos
    input1 = st.number_input("Ingrese el primer número:")
    input2 = st.number_input("Ingrese el segundo número:")

    # Botón para ejecutar la función
    if st.button("Ejecutar"):
        # Llama a la función y obtén el resultado
        resultado = sumar(input1, input2)

        # Muestra el resultado
        st.write("El resultado es:", resultado)

if __name__ == "__main__":
    main()

