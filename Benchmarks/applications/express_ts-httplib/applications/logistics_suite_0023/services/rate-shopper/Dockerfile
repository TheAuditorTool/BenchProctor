FROM alpine:3.20 AS build
WORKDIR /src
RUN apk add --no-cache build-base
COPY . .
RUN make

FROM alpine:3.20
RUN apk add --no-cache libstdc++
WORKDIR /app
COPY --from=build /src/rate_shop /app/rate_shop
USER 1000:1000
CMD ["/app/rate_shop"]
