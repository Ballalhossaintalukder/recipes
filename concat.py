import re

input_file = 'nginx.yml'

with open(input_file, 'r') as f:
    content = f.read()

# Define the regex pattern
# captures "    file: " followed by anything until end of line
pattern = r"(^\s*)file:\s*(.*\.yml)"

# Define a function to generate the replacement
def replacement_func(match):
    prefix = match.group(1) # The "    file: " part (keeps indentation)
    old_val = match.group(2) # The "html-cra.yml" part
    content = ""
    with open(old_val, 'r') as f:
        for line in f:
            content += f"{prefix}  {line}"

    return f"{prefix}source: |\n{prefix}  {content.strip()}"

# Apply the substitution line by line (multiline flag)
new_content = re.sub(pattern, replacement_func, content, flags=re.MULTILINE)

print(new_content)