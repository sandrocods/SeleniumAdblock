from setuptools import setup

setup(
    name='SeleniumAdblock',
    version='1',
    packages=['SeleniumAdblock'],
    url='sandroputraa.com',
    license='',
    author='sandroputraa',
    author_email='krisandromartinus@gmail.com',
    description='Easy Package to disable all ads on your selenium automation',
    install_requires=[
        'selenium',
    ],
    keywords="selenium adblock adblocker adblocker selenium",
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'SeleniumAdblock = SeleniumAdblock.SeleniumAdblock:main',
        ],
    },
    package_data={
        'SeleniumAdblock': ['AdBlock-best-ad-blocker.crx', 'Popup-Blocker-strict.crx', 'Ultimate-Ad-Blocker.crx'],
    },
)
