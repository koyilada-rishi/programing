
    # Use Tomcat as the base image
    FROM tomcat:9.0

    # Remove the default Tomcat webapps
    RUN rm -rf /usr/local/tomcat/webapps/*

    # Copy the WAR file into the webapps directory
    COPY your_war_file.war /usr/local/tomcat/webapps/

    # Expose port 8080
    EXPOSE 8080

    # Start Tomcat
    CMD ["catalina.sh", "run"]
    