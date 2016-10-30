from distutils.core import setup

setup(
    name='spiced-singleton-tasks',
    version="1.0.0",
    description='Singleton tasks are simple now. With spices they will be more tasty.',
    url='none',
    packages=['spicedtasks',],
    package_data={'spicedtasks': ['spicedtasks.py']},
    author='Nikita Malovichko',
    author_email='nvmalovichko@gmail.com',
    install_requires=['redis',]
)
