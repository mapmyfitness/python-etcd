from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
NEWS = open(os.path.join(here, 'NEWS.txt')).read()


version = '0.3.3'

install_requires = [
    'urllib3>=1.7',
    'pyOpenSSL>=0.14',
]

test_requires = [
    'mock',
    'nose',
]

setup(
    name='mmf-python-etcd',
    version=version,
    description="A python client for etcd",
    long_description=README + '\n\n' + NEWS,
    classifiers=[
        "Topic :: System :: Distributed Computing",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Topic :: Database :: Front-Ends",
    ],
    keywords='etcd raft distributed log api client',
    author='Jose Plana',
    author_email='jplana@gmail.com',
    url='http://github.com/mapmyfitness/python-etcd',
    download_url='http://pypi.mapmyfitness.com/mmf/stable/+simple/mmf-python-etcd/',
    license='MIT',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    tests_require=test_requires,
    test_suite='nose.collector',

)
