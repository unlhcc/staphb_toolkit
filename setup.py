from setuptools import setup, find_packages

setup(
    name="staphb_toolkit",
    version="1.0",
    url="https://staph-b.github.io/staphb_toolkit/",
    description="Python Toolkit for using containerized programs in either Singularity or Docker",
    packages=["staphb_toolkit.core","staphb_toolkit.lib","staphb_toolkit.workflows"],
    package_dir={"staphb_toolkit.core": "core", "staphb_toolkit.lib": "lib", "staphb_toolkit.workflows": "workflows" },
    license="GPLv3",
    scripts = [
        "staphb_toolkit",
        "staphb_toolkit_workflows"
    ],
    install_requires=[
    "spython>=0.0.73",
    "psutil>=5.6.3",
    "docker>=4.1.0"
    ],
    python_requires='>=3.7',
    zip_safe=False
)

