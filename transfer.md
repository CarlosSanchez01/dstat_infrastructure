## Transfer files between development and raspberry pi

### Set raspberry pi as fixed ip

Wifi router serves as hub between the PC and the raspberry pi

~~~~
192.168.0.201
~~~~

### SCP

~~~~
scp -r /local_folder_to_transfer user@remoteIP:folder_destination

scp -r /home/carlos/dstat_carlos/dstat_simple/ pi@192.168.0.201:Desktop
~~~~

This simplify changing files in local and then transfer to raspberry pi


## Connection to run programs

### SSH

~~~~
ssh -X pi@192.168.0.201
~~~~