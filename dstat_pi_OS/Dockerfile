FROM ubuntu:latest

RUN apt-get update && apt-get install -y firefox

RUN apt-get install -y gobject-introspection python-gobject python-pip sudo
RUN pip install --upgrade pip

RUN apt-get install -y libgtk-3-dev

ENV TZ=Europe/Minsk
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get update && apt-get install -y python-tk
RUN apt-get install -y libcanberra-gtk-module libcanberra-gtk3-module

RUN python -V

RUN pip install dstat-interface
RUN pip install cairocffi


RUN apt-get install -y git
RUN git clone http://microfluidics.utoronto.ca/gitlab/dstat/dstat-interface.git

CMD ls
#CMD $DISPLAY

RUN export uid=1000 gid=1000 && \
    mkdir -p /home/developer && \
    echo "developer:x:${uid}:${gid}:Developer,,,:/home/developer:/bin/bash" >> /etc/passwd && \
    echo "developer:x:${uid}:" >> /etc/group && \
    echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \
    chmod 0440 /etc/sudoers.d/developer && \
    chown ${uid}:${gid} -R /home/developer

USER developer
ENV HOME /home/developer
CMD sudo usermod -a -G dialout developer
#CMD /usr/bin/firefox

RUN pip --version
RUN python -m serial.tools.list_ports
RUN sudo apt-get install -y screen
RUN sudo apt-get install -y usbutils


CMD RUN python -m serial.tools.list_ports
CMD python dstat-interface/dstat_interface/main.py

