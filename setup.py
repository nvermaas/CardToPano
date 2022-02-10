from setuptools import setup, find_packages

setup(name='card-to-pano',
      version='1.0.0',
      description='Convert Google Cardboard images to PANO ImageSpheres',
      url='https://github.com/nvermaas/CardToPano',
      author='Nico Vermaas',
      author_email='nvermaas@xs4all.nl',
      license='BSD',
      install_requires=['requests','Pillow'],
      packages=find_packages(),
      #packages=['astrobase_services'],
      include_package_data=True,
      entry_points={
            'console_scripts': [
                  'card-to-pano=cardtopano.main:main',
            ],
      },
      )