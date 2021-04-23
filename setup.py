from setuptools import setup, find_namespace_packages


# noinspection DuplicatedCode
def read_file(fn: str, as_lines=False) -> str:
    with open(fn, 'rt', encoding='utf-8') as fp:
        return fp.readlines() if as_lines else fp.read()

setup(
    name='Backinajiffy-Pygments_Gruvbox',
    version='0.0.1',
    author="Dirk Makowski",
    description="Gruvbox Theme for Pygments",
    long_description=read_file('README.md'),
    long_description_content_type="text/markdown",
    url="https://parenchym.com",
    packages=find_namespace_packages(include=['backinajiffy.*']),
    entry_points="""
        [pygments.styles]
        gruvbox-light = backinajiffy.pygments_gruvbox:GruvboxLightStyle
        gruvbox-dark = backinajiffy.pygments_gruvbox:GruvboxDarkStyle
    """,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ],
    install_requires=read_file('requirements.txt')
)
