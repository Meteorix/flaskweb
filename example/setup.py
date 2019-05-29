# coding=utf-8
# Created by Meteorix at 2019/4/16
from setuptools import setup
from setuptools.extension import Extension
from setuptools.command.build_py import build_py
from Cython.Build import cythonize
from Cython.Distutils import build_ext
from pathlib import Path
from glob import glob
import os
import sys


package_name = "example"
packages = [package_name,]
extensions = []
cythonizing = True

if "sdist" in sys.argv:
    cythonizing = False


if cythonizing:
    print("cythonize...")
    for p in packages:
        for filepath in Path(p).glob("**/*.py"):
            filepath = filepath.as_posix()
            modname = os.path.splitext(filepath)[0].replace("/", ".")
            # cythonize cannot deal with __init__.py
            if not modname.endswith("__init__"):
                ext = Extension(modname, [filepath])
                extensions.append(ext)
    print(extensions)


class my_build_py(build_py):
    def find_package_modules(self, package, package_dir):
        modules = super().find_package_modules(package, package_dir)
        if cythonizing:
            # only copy all __init__.py
            modules = [m for m in modules if m[-1].endswith("__init__.py")]
        return modules


setup(
    name='example',
    version='0.0.2',
    author='meteorix',
    author_email='lxhustauto@gmail.com',
    description='Example web app built with flaskweb',
    install_requires=['flaskweb'],
    ext_modules=cythonize(
        extensions,
        build_dir="build",
        compiler_directives=dict(
            always_allow_keywords=True,
            language_level=3,
        ),
    ),
    packages=packages,
    package_data={
        package_name: ['static/*/*', 'templates/*', 'specs/*']
    },
    cmdclass=dict(
        build_ext=build_ext,
        build_py=my_build_py,
    )
)
