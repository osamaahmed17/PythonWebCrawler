import os

#Each website you crawl would be a seperate project (folder)
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating project' + directory)
        os.makedirs(directory)


create_project_dir("TestFile")

#create queue and crawl files(if not created)
def create_data_files(project_name,base_url):
        queue= project_name+'/queue.txt' #This file would contain all the links of the website waiting to be crawled
        crawled =project_name+'/crawled.txt' #This file would contain all the links of the website which have been crawled
        if not os.path.isfile(queue):
                write_file(queue,base_url)
        if not os.path.isfile(crawled):
                write_file(crawled,'')


#for creating new file
def write_file(path,data):
        f=open(path,'w')
        f.write(data)
        f.close()

#Add data into existing file
def append_to_file(path,data):
        with open(path,a) as file:
                file.write(data+'\n')

#Delete the contents of the file
def delete_file_contenets(path):
        with open(path,'w'):
                pass

#Read the file and convert each line to set item
def file_to_set(file_name):
        results=set()
        with open (file_name,'rt') as f:
                for line in f:
                        results.add(line.replace('\n',''))
        return results

#iterate through set, each item will be in the file
def set_to_file(links,file):
        delete_file_contents(file)
        for link in sorted(links):
                append_to_file(file,link) 

        
