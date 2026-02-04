from setuptools import setup, find_packages

setup(
    name="topsis-kinjal-102303858",
    version="1.0.0",
    author="Kinjal",
    author_email="kinjalarora0001@gmail.com",
    description="TOPSIS implementation as a Python package",
    long_description="A command-line tool to perform TOPSIS analysis.",
    long_description_content_type="text/plain",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas"
    ],
    entry_points={
        "console_scripts": [
            "topsis=topsis.topsis:main"
        ]
    },
    python_requires=">=3.7",
)
