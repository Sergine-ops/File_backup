from setuptools import setup

setup(
    name = 'file_backup_tool',
    version = '0.1',
    py_modules=['backup_tool'],
    install_requires=[
        'boto3',
    ],
    entry_points={
        'console_scripts':[
            'file_backup_tool = backup_tool:main',
        ]
    }
)