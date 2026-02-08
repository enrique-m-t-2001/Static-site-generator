from markdown_blocks import markdown_to_html_node, extract_title
import os
def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    with open(from_path,"r") as f:
        markdown = f.read()
    
    with open(template_path,"r") as f:
        template = f.read()
    
    htmlnode = markdown_to_html_node(markdown)
    html_string = htmlnode.to_html()
    
    try:
        title = extract_title(markdown)
    except Exception as e:
        print(e)

    html = template.replace("{{ Title }}",title).replace("{{ Content }}",html_string)

    os.makedirs(os.path.dirname(dest_path),exist_ok = True)

    with open(dest_path,"w") as f:
        f.write(html)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for entry in os.listdir(dir_path_content):
        new_dir_path_content = os.path.join(dir_path_content,entry)
        if os.path.isfile(new_dir_path_content) and entry.endswith(".md"):
            final_dest_dir_path = os.path.join(dest_dir_path,entry.replace(".md",".html"))
            generate_page(new_dir_path_content,template_path,final_dest_dir_path)
        else:
            new_dest_dir_path =  os.path.join(dest_dir_path,entry)
            os.makedirs(new_dest_dir_path, exist_ok = True)
            generate_pages_recursive(new_dir_path_content,template_path,new_dest_dir_path)
