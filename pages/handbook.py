import streamlit as st

with st.expander("class1筆記"):
    st.write(
        """

---

## 🧠 1. 註解：寫給人看的說明，不會被電腦執行

* `#` 是單行註解，用來寫簡單說明。
* `"""
        """` 是多行註解，可以一次寫好幾行。

---

## 📢 2. print：顯示在畫面上的指令

```python
print("Hello, World!")
```

會把 `"Hello, World!"` 這段文字顯示出來。

---

## 🔢 3. 基本資料種類（型態）

* `int`：整數（例如：1、2、100）
* `float`：小數（例如：1.0、3.14）
* `str`：字串，也就是文字（例如："apple"）
* `bool`：布林值，只有 `True`（對）或 `False`（錯）

---

## 📦 4. 變數：幫資料取個名字

```python
a = 10
print(a)
a = "apple"
print(a)
```

用 `=` 把資料存在一個「名字」裡，方便之後使用。

---

## ➕ 5. 運算符：加減乘除

* `+` 加法
* `-` 減法
* `*` 乘法
* `/` 除法（有小數）
* `//` 除法（只取整數的部分）
* `%` 取餘數（例如 7 % 3 = 1）
* `**` 次方（例如 2\*\*3 = 8）

📌 運算的順序：

1. 先算括號 `()`
2. 次方 `**`
3. 乘、除、取整數除法、取餘數
4. 最後才是加減

---

## 🧵 6. 字串的玩法

```python
print("apple" + " pen")  # 變成 "apple pen"
print("apple " * 3)      # 變成 "apple apple apple "
```

* `+` 可以把字串接在一起。
* `*` 可以把字串重複好幾次。

---

## 📏 7. 特別的函式（功能）

* `len()`：看字串有多長
  → `len("apple")` 會顯示 `5`
* `type()`：看資料是哪一種型態
  → `type(1)` 顯示 `<class 'int'>`

---

## 🔄 8. 型態轉換（改變資料的種類）

```python
int(1.0)      # 變成整數 → 1
float(1)      # 變成小數 → 1.0
str(1)        # 變成字串 → "1"
bool(1.234)   # 變成布林值 → True
```

🔔 注意：如果字串裡面不是數字，像是 `"hello"`，就不能轉成數字，會出錯！

---

## ⌨️ 9. input：讓使用者輸入資料

```python
a = input("請輸入一些文字:")
print(a)
```

* `input()` 會讓使用者輸入東西。
* `a` 裡會裝著使用者輸入的內容。
* 這個內容一開始**都是字串**，要自己用 `int()` 轉成數字。

---

## 🧮 10. 計算範例：圓面積 & 平均成績

```python
a = int(input("請輸入半徑:"))
print(a * a * 3.14)
```

這是算圓面積（π ≈ 3.14）。

```python
b = int(input("請輸入期中成績:"))
c = int(input("請輸入期末成績:"))
print("平均成績:", (b + c) / 2)
```

這是算平均成績。

---

## 📝 11. f-string：字串裡放變數

```python
name = "apple"
age = 18
print(f"hello, my name is {name}, and I'm {age} years old.")
```

用 `f"..."` 可以在字串中間放變數，非常方便！

---

如果你需要我幫你畫圖、做筆記或變成遊戲小練習再學一次也可以喔！😄


"""
    )

with st.expander("class2筆記"):
    st.write(
        """
好的！以下是你今天上課學到的 Python 指令內容，我幫你用**國小六年級**可以懂的方式整理成簡單又清楚的筆記 📚👇

---

## 🟡 1. 比較運算子：比大小、看是不是一樣

這些是用來「比較兩個東西」的：

| 符號   | 意思    | 範例       | 結果      |
| ---- | ----- | -------- | ------- |
| `==` | 是否相等  | `1 == 1` | `True`  |
| `!=` | 是否不相等 | `1 != 1` | `False` |
| `<`  | 小於    | `1 < 1`  | `False` |
| `>`  | 大於    | `1 > 1`  | `False` |
| `<=` | 小於或等於 | `1 <= 1` | `True`  |
| `>=` | 大於或等於 | `1 >= 1` | `True`  |

🧠 結果只會是 `True`（對）或 `False`（錯）

---

## 🟢 2. 邏輯運算子：判斷多個條件的真假

這些是用來「組合條件」的：

### `and`：**兩個都要對，才會是對**

```python
True and True     # True
True and False    # False
```

### `or`：**只要一個對，就是對**

```python
True or False     # True
False or False    # False
```

### `not`：**相反的意思**

```python
not True          # False
not False         # True
```

---

## 🔢 3. 運算的優先順序（誰先算）

運算時會照這個順序來決定誰先算：

1. 括號 `()` 最優先
2. 次方 `**`
3. 乘、除、取商、取餘數：`*` `/` `//` `%`
4. 加減 `+` `-`
5. 比較：`==` `!=` `<` `>` `<=` `>=`
6. `not`
7. `and`
8. `or` 最後才算

📌 如果不確定，可以用括號包起來，讓它先算！

---

## 🔒 4. 密碼門程式：用 if 判斷條件

```python
password = input("請輸入密碼：")
if password == "1234":
    print("歡迎pauline")
elif password == "5678":
    print("歡迎john")
elif password == "0000":
    print("歡迎patrick")
else:
    print("密碼錯誤")
```

🔑 `if` 是「如果」，`elif` 是「不然如果」，`else` 是「其他情況」。

🧠 **`elif` 會跳過已經判斷過的條件，效率比較好！**
但如果用好幾個 `if`，每一個都會判斷一次，比較慢。

---

## 🧮 5. 成績計算練習

```python
b = int(input("請輸入國文期中成績:"))
c = int(input("請輸入國文期末成績:"))
print("國文平均成績:", (b + c) / 2)
```

* `input()` 讓使用者輸入數字
* `int()` 把輸入的內容變成整數
* `(b + c) / 2` 是兩次成績的平均分數

---

## ✉️ 6. 字串格式化：f-string

```python
name = "apple"
age = 18
print(f"hello, my name is {name}, and I'm {age} years old.")
```

💡 用 `f"..."` 可以把變數放進字串裡，會自動變成完整的句子！

---

### 🎉 總結

| 學到什麼？        | 功能             |
| ------------ | -------------- |
| 比較運算子        | 判斷兩個東西的大小或是否一樣 |
| 邏輯運算子        | 多個條件一起判斷       |
| if elif else | 根據不同情況執行不同事情   |
| 優先順序         | 決定先算誰後算誰       |
| f-string     | 字串中插入變數        |

---

如果你想，我也可以幫你把這些整理成圖解、筆記、或者小練習題喔！要嗎？😄

"""
    )

with st.expander("class3筆記"):
    st.write(
        """
太好了！你學了很多 Python 的基礎知識呢～
我幫你把這些內容整理成適合國小四五年級看的簡單說明，讓你更容易看懂，也可以用來複習：

---

### 🧺 **一、List 是什麼？**

List 就像是一個**裝東西的盒子**，可以放很多東西，而且順序不會亂。

```python
print([])  # 空的盒子
print([1, 2, 3])  # 放了三個數字
print([1, 2, 3, "a", "b", "c"])  # 數字跟文字都可以放
print([1, 2, 3, ["a", "b", "c"]])  # 還可以放一個小盒子（list 裡面又有 list）
print([1, True, "a", 1.23])  # 不同種類的東西也能放一起
```

---

### 🔍 **二、怎麼拿出盒子裡的東西？**

盒子裡的東西會有編號，從 **0 開始** 數：

```python
L = [1, 2, 3, "a", "b", "c"]
print(L[0])  # 1
print(L[3])  # "a"
```

也可以一次拿很多：

```python
print(L[::2])  # 每隔一個拿一次： [1, 3, 'b']
print(L[1:4])  # 拿第1到第3個（不含第4個）：[2, 3, 'a']
print(L[1:4:2])  # 從第1到第3個，每隔一個拿一次：[2, 'a']
```

---

### 🔢 **三、看 list 有幾個東西**

```python
print(len(L))  # 6
```

---

### 🔁 **四、用 for 迴圈走過 list 的每一個東西**

```python
for i in range(0, len(L), 2):  # 每隔一個拿
    print(L[i])

for i in L:  # 一個一個拿
    print(i)
```

---

### 🧪 **五、變數的複製方式**

* 叫做「值的複製」（call by value）時，**a 變了 b 不會變**。
* 叫做「記憶體位置一樣」（call by reference）時，**a 變了 b 也會變**。

```python
a = 1
b = a
b = 2
print(a, b)  # a 還是 1

a = [1, 2, 3]
b = a
b[0] = 2
print(a)  # a 跟 b 都變了！

a = [1, 2, 3]
b = a.copy()
b[0] = 2
print(a)  # a 不會被改到
```

---

### ➕ ➖ **六、加東西跟刪東西**

```python
L = [1, 2, 3]
L.append(4)  # 加在最後
print(L)

L = ["a", "b", "c", "d", "a"]
L.remove("a")  # 刪掉第一個"a"
L.pop(0)  # 刪掉第0個
L.pop()  # 刪掉最後一個
```

---

### 📊 **七、成績平均**

```python
midterm = [80, 95, 78, 60, 55]
final = [64, 73, 52, 34, 95]
avg = (midterm[1] + final[1]) / 2
print(avg)
```

---

### 👥 **八、名單＋號碼**

```python
name = ["Amy", "Mandy", "Peter"]
index = 1
for i in name:
    print(f"{index}號是{i}")
    index += 1
```

---

### 🌐 **九、Streamlit（做網頁的小工具）**

```python
import streamlit as st

# 顯示數字輸入框
number = st.number_input("請輸入一個分數", step=1, min_value=0, max_value=100)

# 顯示分數的等級
if number >= 90:
    st.markdown("A")
elif number >= 80:
    st.markdown("B")
# 依此類推...
```

#### 按鈕效果：

```python
if st.button("點我"):
    st.balloons()  # 放氣球
    st.snow()  # 下雪
```

#### 數字金字塔：

```python
number = st.number_input("請輸入一個數字(1到9)", step=1, min_value=1, max_value=9)
for i in range(1, number + 1):
    st.write(str(i) * i)
```

---

### 🎯 **十、for 迴圈和 range 的用法**

```python
for i in range(5):  # 0~4
    print(i)

for i in range(1, 5):  # 1~4
    print(i)

for i in range(1, 10, 2):  # 1~9，跳兩格
    print(i)
```

---

如果你想，我也可以幫你做成小小的學習筆記（PDF 或 Word），你可以帶去學校或放在電腦裡練習喔！需要的話再告訴我 😊

"""
    )
