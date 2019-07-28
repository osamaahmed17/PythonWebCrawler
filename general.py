import os

#Each website you crawl would be a seperate project (folder)
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating project' + directory)
        os.makedirs(directory)


create_project_dir("TestFile")

#create queue and crawl files(if not created)
def create_data_files(project_name,base_url):
        queue= project_name+'queue.txt' #This file would contain all the links of the website waiting to be crawled
        crawled =project_name+'crawled.txt' #This file would contain all the links of the website which have been crawled
        if not os.path.isfile(queue):
                write_file(queue,base_url)
        if not os.path.isfile(crawled):
                write_file(crawled,'')


#for creating new file
def write_file(path,data):
        f=open(path,'w')
        f.write(data)
        f.close()
        
