FROM alpine:3.20 AS build
WORKDIR /src
RUN apk add --no-cache build-base curl-dev libpq-dev
COPY . .
RUN make

FROM alpine:3.20
RUN apk add --no-cache libstdc++ libcurl libpq
WORKDIR /app
COPY --from=build /src/thumbnail_render /app/thumbnail_render
USER 1000:1000
CMD ["/app/thumbnail_render"]
