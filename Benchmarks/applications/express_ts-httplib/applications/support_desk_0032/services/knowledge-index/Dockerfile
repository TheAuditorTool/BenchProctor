FROM alpine:3.20 AS build
WORKDIR /src
RUN apk add --no-cache build-base
COPY . .
RUN make

FROM alpine:3.20
RUN apk add --no-cache libstdc++
WORKDIR /app
COPY --from=build /src/knowledge_search /app/knowledge_search
USER 1000:1000
CMD ["/app/knowledge_search"]
