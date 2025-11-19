from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="hotel",
    version="0.1",
    author="Matias F. Adell",
    packages=find_packages(),       # identificar paquetes automaticamente
    install_requires=requirements,
)