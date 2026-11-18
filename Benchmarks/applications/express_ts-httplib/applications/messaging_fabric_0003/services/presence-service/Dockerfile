FROM alpine:3.20 AS build
WORKDIR /src
RUN apk add --no-cache build-base hiredis-dev sqlite-dev
COPY . .
RUN make

FROM alpine:3.20
RUN apk add --no-cache libstdc++ hiredis sqlite-libs
WORKDIR /app
COPY --from=build /src/presence_update /app/presence_update
RUN mkdir -p /var/app && chown 1000:1000 /var/app
USER 1000:1000
CMD ["/app/presence_update"]
