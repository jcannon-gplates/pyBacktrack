import os.path
from setuptools import setup

# Open project description text file.
#
# The first line must be the short description.
# Followed by a blank line.
# Followed by the long description.
with open(os.path.join('docs', 'project_description.txt')) as project_description_file:
    project_description_lines = project_description_file.read().strip().split("\n")
project_description = project_description_lines[0]
project_long_description = "\n".join(project_description_lines[2:])

# Read package __version__.
exec(open('pybacktrack/version.py').read())

setup(
    name='pybacktrack',
    version=__version__,
    description=project_description,
    long_description=project_long_description,
    url='https://github.com/EarthByte/pyBacktrack',
    author='John Cannon',
    author_email='john.cannon@sydney.edu.au',
    license='GPL',
    classifiers=['Intended Audience :: Developers',
                 'Intended Audience :: Education',
                 'Intended Audience :: Science/Research',
                 'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
                 'Operating System :: POSIX :: Linux',
                 'Operating System :: MacOS :: MacOS X',
                 'Operating System :: Microsoft :: Windows',
                 'Programming Language :: Python :: 2 :: Only',
                 'Programming Language :: Python :: 2.7',
                 'Topic :: Scientific/Engineering'],
    keywords='bathymetry backtrack backstrip rift subsidence tectonic',
    project_urls={
        'Documentation': 'http://pybacktrack.readthedocs.io',
        'Source': 'https://github.com/EarthByte/pyBacktrack'
    },
    packages=['pybacktrack', 'pybacktrack.util'],
    install_requires=['numpy', 'scipy'],
    # 'pytest-runner' is needed so that 'python setup.py test' works.
    # It gets installed to local './.eggs', not installed on the system...
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    python_requires='==2.7.*',  # Python 3 currently not supported.
    #
    # From the setuptools docs...
    #
    # If include_package_data set to True, this tells setuptools to automatically include any data files
    # it finds inside your package directories that are specified by your MANIFEST.in file.
    #
    # You do not need to use package_data if you are using include_package_data,
    # unless you need to add e.g. files that are generated by your setup script and build process.
    #
    include_package_data=True,
    # package_data={'pybacktrack': ['bundle_data/*']},
    zip_safe=False)