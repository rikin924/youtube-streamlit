import streamlit as st
import time

st.title("Streamlit 超超入門")

st.write("Display Image")

"Start!!"

latest_iteration = st.empty()
bar = st.progress(0)

for  i in range(100):
    latest_iteration.text(f"Iteration{i+1}")
    bar.progress(i+1)
    time.sleep(0.1)

"ホームページへようこそ"

left_column, senter_column,right_column = st.beta_columns(3)
button = left_column.button("りき。の")

if button:
    senter_column.button("世界に")
if senter_column.button:
    right_column.write("ようこそ！！！！")

expander = st.beta_expander("私は誰でしょう？")
expander.write("りんです")
expander = st.beta_expander("何人でしょう？")
expander.write("日本人でっす")
expander = st.beta_expander("どこに住んでますか？")
expander.write("神奈川")


#option = st.text_input("あなたの好きな趣味は？？")
#condition = st.slider("あんたの調子は？", 0, 100, 70)


#"コンディション：" , condition , "なんだな"
#"あんたの趣味は" ,option, "なんだな"

#"あんたの好きな数字は", option, "です。"
#if st.checkbox("Show Image"):
 #   img = Image.open("OneDrive/画像/牛.jpg")
  #  st.image(img, caption="ウシ", use_column_width=True)
