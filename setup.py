from distutils.core import setup

setup(
    name='celery-redis-singlton-task',
    version="1.0.1",
    description='Add a celery single task support',
    url='none',
    packages=['spicedtasks',],
    package_data={'spicedtasks': ['spicedtasks.py']},
    author='Nikita Malovichko',
    author_email='nvmalovichko@gmail.com',
    install_requires=['redis',]
)
