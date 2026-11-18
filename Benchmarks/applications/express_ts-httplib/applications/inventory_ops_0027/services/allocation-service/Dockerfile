FROM alpine:3.20 AS build
WORKDIR /src
RUN apk add --no-cache build-base curl-dev sqlite-dev
COPY . .
RUN make

FROM alpine:3.20
RUN apk add --no-cache libstdc++ libcurl sqlite-libs
WORKDIR /app
COPY --from=build /src/allocation_solve /app/allocation_solve
RUN mkdir -p /var/app && chown 1000:1000 /var/app
USER 1000:1000
CMD ["/app/allocation_solve"]
