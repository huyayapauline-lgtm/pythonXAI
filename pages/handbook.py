import streamlit as st
import os

folder_path = "markdown"  # 設資料夾路徑
files = os.listdir(folder_path)  # 取得資料夾中的所有檔案
# 這時候資料夾可能包含其他檔案，我們只需要.md檔案
files_name = []  # 新增清單用來存放
for f in files:  # 逐一檢查所有檔案,看看是否以.md結尾
    if f.endswith(".md"):  # 如果檔案名稱以.md結尾
        # if".md" in f:  # 如果檔案名稱中包含.md
        files_name.append(f)  # 將檔案名稱加入清單
files_name.sort()  # 將檔案名稱排序,預設是由小到大

for f in files_name:  # ['class1.md', 'class2.md']逐一讀取所有.md檔案
    # 用with open()讀取檔案內容並存到file變數裡面,模式為r,檔案編碼為utf-8`
    # 這樣可以不用擔心檔案讀取後忘記關閉檔案
    # open參數格式為(檔案路徑, 模式, 編碼)
    # markdown\class3.md
    with open(os.path.join(folder_path, f), "r", encoding="utf-8") as file:
        content = file.read()  # 讀取檔案內容
    with st.expander(f[:-3]):  # 使用expander,標題為檔案名稱去掉.md
        st.markdown(content)  # 將檔案內容顯示在網頁上
