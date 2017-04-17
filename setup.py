from setuptools import setup

setup(name='geo-code',
      version='0.0.1',
      description='Lightweight Python module for geocoding addresses via the Google Geocoding API',
      url='https://github.com/jwilber/geo-code',
      author='Jared Wilber',
      author_email='jdwlbr@gmail.com',
      license='GNU3',
      packages=['geo-code'],
      install_requires=[
            'pandas',
            'requests',
      ],
      zip_safe=False)