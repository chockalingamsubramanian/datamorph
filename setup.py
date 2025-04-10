from setuptools import setup, find_packages

setup(
    name='pydatamorph',
    version='0.2',
    packages=find_packages(),
    install_requires=[],
    author='Chockalingam Subramanian',
    description='Adaptive LLM-native data pipeline orchestrator',
    entry_points={
        'console_scripts': [
            'datamorph=datamorph.core.runner:main'
        ]
    }
)
