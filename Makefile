PKG_NAME := mvn-spotbugs
URL = https://github.com/spotbugs/spotbugs/archive/3.1.9.tar.gz
ARCHIVES = https://repo1.maven.org/maven2/com/github/spotbugs/spotbugs-annotations/3.1.9/spotbugs-annotations-3.1.9.jar : https://repo1.maven.org/maven2/com/github/spotbugs/spotbugs-annotations/3.1.9/spotbugs-annotations-3.1.9.pom : https://plugins.gradle.org/m2/gradle/plugin/com/github/spotbugs/spotbugs-gradle-plugin/1.6.9/spotbugs-gradle-plugin-1.6.9.jar : https://plugins.gradle.org/m2/gradle/plugin/com/github/spotbugs/spotbugs-gradle-plugin/1.6.9/spotbugs-gradle-plugin-1.6.9.pom : 

include ../common/Makefile.common
