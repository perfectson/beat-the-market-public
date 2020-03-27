FROM gitpod/workspace-full
                    
USER gitpod

# Install custom tools, runtime, etc. using apt-get
# For example, the command below would install "bastet" - a command line tetris clone:
#
RUN sudo mkdir /home/pippo 
RUN wget https://repo.continuum.io/archive/Anaconda3-5.0.1-Linux-x86_64.sh
RUN bash Anaconda3-5.0.1-Linux-x86_64.sh -b
RUN rm Anaconda3-5.0.1-Linux-x86_64.sh

ENV PATH /home/gitpod/anaconda3/bin:$PATH

#RUN conda config --set allow_conda_downgrades true
RUN conda install conda=4.6.11
RUN conda create -n zip35 python=3.5 
RUN conda init bash
RUN conda activate zip35 
#RUN source activate zip35
#RUN conda install -n yourenvname [package]
#RUN sudo apt-get -q update &&      sudo apt-get install -yq bastet &&      sudo rm -rf /var/lib/apt/lists/*
#
# More information: https://www.gitpod.io/docs/config-docker/
