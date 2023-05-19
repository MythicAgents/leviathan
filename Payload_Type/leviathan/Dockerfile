FROM itsafeaturemythic/mythic_python_go:latest

RUN git clone https://github.com/pawliczka/CRX3-Creator /CRX3-Creator
RUN pip3 install cryptography==3.3.2
RUN pip3 install pycparser==2.19
RUN pip3 install six==1.13.0

WORKDIR /Mythic/

COPY [".", "."]

RUN make build

CMD make run