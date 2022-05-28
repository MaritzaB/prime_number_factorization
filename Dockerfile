FROM ubuntu:latest

RUN apt-get update && \
    apt upgrade --yes && \
    apt-get install make --yes
    
RUN apt-get install python3 --yes && \
    apt install python3-pip --yes

RUN ln -snf /usr/share/zoneinfo/Etc/UTC /etc/localtime \
    && echo "Etc/UTC" > /etc/timezone \
    && apt-get update \
    && apt-get upgrade -y \
    && apt-get install texlive-latex-base texlive-latex-extra texlive-fonts-recommended xzdec -y \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pytest
RUN pip install black
RUN pip install -U matplotlib
