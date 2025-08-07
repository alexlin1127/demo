# 使用官方 Python 基礎映像
FROM python:3.12

# 設定工作目錄
WORKDIR /app

# 設定環境變數
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DEBIAN_FRONTEND=noninteractive

# 安裝系統依賴
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# 複製並安裝 Python 依賴
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 複製專案檔案
COPY . .

# 收集靜態檔案
# RUN python manage.py collectstatic --noinput

# # 建立非 root 使用者
# RUN useradd --create-home --shell /bin/bash app \
#     && chown -R app:app /app
# USER app

# 暴露端口
EXPOSE 8000

CMD ["python", "manage.py", "runserver:0.0.0.0"]