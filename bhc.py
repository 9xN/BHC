import os
from datetime import date, datetime

def generate_config_file():
    print("    \033[38;5;204m \033[38;5;204m┌\033[38;5;204m┐\033[38;5;204m \033[38;5;204m \033[38;5;204m┬\033[38;5;204m \033[38;5;204m┬\033[38;5;204m \033[38;5;204m┌\033[38;5;204m─\033[38;5;204m┐")
    print("    \033[38;5;204m \033[38;5;204m├\033[38;5;204m┴\033[38;5;204m┐\033[38;5;205m \033[38;5;205m├\033[38;5;205m─\033[38;5;205m┤\033[38;5;205m \033[38;5;205m│\033[38;5;205m \033[38;5;205m ")
    print("    \033[38;5;205m \033[38;5;205m└\033[38;5;205m─\033[38;5;205m┘\033[38;5;206m \033[38;5;206m┴\033[38;5;206m \033[38;5;206m┴\033[38;5;206m \033[38;5;206m└\033[38;5;206m─\033[38;5;206m┘")
    print("[ By: github.com/9xN ]")
    print("----------------------")
    title = input("Enter the title: ")
    directory = ""
    # Create the filename with today's date and user title and replace spaces with dashes
    today = date.today().strftime("%Y-%m-%d")
    filename = f"{today}-{title.replace(' ', '-')}.markdown"
    filepath = os.path.join(directory, filename)
    print(f"[+] Config file generated at: {filepath}")
    tags = input("Enter tags (separated by comma and space): ").split(", ")
    headerImage = input("Would you like to add a header image? (y/n): ")
    if headerImage == "y":
        image = input("Enter the image URL or relative path (i.e: /assets/images/image.jpg): ")
        headerImage = "true"
    else:
        headerImage = "false"
        image = ""
    description = input("Enter a description: ")
    category = input("Enter the category (i.e: blog, project): ")
    if category == "project":
        projects = "true"
    else:
        projects = "false"
    star = input("Would you like to star this post? (y/n): ")
    if star == "y":
        star = "true"
    else:
        star = "false"
    # Generate the config content
    config = f'''---
title: "{title}"
layout: post
date: {datetime.now().strftime("%Y-%m-%d %H:%M")}
tag: {format_tags(tags)}
image: {image}
headerImage: {headerImage}
projects: {projects}
hidden: {projects}
star: {star}
description: "{description}"
category: {category}
author: fortyfour
externalLink: false
---

## Summary:
{description}
<div class="breaker"></div>
'''

    # Write the config to the file
    with open(filepath, "w") as file:
        file.write(config)

    print("Content written to file.")

def format_tags(tags):
    formatted_tags = ""
    for tag in tags:
        formatted_tags += f"\n- {tag}"
    return formatted_tags

# Run the program
generate_config_file()
