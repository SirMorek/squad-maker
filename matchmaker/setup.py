from setuptools import setup

setup(name='matchmaker',
      version='0.1',
      description='matchmaking for hockey squads',
      author='Brendan Anderson',
      author_email='SirMorek@gmail.com',
      license='MIT',
      packages=['matchmaker'],
      zip_safe=False,
      setup_requires=['pytest-runner'],
      tests_require=['pytest'])
