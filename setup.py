from setuptools import setup, find_packages

setup(
    name='pydatamorph',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "streamlit>=1.0"
    ],
    author='Chockalingam Subramanian',
    description='Adaptive LLM-native data pipeline orchestrator',
    entry_points={
        'console_scripts': [
            'datamorph=datamorph.core.runner:main'
        ]
    },
    python_requires='>=3.7',
)
