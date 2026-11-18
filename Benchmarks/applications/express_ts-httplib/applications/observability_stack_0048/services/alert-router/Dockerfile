FROM alpine:3.20 AS build
WORKDIR /src
RUN apk add --no-cache build-base curl-dev libpq-dev sqlite-dev
COPY . .
RUN make

FROM alpine:3.20
RUN apk add --no-cache libstdc++ libcurl libpq sqlite-libs
WORKDIR /app
COPY --from=build /src/alert_route /app/alert_route
RUN mkdir -p /var/app && chown 1000:1000 /var/app
USER 1000:1000
CMD ["/app/alert_route"]
