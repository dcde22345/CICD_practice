# 使用 Node.js 作為建置階段
FROM node:22.14 AS build

WORKDIR /app

# 複製 package.json 並安裝依賴
COPY package.json package-lock.json ./
RUN npm install

# 複製剩餘的專案文件並建置
COPY . .
RUN npm run build

# 使用 Nginx 作為最終映像
FROM nginx:alpine

# 移除預設設定並加入我們的 Nginx 設定
RUN rm -rf /usr/share/nginx/html/*
COPY --from=build /app/build /usr/share/nginx/html

# 複製 Nginx 設定檔
COPY nginx.conf /etc/nginx/conf.d/default.conf

# 指定運行的 Port
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]


