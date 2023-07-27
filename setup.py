from setuptools import setup, find_packages

setup(
    name="analyze-dbt-models",
    version="0.1.0",
    description="Meltano project file bundle of Matatika artifacts for analysis of your dbt models ",
    packages=find_packages(),
    package_data={
        "bundle": [
            "analyze/channels/*.yml",
            "pipelines/*.yml",
        ]
    },
)
