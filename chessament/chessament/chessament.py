import info

from Blueprints.CraftPackageObject import CraftPackageObject
from CraftCore import CraftCore


class subinfo(info.infoclass):
    def setTargets(self):
        self.displayName = "Chessament"
        self.description = "Chess tournament manager"
        self.webpage = "https://chessament.alcarazzam.dev"

        self.svnTargets["master"] = "https://github.com/alcarazzam/chessament.git"
        self.defaultTarget = "master"

    def setDependencies(self):
        self.buildDependencies["libs/qt/qttools"] = None

        self.runtimeDependencies["virtual/base"] = None
        self.runtimeDependencies["libs/qt/qtbase"] = None
        self.runtimeDependencies["libs/qt/qtdeclarative"] = None
        self.runtimeDependencies["libs/qt/qtwebengine"] = None

        self.runtimeDependencies["kde/frameworks/tier1/kirigami"] = None
        self.runtimeDependencies["kde/frameworks/tier1/kconfig"] = None
        self.runtimeDependencies["kde/frameworks/tier2/kcolorscheme"] = None
        self.runtimeDependencies["kde/frameworks/tier1/kcoreaddons"] = None
        self.runtimeDependencies["kde/frameworks/tier1/ki18n"] = None
        self.runtimeDependencies["kde/frameworks/tier1/kitemmodels"] = None

        self.runtimeDependencies["qt-libs/qcoro"] = None

        self.runtimeDependencies["kde/unreleased/kirigami-addons"] = None
        self.runtimeDependencies["kde/frameworks/tier1/breeze-icons"] = None
        self.runtimeDependencies["kde/frameworks/tier3/qqc2-desktop-style"] = None
        self.runtimeDependencies["kde/plasma/breeze"] = None

        if CraftCore.compiler.isMinGW():
            self.runtimeDependencies["libs/runtime"] = (
                None  # mingw-based builds need this
            )


class Package(CraftPackageObject.get("kde").pattern):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.subinfo.options.dynamic.buildTests = False

    def createPackage(self):
        self.blacklist_file.append(self.blueprintDir() / "blocklist.txt")

        self.addExecutableFilter(
            r"(bin|libexec)/(?!(chessament|QtWebEngineProcess|update-mime-database)).*"
        )
        self.ignoredPackages.append("binary/mysql")

        if not CraftCore.compiler.isLinux:
            self.ignoredPackages.append("libs/dbus")

        return super().createPackage()
