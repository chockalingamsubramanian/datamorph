from setuptools import setup, find_packages

setup(
    name='pydatamorph',
    version='1.1.2',
    #packages=find_packages(),
    packages=['datamorph','datamorph.core','datamorph.ui','datamorph.config','datamorph.llm','datamorph.steps','datamorph.utils'],
    include_package_data=True,
    install_requires=[
        "streamlit>=1.0",
        "pyyaml>=6.0",
        "python-dotenv>=1.1.0"
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

