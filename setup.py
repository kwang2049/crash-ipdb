from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf-8") as fh:
    readme = fh.read()

setup(
    name="crash-ipdb",
    version="0.0.4",
    author="Kexin Wang",
    author_email="kexin.wang.2049@gmail.com",
    description="Trigger ipdb whenever Python crashes",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/kwang2049/crash-ipdb",
    project_urls={
        "Bug Tracker": "https://github.com/kwang2049/crash-ipdb/issues",
    },
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        'ipython==7.34'
    ],
)