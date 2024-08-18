from obsidian_to_hugo import ObsidianToHugo
from py_src.config import vault_path, hugo_content_path
import os
import schedule
import time
from icecream import ic

import subprocess

def run_git_command(command):
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    print(result.stdout)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")

def push():
    run_git_command("git add .")
    run_git_command('git commit -m "auto update"')
    run_git_command("git push")





def check_file_path() -> bool:
  if os.path.exists(vault_path) and os.path.exists(hugo_content_path):
    return True

  return False

"""
  will add _index.md file base on the folder name in your obsidian vault
  good so you can adjust the title whenever you want in obsidian
"""


#updates the hugo_index on change
def update_hugo_index():
    for root, dirs, files in os.walk(vault_path):
      for page in dirs:
          if page == ".obsidian":
            continue


          if page == "notes":
            continue

          v_index_path = os.path.join(vault_path, page, "_index.md")
          h_index_path = os.path.join(hugo_content_path, page, "_index.md")

          with open(v_index_path, "r", encoding="utf-8") as v_f:
              v_content = v_f.read()

          # Open the Hugo file in read-write mode
          with open(h_index_path, "r+", encoding="utf-8") as h_f:
              h_content = h_f.read()

              # Check if contents differ
              if v_content != h_content:

                  h_f.seek(0)
                  # Write the new content
                  h_f.write(v_content)
                  # Truncate the file to the new size
                  h_f.truncate()
      break #break on the first iter since we just want the first loop


#given dirs will make hugo_index in value
def generate_hugo_index(dirs : list):
  for page in dirs:
    if page == ".obsidian":
       continue

    if page == "notes":
       continue

    front_matter = f"""+++
title = "{page.lower()}"
menu = "main"
+++
"""
    #if vault has no index file then generate... stop issue of deleting index.md now in source
    if not os.path.exists(os.path.join(vault_path, page, "_index.md")):
      with open(os.path.join(vault_path, page, "_index.md"), "w+", encoding="utf-8") as f:
        f.write(front_matter)


# Handles the date files

def get_date(filepath: str):
  # filepath.split('/\')
  creation_time = os.path.getctime(filepath)
  creation_date = datetime.fromtimestamp(creation_time).strftime('%Y-%m-%d')

  return creation_date


from datetime import datetime

def generate_hugo_front_matter(title : str, date : str):

    front_matter = f"""+++
title = "{title.lower()}"
date = "{date}"
+++
"""
    return front_matter


def process_md_info(text: str , title : str, date : str):
  md_string = generate_hugo_front_matter(title, date)
  return md_string + text

def add_meta_data_to_obsidian_value():

  for root, dirs, files in os.walk(vault_path):
    #add _index.md files to files that do not have
    if root == vault_path:
      generate_hugo_index(dirs)

    for file in files:
        if file.endswith(".md"):
            with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                content = f.read()

            #prob a better way but whatever
            #handles empty files
            if len(content) == 0:
               continue

            #files that are not empty and no data
            if len(content) > 0:
              if content[0] == "+" or content[1] == "+" or content[2] == "+":
                continue


            date = get_date(filepath=os.path.join(root, file))
            md_string = process_md_info(content, title=file, date=date)

            with open(os.path.join(root, file), "w", encoding="utf-8") as f:
                  f.write(md_string)


def filter_index(file_contents: str, file_path: str) -> bool:
    # do something with the file path and contents
    if file_path != "_index.md":
        return True # copy file
    else:
        return False # skip file



def main():
  if not check_file_path():
    raise FileExistsError("vault or hugo content file paths do not exist, check config.py filepaths")

  #go into vault and check for new files
  #then addes all meta data to not files that do not have
  add_meta_data_to_obsidian_value()

  obsidian_to_hugo = ObsidianToHugo(
      obsidian_vault_dir=vault_path,
      hugo_content_dir=hugo_content_path,
      filters=[],
  )

  obsidian_to_hugo.run()
  #at this point all folders should have an _index.md file now we update them we the new index files.

  update_hugo_index()

  push()

if __name__ == "__main__":
   main()
  # schedule.every().day.at("23:30").do(main)

  # while True:
  #    schedule.run_pending()
  #    time.sleep(1)