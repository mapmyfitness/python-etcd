#!/bin/bash
 docker run -ti -v /home/core/share/python-etcd:/opt/python-etcd/ -w /opt/python-etcd/ svc-personal-goals01.mapmyfitness.com:5000/svc-personal-goals bash -c \
". /opt/virtualenvs/mmf/bin/activate && python setup.py sdist upload -r mmfpypi && python setup.py bdist_wheel upload -r mmfanywheel"
