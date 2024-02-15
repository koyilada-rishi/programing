def generate_dockerfile(war_file, tomcat_version='9.0'):
    dockerfile_content = f'''
    # Use Tomcat as the base image
    FROM tomcat:{tomcat_version}

    # Remove the default Tomcat webapps
    RUN rm -rf /usr/local/tomcat/webapps/*

    # Copy the WAR file into the webapps directory
    COPY {war_file} /usr/local/tomcat/webapps/

    # Expose port 8080
    EXPOSE 8080

    # Start Tomcat
    CMD ["catalina.sh", "run"]
    '''

    with open('Dockerfile', 'w') as dockerfile:
        dockerfile.write(dockerfile_content)

    print("Dockerfile generated successfully!")

# Example usage
generate_dockerfile('your_war_file.war')
