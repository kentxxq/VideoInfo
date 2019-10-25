import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='VideoInfo',
    version='1.0',
    description='parse online video file metadata',
    author='kentxxq',
    author_email='admin@kentxxq.com',
    url='https://www.github.com/kentxxq/VideoInfo',
    packages=['VideoInfo'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=[
        "construct==2.8.8",
        "requests==2.22.0"
    ]
)
