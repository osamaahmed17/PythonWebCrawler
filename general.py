import os

#Each website you crawl would be a seperate project (folder)
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating project' + directory)
        os.makedirs(directory)


create_project_dir("TestFile")