import info

from Blueprints.CraftPackageObject import CraftPackageObject
from CraftCore import CraftCore


class subinfo(info.infoclass):

    def setTargets(self):
        self.versionInfo.setDefaultValues(gitUrl="https://github.com/alcarazzam/chessament.git")

        self.displayName = "Chessament"
        self.description = "Chess tournament manager"
        self.webpage = "https://chessament.alcarazzam.dev"

    def setDependencies( self ):
        self.runtimeDependencies["virtual/base"] = None
        self.runtimeDependencies["libs/qt/qtbase"] = None
        self.runtimeDependencies["libs/qt/qtdeclarative"] = None
        self.runtimeDependencies["kde/frameworks/tier1/kirigami"] = None
        self.runtimeDependencies["kde/frameworks/tier1/kcoreaddons"] = None
        self.runtimeDependencies["kde/frameworks/tier1/kconfig"] = None
        self.runtimeDependencies["kde/frameworks/tier1/ki18n"] = None
        self.runtimeDependencies["kde/frameworks/tier1/kitemmodels"] = None

        self.runtimeDependencies["qt-libs/qcoro"] = None

        self.runtimeDependencies["kde/unreleased/kirigami-addons"] = None
        self.runtimeDependencies["kde/frameworks/tier1/breeze-icons"] = None
        self.runtimeDependencies["kde/frameworks/tier3/qqc2-desktop-style"] = None
        self.runtimeDependencies["kde/plasma/breeze"] = None

        if CraftCore.compiler.isMinGW():
            self.runtimeDependencies["libs/runtime"] = None #mingw-based builds need this


class Package(CraftPackageObject.get("kde").pattern):

    def __init__( self ):
        super().__init__()
        self.subinfo.options.dynamic.buildTests = False

    def createPackage(self):
        self.addExecutableFilter(r"(bin|libexec)/(?!(chessament|update-mime-database)).*")

        if not CraftCore.compiler.isLinux:
            self.ignoredPackages.append("libs/dbus")

        return super().createPackage()

