from setuptools import setup, find_packages

setup(
    name="staphb_toolkit",
    version="1.0",
    license="GPLv3",
    url="https://staph-b.github.io/staphb_toolkit/",
    description="Python Toolkit for using containerized programs in either Singularity or Docker",
    packages=[
        "staphb_toolkit.core",
        "staphb_toolkit.lib",
        "staphb_toolkit.workflows",
        "staphb_toolkit.workflows.dryad",
        "staphb_toolkit.workflows.dryad.app",
        "staphb_toolkit.workflows.foushee",
        "staphb_toolkit.workflows.tredegar",
        ],
    package_dir={
        "staphb_toolkit.core": "core",
        "staphb_toolkit.lib": "lib",
        "staphb_toolkit.workflows": "workflows" },
    package_data={
        "staphb_toolkit.workflows.foushee": ["foushee_config.json"],
        "staphb_toolkit.workflows.tredegar": ["tredegar_config.json"],
        "staphb_toolkit.core": ["docker_config.json"],
    },
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

