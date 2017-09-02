from setuptools import setup

setup(name='walkabout',
      version='0.0.1',
      description='Stochastic path generator',
      author='Michael Jones',
      author_email='mikejonesab12@gmail.com',
      license='MIT',
      keywords = ['stochastic', 'finance', 'brownian', 'geometric brownian'],
      install_requires=[
        'numpy==1.13.1',
        'matplotlib==2.0.2'
      ])
