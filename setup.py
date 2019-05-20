from setuptools import setup, find_packages

setup(
    name="popo",
    version="0.0.1",
    url="https://github.com/MagnaXSoftware/popo",
    license="MIT",
    author="MagnaX Software",
    author_email="info@magnax.ca",
    description="POPO gives you a simple, small, clean ORM with Plain Old Python Objects.",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Database",
    ],
)
