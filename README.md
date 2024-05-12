# Flower Enabled Federated Learning

This directory contains data model, code to run federated code for healthcare, and clients and server code.

# Project Setup

Start by cloning the project
```shell
$ git clone --depth=1 
```
This will create a new directory ehc_prototype with subfolders and files.

# Install dependencies

Run the following command to setup requirements:
```shell
cd ehc_prototype
pip install requirements.txt
```
Note the above requires pip already installed.

# Install Mysql
Install mysql on preferred or using OS

# Run the SQL script to import database
Connet to mysql database, and then run create a database first.
```shell
ehc_prototype;
USE  ehc_prototype;
source /ehc_prototype/sql/ddl.sql
```

# Data
The data it uses is very sensitive, and cannot be publicly shared. however, for you to work with real data, you can put all data the data/all_data folder. Each along with image files, each image file should be named as `filename_label.jpg` where label indicates the classified label of the image. the model will automatically extract this information.
Moreover, for federated model, split the data as follows:
## Two clients Example
### Skewed data
Distribute the whole data in >=60 and <=40 splits in data/cleint_1 and data_cleint_2 folders respectively
You can play with how you want to order your data to run your models. We chose the ones presented in paper.

# Registring Owners and Models

Have a look and run the method in federated/requests/request.py file

# Running the federated learning server:

```shell
python3 federed/server.py
```
# Running clients - each in a separate terminal.

Before each run in a terminal, set the folder in the client.py and then run
```shell
python3 federated/client.py
```


```shell
python3 federated/client.py
```


# Running stand alone locally only

Use the simple.py in the simple folder.
```shell
python3 simple/simple.py 
```
