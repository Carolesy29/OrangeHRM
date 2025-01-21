import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="orange-hrm-test",
    version="1.0.0",
    author="Esymar Vega",
    author_email="carolesy2985@gmail.com",
    description="A Python test project for Inspection and hired.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['tests'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
