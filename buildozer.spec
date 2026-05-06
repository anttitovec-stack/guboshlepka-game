[app]
title = Guboshlepka
package.name = guboshlepka
package.domain = org.test
version = 0.1
source.dir = .
source.include_exts = py,png,jpg,jpeg,wav,ttf
requirements = python3,kivy,plyer
android.arch = armeabi-v7a, arm64-v8a
android.permissions = VIBRATE
orientation = portrait
android.accept_sdk_license = True
p4a.branch = develop
p4a.python_version = 3.11
android.gradle_dependencies = com.android.tools.build:gradle:8.1.0
android.gradle_args = --no-daemon --stacktrace
