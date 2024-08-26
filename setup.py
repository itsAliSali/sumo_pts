from setuptools import setup


with open('README.md', 'r') as f:
      description = f.read()

setup(name='sumo_pts',
      version='0.2',
      description='A Python interface for simulating public transport systems using SUMO.',
      url='https://github.com/itsAliSali/sumo_pts',
      author='itsAliSali',
      author_email='ali.salimian@rwth-aachen.de',
      license='EPL2',
      packages=['sumo_pts'],
      zip_safe=False,
      long_description=description,
      long_description_content_type='text/markdown',
)
