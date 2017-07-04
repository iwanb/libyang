from setuptools import setup, Extension

libyang = Extension('libyang._libyangpyc',
                    sources = ['src/libyangpycPYTHON_wrap.cxx'],
                    undef_macros=['NDEBUG'],
                    libraries = ['pcre', 'yang'])

setup(
    name='libyang',
    version="1.0",
    include_package_data=True,
    description='Bindings for the libyang library',
    url='https://github.com/CESNET/libyang',
    author='Iwan Briquemont',
    author_email='iwan.briquemont@nokia.com',
    ext_modules = [libyang],
    test_suite = "test"
)
