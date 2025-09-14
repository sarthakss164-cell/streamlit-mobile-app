import streamlit as st

st.title(" MOBILE STORE")
count = st.number_input("HOW MANY MOBILES DO YOU HAVE?",min_value=1,step=1)
mobile = []
price = []

for i in range(count):
    phone = st.text_input(f"name of mobile{i+1}",key= f"moblile_{i}")
    money = st.number_input(f"price of mobile{mobile}",min_value=0.0,step=1.0,key=f"price{i}")
    mobile.append(phone)
    price.append(money)
    

if st.button("calculate"):
   total = sum(price)
   max_price =max(price)
   min_price =min(price)
   max_mobile = mobile[price.index(max_price)]
   min_mobile = mobile[price.index(min_price)]
   total= sum(price)

   st.success(f"total price: rs{total}")
   st.info ( f"most expensive mobile : {max_mobile} - rs{max_price}")
   st.info (f"most cheap mobile : {min_mobile} - {min_price}")

   st.markdown("### 🧾 Item List:")
   for mobile, price in zip(mobile, price):
        st.write(f"- {mobile}: ₹{price}")