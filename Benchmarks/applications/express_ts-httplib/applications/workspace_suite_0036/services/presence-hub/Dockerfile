FROM alpine:3.20 AS build
WORKDIR /src
RUN apk add --no-cache build-base curl-dev
COPY . .
RUN make

FROM alpine:3.20
RUN apk add --no-cache libstdc++ libcurl
WORKDIR /app
COPY --from=build /src/presence_track /app/presence_track
USER 1000:1000
CMD ["/app/presence_track"]
