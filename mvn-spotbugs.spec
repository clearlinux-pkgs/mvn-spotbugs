#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-spotbugs
Version  : 3.1.9
Release  : 6
URL      : https://github.com/spotbugs/spotbugs/archive/3.1.9.tar.gz
Source0  : https://github.com/spotbugs/spotbugs/archive/3.1.9.tar.gz
Source1  : https://plugins.gradle.org/m2/gradle/plugin/com/github/spotbugs/spotbugs-gradle-plugin/1.6.9/spotbugs-gradle-plugin-1.6.9.jar
Source2  : https://plugins.gradle.org/m2/gradle/plugin/com/github/spotbugs/spotbugs-gradle-plugin/1.6.9/spotbugs-gradle-plugin-1.6.9.pom
Source3  : https://repo1.maven.org/maven2/com/github/spotbugs/spotbugs-annotations/3.1.9/spotbugs-annotations-3.1.9.jar
Source4  : https://repo1.maven.org/maven2/com/github/spotbugs/spotbugs-annotations/3.1.9/spotbugs-annotations-3.1.9.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : AML Apache-2.0 BSD-2-Clause BSD-3-Clause CC-BY-2.5 EPL-1.0 LGPL-2.1 MIT OLDAP-2.0
Requires: mvn-spotbugs-data = %{version}-%{release}
Requires: mvn-spotbugs-license = %{version}-%{release}
BuildRequires : apache-ant
BuildRequires : buildreq-mvn
BuildRequires : gradle

%description
Put the jar files for SpotBugs plugins in this directory.
For example, you can download the fb-contrib plugin from:
https://github.com/mebigfatguy/fb-contrib

%package data
Summary: data components for the mvn-spotbugs package.
Group: Data

%description data
data components for the mvn-spotbugs package.


%package license
Summary: license components for the mvn-spotbugs package.
Group: Default

%description license
license components for the mvn-spotbugs package.


%prep
%setup -q -n spotbugs-3.1.9

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-spotbugs
cp LICENSE %{buildroot}/usr/share/package-licenses/mvn-spotbugs/LICENSE
cp eclipsePlugin-test/LICENSE.txt %{buildroot}/usr/share/package-licenses/mvn-spotbugs/eclipsePlugin-test_LICENSE.txt
cp spotbugs/licenses/LICENSE-ASM.txt %{buildroot}/usr/share/package-licenses/mvn-spotbugs/spotbugs_licenses_LICENSE-ASM.txt
cp spotbugs/licenses/LICENSE-AppleJavaExtensions.txt %{buildroot}/usr/share/package-licenses/mvn-spotbugs/spotbugs_licenses_LICENSE-AppleJavaExtensions.txt
cp spotbugs/licenses/LICENSE-bcel.txt %{buildroot}/usr/share/package-licenses/mvn-spotbugs/spotbugs_licenses_LICENSE-bcel.txt
cp spotbugs/licenses/LICENSE-commons-lang.txt %{buildroot}/usr/share/package-licenses/mvn-spotbugs/spotbugs_licenses_LICENSE-commons-lang.txt
cp spotbugs/licenses/LICENSE-dom4j.txt %{buildroot}/usr/share/package-licenses/mvn-spotbugs/spotbugs_licenses_LICENSE-dom4j.txt
cp spotbugs/licenses/LICENSE-jaxen.txt %{buildroot}/usr/share/package-licenses/mvn-spotbugs/spotbugs_licenses_LICENSE-jaxen.txt
cp spotbugs/licenses/LICENSE-jcip.txt %{buildroot}/usr/share/package-licenses/mvn-spotbugs/spotbugs_licenses_LICENSE-jcip.txt
cp spotbugs/licenses/LICENSE-jsr305.txt %{buildroot}/usr/share/package-licenses/mvn-spotbugs/spotbugs_licenses_LICENSE-jsr305.txt
cp spotbugs/licenses/LICENSE-logback.txt %{buildroot}/usr/share/package-licenses/mvn-spotbugs/spotbugs_licenses_LICENSE-logback.txt
cp spotbugs/licenses/LICENSE-slf4j.txt %{buildroot}/usr/share/package-licenses/mvn-spotbugs/spotbugs_licenses_LICENSE-slf4j.txt
cp spotbugs/licenses/LICENSE.txt %{buildroot}/usr/share/package-licenses/mvn-spotbugs/spotbugs_licenses_LICENSE.txt
cp spotbugs/src/gui/edu/umd/cs/findbugs/gui2/help/License.html %{buildroot}/usr/share/package-licenses/mvn-spotbugs/spotbugs_src_gui_edu_umd_cs_findbugs_gui2_help_License.html
cp spotbugs/src/main/java/edu/umd/cs/findbugs/gui/help/License.html %{buildroot}/usr/share/package-licenses/mvn-spotbugs/spotbugs_src_main_java_edu_umd_cs_findbugs_gui_help_License.html
mkdir -p %{buildroot}/usr/share/java/.m2/repository/gradle/plugin/com/github/spotbugs/spotbugs-gradle-plugin/1.6.9
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/gradle/plugin/com/github/spotbugs/spotbugs-gradle-plugin/1.6.9/spotbugs-gradle-plugin-1.6.9.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/gradle/plugin/com/github/spotbugs/spotbugs-gradle-plugin/1.6.9
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/gradle/plugin/com/github/spotbugs/spotbugs-gradle-plugin/1.6.9/spotbugs-gradle-plugin-1.6.9.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/github/spotbugs/spotbugs-annotations/3.1.9
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/com/github/spotbugs/spotbugs-annotations/3.1.9/spotbugs-annotations-3.1.9.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/github/spotbugs/spotbugs-annotations/3.1.9
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/com/github/spotbugs/spotbugs-annotations/3.1.9/spotbugs-annotations-3.1.9.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/com/github/spotbugs/spotbugs-annotations/3.1.9/spotbugs-annotations-3.1.9.jar
/usr/share/java/.m2/repository/com/github/spotbugs/spotbugs-annotations/3.1.9/spotbugs-annotations-3.1.9.pom
/usr/share/java/.m2/repository/gradle/plugin/com/github/spotbugs/spotbugs-gradle-plugin/1.6.9/spotbugs-gradle-plugin-1.6.9.jar
/usr/share/java/.m2/repository/gradle/plugin/com/github/spotbugs/spotbugs-gradle-plugin/1.6.9/spotbugs-gradle-plugin-1.6.9.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-spotbugs/LICENSE
/usr/share/package-licenses/mvn-spotbugs/eclipsePlugin-test_LICENSE.txt
/usr/share/package-licenses/mvn-spotbugs/spotbugs_licenses_LICENSE-ASM.txt
/usr/share/package-licenses/mvn-spotbugs/spotbugs_licenses_LICENSE-AppleJavaExtensions.txt
/usr/share/package-licenses/mvn-spotbugs/spotbugs_licenses_LICENSE-bcel.txt
/usr/share/package-licenses/mvn-spotbugs/spotbugs_licenses_LICENSE-commons-lang.txt
/usr/share/package-licenses/mvn-spotbugs/spotbugs_licenses_LICENSE-dom4j.txt
/usr/share/package-licenses/mvn-spotbugs/spotbugs_licenses_LICENSE-jaxen.txt
/usr/share/package-licenses/mvn-spotbugs/spotbugs_licenses_LICENSE-jcip.txt
/usr/share/package-licenses/mvn-spotbugs/spotbugs_licenses_LICENSE-jsr305.txt
/usr/share/package-licenses/mvn-spotbugs/spotbugs_licenses_LICENSE-logback.txt
/usr/share/package-licenses/mvn-spotbugs/spotbugs_licenses_LICENSE-slf4j.txt
/usr/share/package-licenses/mvn-spotbugs/spotbugs_licenses_LICENSE.txt
/usr/share/package-licenses/mvn-spotbugs/spotbugs_src_gui_edu_umd_cs_findbugs_gui2_help_License.html
/usr/share/package-licenses/mvn-spotbugs/spotbugs_src_main_java_edu_umd_cs_findbugs_gui_help_License.html
