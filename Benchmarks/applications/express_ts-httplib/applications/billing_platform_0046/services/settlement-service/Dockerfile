FROM alpine:3.20 AS build
WORKDIR /src
RUN apk add --no-cache build-base libpq-dev sqlite-dev
COPY . .
RUN make

FROM alpine:3.20
RUN apk add --no-cache libstdc++ libpq sqlite-libs
WORKDIR /app
COPY --from=build /src/settlement_batch /app/settlement_batch
RUN mkdir -p /var/app && chown 1000:1000 /var/app
USER 1000:1000
CMD ["/app/settlement_batch"]
