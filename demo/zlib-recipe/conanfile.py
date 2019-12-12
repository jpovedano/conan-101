from conans import ConanFile, AutoToolsBuildEnvironment
from conans import tools


class ZlibConan(ConanFile):
    name = "zlib"
    version = "1.2.11"
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Foo here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def source(self):
        # Download the source code.
        # It will be extracted to zlib-1.2.11
        tools.get("http://zlib.net/zlib-1.2.11.tar.gz")

    def build(self):
        # ZLib is based on autotools, so we use the autotools helper
        autotools = AutoToolsBuildEnvironment(self)
        autotools.configure(configure_dir="zlib-1.2.11")
        autotools.make()
        autotools.install() # make install

    def package_info(self):
        self.cpp_info.libs = ["z"]
