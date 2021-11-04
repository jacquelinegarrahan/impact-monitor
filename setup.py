from setuptools import setup, find_packages
from os import path
import versioneer

cur_dir = path.abspath(path.dirname(__file__))

# parse requirements
with open(path.join(cur_dir, "requirements.txt"), "r") as f:
    requirements = f.read().split()

setup(
    name="impact-monitor",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    packages=find_packages(),
    author='SLAC National Accelerator Laboratory',
    author_email="jgarra@slac.stanford.edu",
    license="SLAC Open",
    install_requires=requirements,
    url="https://github.com/jacquelinegarrahan/impact-monitor",
    include_package_data=True,
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
        "start-monitor=impact_monitor.monitor:main",
        "import-docs=impact_monitor.startup:main"
        ]
    },
)