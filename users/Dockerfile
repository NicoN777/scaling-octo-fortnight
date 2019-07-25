FROM openjdk:8-jdk-alpine
COPY . /javaapp
WORKDIR /javaapp
ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-jar","api-0.0.1-SNAPSHOT.jar"]
