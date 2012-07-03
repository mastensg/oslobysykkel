from distutils.core import setup

setup(
    name="OsloBysykkel",
    version="0.1.0",

    author="Martin Stensgård",
    author_email="mastensg@ping.uio.no",

    package_dir={"": "oslobysykkel"},
    py_modules=["oslobysykkel"],

    scripts=[
        "bin/oslobysykkel-query",
        ],

    url="http://pypi.python.org/pypi/OsloBysykkel/",

    license="GNU General Public Licence 3",

    platforms=["POSIX"],

    description="Interface for ClearChannel's Oslo city bike API.",
)
