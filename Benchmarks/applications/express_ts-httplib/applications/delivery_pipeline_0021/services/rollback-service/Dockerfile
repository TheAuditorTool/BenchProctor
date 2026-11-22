FROM alpine:3.24.2@sha256:294b683cb724975bec92580e1e685676bd4b50bda910ddb8c51d4cabeaec77e6 AS build
WORKDIR /src
RUN apk add --no-cache build-base curl-dev rabbitmq-c-dev
COPY . .
RUN make

FROM alpine:3.24.2@sha256:294b683cb724975bec92580e1e685676bd4b50bda910ddb8c51d4cabeaec77e6
RUN apk add --no-cache libstdc++ libcurl rabbitmq-c
WORKDIR /app
COPY --from=build /src/rollback_trigger /app/rollback_trigger
USER 1000:1000
CMD ["/app/rollback_trigger"]
