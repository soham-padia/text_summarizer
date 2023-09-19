import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

__version__ = "0.0.1"

REPO_NAME="text_summarizer"
AUTHOR_USER_NAME="soham-padia"
SRC_REPO="text_summarizer"
AUTHOR_EMAIL="sohampadia10@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small nlp project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)
