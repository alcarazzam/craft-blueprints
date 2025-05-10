import info

from Blueprints.CraftPackageObject import CraftPackageObject
from CraftCore import CraftCore


class subinfo(info.infoclass):
    def setTargets(self):
        self.versionInfo.setDefaultValues(gitUrl="https://invent.kde.org/games/chessament.git")

        self.displayName = "Chessament"
        self.description = "Chess tournament manager"

    def setDependencies(self):
        self.buildDependencies["libs/qt/qttools"] = None

        self.runtimeDependencies["virtual/base"] = None
        self.runtimeDependencies["libs/qt/qtbase"] = None
        self.runtimeDependencies["libs/qt/qtdeclarative"] = None
        self.runtimeDependencies["libs/qt/qtnetworkauth"] = None
        self.runtimeDependencies["libs/qt/qtwebengine"] = None

        self.runtimeDependencies["kde/frameworks/tier1/kirigami"] = None
        self.runtimeDependencies["kde/frameworks/tier1/kconfig"] = None
        self.runtimeDependencies["kde/frameworks/tier2/kcolorscheme"] = None
        self.runtimeDependencies["kde/frameworks/tier1/kcoreaddons"] = None
        self.runtimeDependencies["kde/frameworks/tier1/ki18n"] = None
        self.runtimeDependencies["kde/frameworks/tier3/kiconthemes"] = None
        self.runtimeDependencies["kde/frameworks/tier1/kitemmodels"] = None

        self.runtimeDependencies["qt-libs/qcoro"] = None
        self.runtimeDependencies["qt-libs/qtkeychain"] = None

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

        self.defines["company"] = "alcarazzam.dev"
        self.defines["shortcuts"] = [
            {
                "name": "Chessament",
                "target": "bin/chessament.exe",
                "appId": "chessament",
                "icon": self.buildDir() / "src/CHESSAMENT_ICON.ico",
            }
        ]
        self.defines["icon"] = self.buildDir() / "src/CHESSAMENT_ICON.ico"

        self.addExecutableFilter(
            r"(bin|libexec)/(?!(chessament|QtWebEngineProcess|update-mime-database|snoretoast)).*"
        )
        self.ignoredPackages.append("binary/mysql")

        if not CraftCore.compiler.isLinux:
            self.ignoredPackages.append("libs/dbus")

        return super().createPackage()
