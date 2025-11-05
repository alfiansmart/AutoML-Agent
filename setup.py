"""
Setup script for AutoML Agent with Azure OpenAI
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="automl-agent-azure",
    version="0.1.0",
    author="AutoML Agent Contributors",
    description="AutoML Agent implementation with Azure OpenAI GPT-4-mini and o3-mini support",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alfiansmart/AutoML-Agent",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: Other/Proprietary License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.11",
    install_requires=requirements,
    include_package_data=True,
    package_data={
        "prompt_agent": ["WizardLAMP/*.json"],
    },
)
