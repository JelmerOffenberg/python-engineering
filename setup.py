from setuptools import find_packages, setup

setup(
    name="app",
    version="0.1",
    author="Data",
    packages=find_packages("src"),
    package_dir={"": "src"},
    setup_requires=["wheel"],
    install_requires=["pandas", "pytest", "scikit-learn", "fastapi[all]", "pydantic"],
    python_requires="==3.9.*",
)
