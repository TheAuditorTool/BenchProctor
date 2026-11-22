FROM maven:3.9.16-eclipse-temurin-25@sha256:93b8a14ea2f412782e4e842651273b4d903e35cc496284f178fbbe2d67d00976 AS build
WORKDIR /src
COPY pom.xml ./
COPY src ./src
RUN mvn -o -C -q -DskipTests package || mvn -C -q -DskipTests package

FROM eclipse-temurin:25.0.4_7-jre-alpine-3.24@sha256:2ca9adf44f5c29d28ecd26cf92d75cc0c66b7f32bfd839a4439e363a8b428af8
WORKDIR /app
COPY --from=build /src/target/payout-service-1.0.0.jar /app/service.jar
USER 1000:1000
CMD ["java", "-jar", "/app/service.jar"]
