FROM maven:3.9-eclipse-temurin-21 AS build
WORKDIR /src
COPY pom.xml ./
COPY src ./src
RUN mvn -o -q -DskipTests package || mvn -q -DskipTests package

FROM eclipse-temurin:21-jre-alpine
WORKDIR /app
COPY --from=build /src/target/consent-registry-1.0.0.jar /app/service.jar
USER 1000:1000
CMD ["java", "-jar", "/app/service.jar"]
