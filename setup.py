from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="cookie-licking-detector",
    version="0.1.0",
    author="Kushal Garg",
    author_email="kushalgarg71106@outlook.com",
    description="Detect and manage stale issue claims on GitHub",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kshlgrg/cookie-licking-detector",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "requests>=2.31.0",
        "python-dotenv>=1.0.0",
        "transformers>=4.30.0",
        "torch>=2.0.0",
        "numpy>=1.24.0",
    ],
)
