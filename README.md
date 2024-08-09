# 圖片轉換器

## 簡介

這是一個強大的圖片批量轉換工具，可以將多個資料夾中的圖片同時轉換為指定格式。本工具利用多核心處理技術，能夠快速處理大量圖片。

## 功能特點

- 支持多個輸入資料夾
- 可指定輸出格式（如 jpg, png 等）
- 利用多核心處理，提高轉換速度
- 支持常見圖片格式的轉換
- 可打包成獨立執行檔，方便在不同環境中使用

## 系統要求

- Python 3.6+
- Linux 操作系統（其他系統可能需要調整）

## 安裝

1. 克隆此儲存庫：
   ```
   git clone https://github.com/yourusername/image_converter.git
   cd image_converter
   ```

2. 創建虛擬環境（推薦）：
   ```
   python -m venv venv
   source venv/bin/activate
   ```

3. 安裝依賴：
   ```
   pip install -r requirements.txt
   ```

## 使用方法

### 使用 Python 腳本

```
python src/main.py <輸入資料夾1> <輸入資料夾2> ... <輸出資料夾> <輸出格式>
```

例如：
```
python src/main.py input_images1 input_images2 output_images jpg
```

### 使用打包後的執行檔

```
./image_converter <輸入資料夾1> <輸入資料夾2> ... <輸出資料夾> <輸出格式>
```

例如：
```
./image_converter input_images1 input_images2 output_images jpg
```

## 打包成執行檔

要將程式打包成單一執行檔，請使用 `scripts` 目錄中的 `build.sh` 腳本：

```bash
./scripts/build.sh
```

這個腳本會自動處理打包過程，生成一個獨立的執行檔。請注意，打包過程可能需要一些時間，請耐心等待。