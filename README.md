# REPORT TOOL README
This is a report tool designed to give reports both on terminal and as a txt file for the Udacity's provideds News DB.

### Questions this tool answer
<ul>
<li>What are the most read articles?</li>
<li>What are the most popular authors?</li>
<li>In wich days more than 1% of logs where errors?</li>
</ul>

## Getting started

### Prerequisites
This tool is intended to work only in the presence of the newsdata DB provided by Udacity via their pre-setup virtual machine configured with the use of Vagrant and Virtual Box.

To install Vagrant either download from:
https://www.vagrantup.com/downloads.html
or in an unix-like terminal run
```
sudo apt install vagrant
```

To install Virtual Box either download from:
https://www.virtualbox.org/wiki/Downloads
or in an Unix-like terminal run
```
sudo apt install virtualbox
```

Download Udacity VM from either
https://github.com/udacity/fullstack-nanodegree-vm
or use the git clone command
```
git clone https://github.com/udacity/fullstack-nanodegree-vm <em>folder_name_here</em>
```

OBS: if you don't have git installed you can run on an Unix-like terminal
```
sudo apt install git
```

The Udacity provided database, download it from
https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

Make sure the database file is extracted inside the folder "/vagrant" in your VM folder.

### Installing

In your terminal, go to the folder "/vagrant" inside the VM folder
```
sudo vagrant up
```

Wait for the system setup and then connect via SSH
```
sudo vagrant ssh
```

After it go for the shared folder vagrant
```
cd /vagrant
```

Now setup the DB via
```
psql -d news -f newsdata.sql
```

Now download or clone the report_tool inside the "/vagrant" folder
```
git clone https://github.com/leoaucar/report_tool report_tool
```

### How to use
To generate a new report on the DB just run the file "report.py", located in the folder "/vagrant/report_tool".
```
python3 report.py
```

The tool will generate a .txt file that contains the results of the query and is stored in the same folder of the python file.


## Built With
* Python3
* Atom text editor
* PostgreeSQL DB
* Vagrant
* Virtual Box VM
* Ubuntu 16.04
* Git version control


## Authors
Leonardo Aucar


## License
Uses MIT open source license https://opensource.org/licenses/MIT
