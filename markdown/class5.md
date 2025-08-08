我幫你把今天學到的東西整理成「國小四五年級」能懂的版本，重點簡單明瞭，還加一點小例子讓你更好記。

---

## 🗂 字典（dict）

- **像資料櫃一樣**，一格格有「名字」(key) 和 「內容」(value)。
- **key** 不能重複（像抽屜的標籤），但 **value** 可以重複。
- **key** 只能用「不會變的東西」當名字（數字、文字）。
- **value** 可以是任何東西（數字、文字、list、dict…）。
- 不能用像 list 那樣的「位置號碼」取值，只能用 key。

```python
d = {"蘋果": 3, "香蕉": 5}
print(d["蘋果"])  # 3
```

**常用功能：**

- `d.keys()` → 取得所有 key
- `d.values()` → 取得所有 value
- `d.items()` → 取得所有「key + value」組合
- `d["新水果"] = 數量` → 新增或修改
- `d.pop("水果名", "找不到")` → 刪除，找不到時回傳預設文字

---

## 🛠 函數（function）

- **像積木**，把一段會重複用的程式收進一個名字裡，要用的時候直接呼叫。
- 用 `def` 開頭，後面接名字和括號，再加冒號。
- 小括號裡可以放「參數」→ 進來的資料。

### 1. 沒有參數

```python
def hello():
    print("哈囉！")

hello()  # 哈囉！
```

### 2. 有參數

```python
def hello(name):
    print(f"哈囉，{name}！")

hello("小明")  # 哈囉，小明！
```

### 3. 有回傳值（return）

```python
def add(a, b):
    return a + b

sum = add(3, 4)  # sum = 7
```

### 4. 多個回傳值

```python
def add_sub(a, b):
    return a + b, a - b

sum, sub = add_sub(5, 3)  # sum=8, sub=2
```

### 5. 預設參數

```python
def hello(name, msg="哈囉"):
    print(f"{msg}，{name}！")

hello("小美")  # 哈囉，小美！
```

### 6. 限制參數型態（提示用）

```python
def add(a: int, b: int = 0) -> int:
    return a + b
```

---

## 🌏 全域變數 & 區域變數

- **全域變數**：放在函數外面，大家都看得到。
- **區域變數**：只在函數裡面有用，出去就消失。
- 如果要在函數裡改全域變數，要用 `global`。

```python
length = 5  # 全域

def calc_area():
    area = length**2  # area是區域
    print(area)

calc_area()  # 25
```

---

## 📚 巢狀字典（dict 裡面有 dict 或 list）

可以存更複雜的資料，例如成績表：

```python
grade = {
    "小明": {"國文": [90, 80, 70], "數學": [85, 75, 65]},
    "小美": {"國文": [88, 78, 68], "數學": [83, 73, 63]}
}

print(grade["小明"]["數學"][0])  # 85
```

---

## 🧮 實用小技巧

- 算平均：

```python
scores = [90, 80, 70]
avg = sum(scores) / len(scores)
```

- 迴圈搭配 dict：

```python
for name, subjects in grade.items():
    print(name, subjects)
```

---

如果你要的話，我可以幫你畫一張「字典 + 函數 + 全域/區域變數」的**彩色心智圖**，讓你看一眼就懂今天的課程內容。
你要我幫你畫嗎？
