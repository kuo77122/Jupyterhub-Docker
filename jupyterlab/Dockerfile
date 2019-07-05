FROM jupyter/scipy-notebook

MAINTAINER Che-Nan Kuo <kuo77122@gmail.com>

USER root
# Install LightGBM
RUN apt-get update && \
    apt-get install -y cmake build-essential gcc g++ git && \
    rm -rf /var/lib/apt/lists/*

RUN git clone --recursive --branch stable https://github.com/Microsoft/LightGBM && \
    mkdir LightGBM/build && \
    cd LightGBM/build && \
    cmake .. && \
    make -j4 && \
    make install && \
    cd ../python-package && python setup.py install && \
    cd ../.. && \
    rm -rf LightGBM

# Install Catboost and Visualization tools
RUN pip install catboost ipywidgets
RUN jupyter nbextension enable --py widgetsnbextension

# Install XGBoost library
RUN git clone --recursive https://github.com/dmlc/xgboost && \
    cd xgboost && \
    make -j4 && \
    cd python-package; python setup.py install

# Install nbresuse
RUN pip install nbresuse

# Clean
RUN apt-get autoremove -y && apt-get clean && \
    rm -rf /usr/local/src/*
