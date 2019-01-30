import setuptools

with open("README.rst") as f:
    long_description = f.read()

setuptools.setup(
    name="ltsv2json",
    version="1.0.1",
    author="Chris Rehn",
    author_email="chris@rehn.me",
    description="LTSV-to-JSON converter",
    long_description=long_description,
    url="https://github.com/hoffa/ltsv2json",
    packages=setuptools.find_packages(),
    entry_points={"console_scripts": {"ltsv2json=ltsv2json:main"}},
    license="MIT",
    classifiers=(
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Utilities",
    ),
)
