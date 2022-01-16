import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="streamlit-barfi",
    version="0.1.0",
    author="Adithya Krishnan",
    author_email="krishsandeep@gmail.com",
    description="Streamlit component for a graphical programming environment to perform simulations.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/krish-adi",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "streamlit >= 0.63",
        "networkx >= 2.6.2",
    ],
)