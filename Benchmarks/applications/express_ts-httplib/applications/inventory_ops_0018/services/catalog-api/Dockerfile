FROM alpine:3.20 AS build
WORKDIR /src
RUN apk add --no-cache build-base libpq-dev
COPY . .
RUN make

FROM alpine:3.20
RUN apk add --no-cache libstdc++ libpq
WORKDIR /app
COPY --from=build /src/sku_lookup /app/sku_lookup
USER 1000:1000
CMD ["/app/sku_lookup"]
