# Requirements development dstat

## Conda environment

~~~~
conda env create -f <./conda-env.yml>
~~~~

## Packages

conda-env.yml 

~~~~
name: dstat
channels:
  - conda-forge
  - mdryden
  - defaults
dependencies:
  - ca-certificates=2018.4.16=0
  - certifi=2018.4.16=py27_0
  - nb_conda_kernels=2.1.0=py27_0
  - openssl=1.0.2o=0
  - appnope=0.1.0=py27_0
  - backports=1.0=py27_0
  - backports_abc=0.5=py27_0
  - bleach=1.5.0=py27_0
  - configparser=3.5.0=py27_0
  - curl=7.54.1=0
  - cycler=0.10.0=py27_0
  - decorator=4.1.2=py27_0
  - entrypoints=0.2.3=py27_0
  - enum34=1.1.6=py27_0
  - expat=2.1.0=0
  - freetype=2.5.5=2
  - funcsigs=1.0.2=py27hb9f6266_0
  - functools32=3.2.3.2=py27_0
  - get_terminal_size=1.0.0=py27_0
  - gettext=0.19.8=1
  - git=2.11.1=0
  - html5lib=0.9999999=py27_0
  - icu=54.1=0
  - intel-openmp=2018.0.0=h8158457_8
  - ipykernel=4.6.1=py27_0
  - ipython=5.3.0=py27_0
  - ipython-notebook=4.0.4=py27_0
  - ipython_genutils=0.2.0=py27_0
  - jbig=2.1=0
  - jinja2=2.9.6=py27_0
  - jpeg=9b=0
  - jsonschema=2.6.0=py27_0
  - jupyter_client=5.1.0=py27_0
  - jupyter_core=4.3.0=py27_0
  - krb5=1.13.2=0
  - libcxx=4.0.1=h579ed51_0
  - libcxxabi=4.0.1=hebd6815_0
  - libffi=3.2.1=1
  - libgfortran=3.0.1=h93005f0_2
  - libiconv=1.14=0
  - libpng=1.6.30=1
  - libssh2=1.8.0=0
  - libtiff=4.0.6=3
  - llvmlite=0.21.0=py27hac8ee23_0
  - markupsafe=1.0=py27_0
  - matplotlib=2.0.2=np113py27_0
  - mistune=0.7.4=py27_0
  - mkl=2018.0.1=hfbd8650_4
  - nbconvert=5.2.1=py27_0
  - nbformat=4.4.0=py27_0
  - notebook=5.0.0=py27_0
  - numba=0.36.2=np113py27h7c931aa_0
  - numpy=1.13.3=py27h62f9060_0
  - pandas=0.20.3=py27_0
  - pandocfilters=1.4.2=py27_0
  - path.py=10.3.1=py27_0
  - pathlib2=2.3.0=py27_0
  - patsy=0.4.1=py27_0
  - pcre=8.39=1
  - pexpect=4.2.1=py27_0
  - pickleshare=0.7.4=py27_0
  - pip=9.0.1=py27_1
  - prompt_toolkit=1.0.15=py27_0
  - ptyprocess=0.5.2=py27_0
  - pygments=2.2.0=py27_0
  - pyparsing=2.2.0=py27_0
  - pyqt=5.6.0=py27_2
  - python=2.7.13=0
  - python-dateutil=2.6.1=py27_0
  - pytz=2017.2=py27_0
  - pyyaml=3.12=py27_0
  - pyzmq=16.0.2=py27_0
  - qt=5.6.2=2
  - readline=6.2=2
  - scandir=1.5=py27_0
  - scipy=1.0.0=py27h793f721_0
  - seaborn=0.8=py27_0
  - setuptools=36.4.0=py27_0
  - simplegeneric=0.8.1=py27_1
  - singledispatch=3.4.0.3=py27_0
  - sip=4.18=py27_0
  - six=1.10.0=py27_0
  - sqlite=3.13.0=0
  - ssl_match_hostname=3.5.0.1=py27_0
  - statsmodels=0.8.0=np113py27_0
  - subprocess32=3.2.7=py27_0
  - terminado=0.6=py27_0
  - testpath=0.3.1=py27_0
  - tk=8.5.18=0
  - tornado=4.5.2=py27_0
  - traitlets=4.3.2=py27_0
  - wcwidth=0.1.7=py27_0
  - wheel=0.29.0=py27_0
  - xz=5.2.3=0
  - yaml=0.1.6=0
  - zlib=1.2.11=0
  - adwaita-icon-theme=3.24.0=1
  - arrow=0.10.0=py27_0
  - at-spi2-atk=2.24.1=2
  - at-spi2-core=2.24.1=2
  - atk=2.24.0=3
  - cairo-gobject=1.14.8=8
  - dbus-client=1.10.18=0
  - dfu-programmer=0.7.2=2
  - dstat-interface=1.4.6=py27_0
  - dstat-interface-deps=1.0=0
  - gdk-pixbuf=2.36.6=2
  - glib=2.52.2=5
  - gobject-introspection=1.52.1=2
  - gtk3=3.22.15=4
  - harfbuzz=1.4.6=3
  - libepoxy=1.4.2=5
  - libusb=1.0.21=0
  - pango=1.40.6=2
  - pixman=0.34.0=1
  - py2cairo=1.10.0=py27_0
  - pygobject3=3.24.2=py27_3
  - pyserial=3.3=py27_0
  - zmq-plugin=0.2.post14=py27_0
  - pip:
    - backports.shutil-get-terminal-size==1.0.0
    - backports.shutil-which==3.5.1
    - backports.ssl-match-hostname==3.5.0.1
    - chardet==3.0.4
    - colorama==0.3.9
    - idna==2.6
    - paver==1.2.4
    - pygobject==3.24.1
    - requests==2.18.4
    - urllib3==1.22
    - vmprof==0.4.10

~~~~
