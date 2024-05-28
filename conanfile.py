from conan import ConanFile

class MoxPPRecipe(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "PremakeDeps"

    def requirements(self):
        self.requires("boost/1.85.0")

    def configure(self):
        # This only works on windows (we added this so that you can see
        # how to change settings of packages)
        # self.options["spdlog"].wchar_support = True
    	self.options['boost'].without_fiber = False
