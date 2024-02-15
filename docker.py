def generate_dockerfile(base_image, packages):
    dockerfile_content = f"FROM {base_image}\n"
    
    if packages:
        dockerfile_content += "RUN apt-get update && apt-get install -y \\\n"
        dockerfile_content += " \\\n".join(packages)
        dockerfile_content += "\n"
    
    with open("Dockerfile", "w") as f:
        f.write(dockerfile_content)

# Example usage:
base_image = "ubuntu:latest"
packages = ["python3", "python3-pip", "git"]
generate_dockerfile(base_image, packages)
print("Dockerfile generated successfully.")
