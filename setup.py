import setuptools

exec(open("modulesbuilder/version.py").read())
mb_version = __version__

setuptools.setup(
        version = mb_version
 )
