FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
COPY requirements-dev.txt /code/
RUN pip install -r requirements-dev.txt
RUN git clone https://github.com/dmtx/libdmtx.git && \
    cd libdmtx && \
    ./autogen.sh && \
    ./configure && \
    make && make install

RUN apt update -y && \ 
    cd /opt && \
    apt install -y libgl1-mesa-glx cmake && \
    wget -O opencv.zip https://github.com/opencv/opencv/archive/master.zip && \
    unzip opencv.zip  && \
    mkdir -p build && cd build && \
    cmake  ../opencv-master && \
    cmake --build . && \
    rm -rf opencv.zip && \
    rm -rf /var/lib/apt/lists/* && \
    apt clean


COPY . /code/
