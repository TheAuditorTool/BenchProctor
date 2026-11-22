FROM alpine:3.24.2@sha256:294b683cb724975bec92580e1e685676bd4b50bda910ddb8c51d4cabeaec77e6 AS build
WORKDIR /src
RUN apk add --no-cache build-base curl-dev rabbitmq-c-dev sqlite-dev
COPY . .
RUN make

FROM alpine:3.24.2@sha256:294b683cb724975bec92580e1e685676bd4b50bda910ddb8c51d4cabeaec77e6
RUN apk add --no-cache libstdc++ libcurl rabbitmq-c sqlite-libs
WORKDIR /app
COPY --from=build /src/audit_append /app/audit_append
RUN mkdir -p /var/app && chown 1000:1000 /var/app
USER 1000:1000
CMD ["/app/audit_append"]
