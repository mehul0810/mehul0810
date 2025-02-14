import feedparser

# URL for your RSS feed (update if needed)
RSS_FEED_URL = "https://mehulgohil.com/rss"

# Path to your README.md
READ_ME_PATH = "README.md"

# Parse the RSS feed
feed = feedparser.parse(RSS_FEED_URL)

# Extract the latest 3 blog posts (customize the count as desired)
latest_posts = feed.entries[:3]
post_lines = []
for post in latest_posts:
    post_lines.append(f"- [{post.title}]({post.link})")

# Read the current README.md content
with open(READ_ME_PATH, "r", encoding="utf-8") as file:
    content = file.read()

# Define the markers for the blog posts section
start_marker = "<!-- BEGIN BLOG POSTS -->"
end_marker = "<!-- END BLOG POSTS -->"

# Locate the markers in the README.md
start_index = content.find(start_marker)
end_index = content.find(end_marker, start_index)

if start_index == -1 or end_index == -1:
    raise Exception("Markers for blog posts not found in README.md. Please ensure the markers exist.")

# Create the new blog posts section content
new_section = start_marker + "\n" + "\n".join(post_lines) + "\n" + end_marker

# Replace the old section with the new one
new_content = content[:start_index] + new_section + content[end_index + len(end_marker):]

# Write the updated content back to README.md
with open(READ_ME_PATH, "w", encoding="utf-8") as file:
    file.write(new_content)
