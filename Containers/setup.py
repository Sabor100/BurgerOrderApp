from setuptools import setup, find_packages

setup(
    name='PA1489', # name of project
    version='0.1', # version of our product. We have many versions before but the setup file has been created now so I called it version 0.1
    author='Team14', # name of team
    author_email='thch24@student.bth.se', # my email, only for example for file
    description='Application that customers can order their burger and kitchen can see the orders', # description about our project
    long_description=open('README.md').read(), # link to file readme, ofcourse
    url='https://github.com/HaileyLV/PA1489-project', # link to our project on Github
    packages=find_packages(), # it will find all module in out project
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
    install_requires=[  # all we need to run the program
        'Flask==2.2.5',
        'pytest==8.3.3',
        'pytest-flask==1.2.0',
        'Flask-SQLAlchemy==3.0.5',
    ],
    entry_points={
        'console_scripts': [
            'customer=BurgerOrderer.app:main',   # First script: Calls the main() function in BurgerOrderer.app
            'kitchen=KitchenView.app:main',  # First script: Calls the main() function in KitchenView.app
        ],
    },
)
