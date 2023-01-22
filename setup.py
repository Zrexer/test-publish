from setuptools import setup, find_packages


setup(
    name='example_publish_pypi_medium',
    version='0.1',
    license='MIT',
    author="arshia",
    author_email='hslhostlet@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/Zrexer/test-publish',
    keywords='example project',
    install_requires=[
          'scikit-learn',
      ],

)
