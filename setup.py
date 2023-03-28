from setuptools import setup, find_packages

setup(
    name='plot_solution',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'plotly'
    ],
    entry_points={
        'console_scripts': [
            'plot_solution=plot_solution.main:main',
            'python plot_solution=plot_solution.main:main'
        ]
    }
)
