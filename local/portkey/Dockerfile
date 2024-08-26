FROM portkeyai/gateway:latest

WORKDIR /app

RUN npm install undici@latest

COPY load-patch.js /app/load-patch.js

ENTRYPOINT ["node"]

CMD ["--eval", "import('/app/load-patch.js').then(() => import('/app/build/start-server.js'))"]
