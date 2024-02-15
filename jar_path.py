def generate_dockerfile(java_version):
    app_jar = "/path/to/your/java/app.jar"  # Fixed JAR file path
    dockerfile_content = f"""
FROM openjdk:{java_version}

WORKDIR /app

COPY {app_jar} /app/

CMD ["java", "-jar", "{app_jar}"]
"""
    with open("Dockerfile", "w") as f:
        f.write(dockerfile_content)

# Example usage:
java_version = "11"
generate_dockerfile(java_version)
print("Dockerfile generated successfully.")
