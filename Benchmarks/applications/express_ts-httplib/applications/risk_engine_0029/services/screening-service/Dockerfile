FROM alpine:3.20 AS build
WORKDIR /src
RUN apk add --no-cache build-base sqlite-dev
COPY . .
RUN make

FROM alpine:3.20
RUN apk add --no-cache libstdc++ sqlite-libs
WORKDIR /app
COPY --from=build /src/screening_run /app/screening_run
RUN mkdir -p /var/app && chown 1000:1000 /var/app
USER 1000:1000
CMD ["/app/screening_run"]
