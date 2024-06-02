import setuptools

__version__="0.0.0"
AUTHOR_NAME="Abhikkumar619"
AUTHOR_EMAIL="abisheky194@gmail.com"
REPO_NAME="mlops_implementation"
SRC_REPO="mlops"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="implementing the mlops tools", 
    long_description_content="text/markdown", 
    url=f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker":f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"":"src"}, 
    packages=setuptools.find_packages(where="src")
)