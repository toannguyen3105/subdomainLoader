from setuptools import setup, find_packages

setup(
    name="subdomainLoader",
    version="0.1.0",
    description="A Python library to manage subdomains with Nginx and Certbot",
    author="Tony Nguyen",
    author_email="toannh8.ptit@gmail.com",
    packages=find_packages(),
    install_requires=[],  # Add dependencies if needed
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
