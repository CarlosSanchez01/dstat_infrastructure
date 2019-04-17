# Dstat update

Simple Dstat infrastructure for Raspberry pi allow for chronoamperometry (CA), linear sweep voltammetry (LSV), cyclic voltammetry (CV) and electrochemical impedance spectroscopy (EIS) measurements.

## Dstat interface raspberry pi

This platform should be simple to not saturate the resources of the Rpi.
Due to the long-term nature of the experiments, the data managemnet should dump to file continuously and avoid saturating RAM and CPU specifications.

## Client-server infrastructure

A server will allow to control the dstat connected to each of the raspberry pi and plot the results according to the configuration.

Use Socket in Python?
Socket communication.

Raspberry pi as a server that is continuously controlling the dstat and serving information.


### Local wifi network

A hub will be used to build the network


### Node js

Using asynchronous data exchange is required. Node js can be a platform to develop this.

### Unix base

Linux will be used to facilitate interaction between raspberry pi and server