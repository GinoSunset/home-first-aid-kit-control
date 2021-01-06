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
COPY . /code/