FROM alpine:3.20 AS build
WORKDIR /src
RUN apk add --no-cache build-base curl-dev
COPY . .
RUN make

FROM alpine:3.20
RUN apk add --no-cache libstdc++ libcurl
WORKDIR /app
COPY --from=build /src/anomaly_score /app/anomaly_score
USER 1000:1000
CMD ["/app/anomaly_score"]
