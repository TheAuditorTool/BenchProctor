FROM maven:3.9.16-eclipse-temurin-11@sha256:7bb84a451705605a47d24eb844d4d9ab03e33e131a507db76aafe25db3907f64 AS build
WORKDIR /src
COPY pom.xml ./
COPY src ./src
RUN mvn -o -C -q -DskipTests package || mvn -C -q -DskipTests package

FROM eclipse-temurin:11.0.32_9-jre-alpine-3.24@sha256:3dd6fc91717988cad5faf27a4ce9ed608386bb3c340f912f122d8bdcc2857ddb
WORKDIR /app
COPY --from=build /src/target/screening-service-1.0.0.jar /app/service.jar
USER 1000:1000
CMD ["java", "-jar", "/app/service.jar"]
