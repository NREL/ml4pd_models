from setuptools import setup, find_packages
import pathlib
from datetime import date

here = pathlib.Path(__file__).parent.resolve()
today = date.today().strftime(r"%Y.%m.%d")

setup(
    name="ml4pd_models",
    version=today,
    maintainer="Hien Vo",
    maintainer_email="hvo@nrel.gov",
    description="A library of ML models for ML4PD.",
    packages=find_packages(),
    python_requires=">=3.8",
    include_package_data=True,
)
