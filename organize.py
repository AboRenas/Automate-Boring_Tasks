import os,shutil,pathlib
import logging,datetime

logging.basicConfig(level=logging.INFO,
                    format= ('%(asctime)s: %(message)s'),
                    handlers=[logging.FileHandler("file_organizer.log"),
                              logging.StreamHandler()]
                    )

logger = logging.getLogger(__name__)


File_Categories = {
    "Image":[".jpg",".jpeg", ".png", ".gif", ".bmp", ".tif", ".tiff"],
    "Documents":[".pdf", ".doc", ".txt", ".docx", ".xls", ".xlsx", ".xlsm", ".rtf"],
    "Audio": [".mp3", ".wav", ".flac", ".acc", ".ogg", ".wav", ".mp4", ".mpeg"],
    "Video": [".mp4", ".mov", ".avi", ".mpg", ".mpeg", ".mpeg2"],
    "Archives": [".zip", ".rar", ".7z", ".gz", ".bz2", ".xz"],
    "Code": [".py",".html",".css", ".java", ".ccp"],
    "Executables": [".exe",".bat", ".sh","msi"],
    "Data":[".csv", ".json", ".xml", ".yaml", ".yml",".db"]
}

def get_category(file_extension):
    for category, extensions  in File_Categories.items():
        if file_extension.lower  in extensions:
            return category
        return "Additional"
def create_directory(directory,categories):
    for category in categories:
        category_path = os.path.join(directory,category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)
            logger.info("Directory {} created".format(category_path))

def organize_file(source_dir,organize_by="category"):
    if not os.path.isdir(source_dir):
        logger.error("Source directory {} does not exist".format(source_dir))
    return

files = [f for f in os.listdir(source_dir)
         if os.path.isfile(os.path.join(source_dir, f))]
if not files:
    logger.info("No files found in source directory")
        return
logger.info(f"Found {len(files)} files to organize")

if organize_by == "category":
    organize_by_catergory(source_dir, files)
elif organize_by == "extension":
    organize_by_extension(source_dir, files)
elif organize_by == "date":
    organize_by_date(source_dir, files)
else:
    logger.error(f"unknown organization type: {organize_by}")
        return

def organize_by_catergory(source_dir, files):
    categories = set()
    for file in files:
       _, ext = os.path.splitext(file)
       category = get_category(ext)
       categories.add(category)

       create_directory(source_dir,categories)
    for file in files:
           file_path = os.path.join(source_dir, file)
           _, ext = os.path.splitext(file)
           category = get_category(ext)

           dest_dir = os.path.join(source_dir, category)
           dest_path = os.path.join(dest_dir, file)
    try:
               if not os.path.exists(dest_dir):
                   base,ext = os.path.splitext(file)
                   timestamp = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
                   new_filename = f"{base}_{timestamp}{ext}"
                   dest_path = os.path.join(dest_dir, new_filename)
                   shutil.move(file_path, dest_path)
                   logger.info(f"Moved {file_path} -> {dest_path}")
    except Exception as e:
                logger.error(f"Error moving {file}: {str(e)}")


def organize_by_extension(source_dir, files):
    extensions = set()
    for file in files:
        _, ext = os.path.splitext(file)
        if ext:
            extensions.add(ext.lower())
    for ext in extensions:
        ext_folder = os.path.join(source_dir, ext)
        if not os.path.exists(ext_folder):
            os.makedirs(ext_folder)

    for file in files:
        file_path = os.path.join(source_dir, file)
        _, ext = os.path.splitext(file)

        if ext:
            ext_folder = os.path.join(ext_folder, ext.lower())
            dest_path = os.path.join(ext_folder, file)
            try:
                if os.path.exists(dest_path):
                    base,ext_part = os.path.splitext(file)
                    timestamp = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
                    new_filename = f"{base}_{timestamp}{ext_part}"
                    dest_path = os.path.join(ext_folder, new_filename)
                shutil.move(file_path, dest_path)
                logger.info(f"Moved {file_path} -> {ext[:1]} folder")
            except Exception as e:
                logger.error(f"Error moving {file}: {str(e)}")

def organize_by_date(source_dir, files):
    for file in files:
        file_path = os.path.join(source_dir, file)
        creation_time = os.path.getctime(file_path)
        date_obj =datetime.datetime.fromtimestamp(creation_time)
        date_folder = date_obj.strftime("%Y_%m_%d_%H_%M_%S")

        date_dir = os.path.join(source_dir, date_folder)

        if not os.path.exists(date_dir):
            os.makedirs(date_dir)

        dest_path = os.path.join(date_dir, file)
        try:
            if os.path.exists(dest_path):
                base,ext_part = os.path.splitext(file)
                timestamp = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
                new_filename = f"{base}_{timestamp}{ext_part}"
                dest_path = os.path.join(date_dir, new_filename)
            shutil.move(file_path, dest_path)
            logger.info(f"Moved {file} -> {date_folder} folder")
        except Exception as e:
            logger.error(f"Error moving {file}: {str(e)}")

def search_files(directory, search_term, search_by="name"):
    if not os.path.isdir(directory):
        logger.error("Directory {} does not exist".format(directory))
        return []
    matching_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)

            if search_by == "name":
                if search_termt.lower() in file_path:
                    matching_files.append(file_path)
                elif search_by.lower() == "extension":
                    _, ext = os.path.splitext(file_path)
                    if ext.lower() in file_path:
                        matching_files.append(file_path)
                elif search_by.lower() == "content":
                    try:
                        with open(file_path, "r", error ='ignore') as f:
                            content = f.read()
                            if search_by.lower() in  content.lower():
                                matching_files.append(file_path)
                    except:
                        continue

            return matching_files


def main():
    current_dir = os.getcwd()
    target_dir = current_dir

    print("file Organize Script")
    print("============")
    print(f"Target directory: {target_dir}")
    print()

    print("Searching for files........")
    pdf_files = search_files(target_dir, ".pdf", search_by="extension")
    print(f"Found {len(pdf_files)} PDF files")
    for file in pdf_files:
        print(f" - {file}")
    print()
    print("Organizing files by category........")

    organize_by_catergory(target_dir, organize_by="category")
    print("Organizing completed! Check  logs in your terminal.......")

if __name__ == "__main__":
    main()





