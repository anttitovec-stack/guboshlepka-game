[app]

title = Guboshlepka

package.name = guboshlepka
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf,wav,mp3,ogg,json,txt
source.include_patterns = images/,images/filler/,images/natural/,images/ui/,sounds/*

version = 0.1

requirements = python3,kivy

orientation = portrait
fullscreen = 1

icon.filename = icon.png
presplash.filename = icon.png

osx.python_version = 3
osx.kivy_version = 2.3.0

android.permissions = INTERNET
android.api = 31
android.minapi = 21
android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

[buildozer]

log_level = 2
warn_on_root = 1
