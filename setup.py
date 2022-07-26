from distutils.core import setup
setup(
    name='lawsplit',
    packages=['lawsplit'],
    version='1.0.3',
    license='MIT',
    description='LawSplit: A smart legal text sentence splitter',
    author='Pritish Wadhwa',
    author_email='pritish19440@iiitd.ac.in',
    url='https://github.com/PritishWadhwa',
    download_url='https://github.com/PritishWadhwa/LawSplit/archive/refs/tags/v1.0.3.tar.gz',
    keywords=['LEGAL', 'SPLIT', 'PARAGRAPH', 'DOCUMENTS', 'NLP', 'SENTENCES'],
    install_requires=[
        'pysbd'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
