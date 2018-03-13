"""For pip."""
from setuptools import setup
from setuptools import find_packages


exec(open('pdftotree/_version.py').read())
setup(
    name='pdftotree',
    version=__version__,
    description='Parse PDFs into HTML-like trees.',
    packages=find_packages(),
    install_requires=[
        'IPython',
        'beautifulsoup4',
        'future',
        'numpy',
        'pandas',
        'pdfminer.six',
        'pillow',
        'scipy',
        'six',
        'sklearn',
        'tabula-py',
        'wand',
    ],
    keywords=['pdf', 'parsing', 'html'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    url="https://github.com/HazyResearch/pdftotree",
    scripts=[
        'bin/pdftotree',
        'bin/extract_tables',
    ],
    classifiers=[  # https://pypi.python.org/pypi?:action=list_classifiers
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3 :: Only",
    ],
    project_urls={
        'Tracker': 'https://github.com/HazyResearch/pdftotree/issues',
        'Source': 'https://github.com/HazyResearch/pdftotree',
    },
    python_requires='>3',
    author="Hazy Research",
    author_email="senwu@cs.stanford.edu",
    license='MIT',
)
