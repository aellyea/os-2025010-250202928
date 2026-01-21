FROM gcc:12

WORKDIR /app

COPY app.cpp .

RUN g++ app.cpp -o app

CMD ["./app"]
