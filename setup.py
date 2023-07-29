from setuptools import setup, find_packages

setup(
    name='fromchaos',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'openai',
        'tenacity',
    ],
    author='Ryder Damen',
    author_email='dev@ryderdamen.com',
    description='A python library for extracting organized data out of chaos using large-language-models (LLMs) like ChatGPT.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ryderdamen/fromchaos',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License', 
        'Programming Language :: Python :: 3.8',
    ],
    python_requires='>=3.8',
)
