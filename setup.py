from setuptools import setup, find_packages

setup(name='python_people_names',
      version='0.0.19',
      description='people\'s name parser',
      author='lynzt',
      url='https://github.com/lynzt/python_people_names',
      packages=['people_names'],
      dependency_links=[
        'git+git://github.com/lynzt/python_utils.git',
        ]
     )
