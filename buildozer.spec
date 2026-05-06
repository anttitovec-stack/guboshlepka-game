[app]

# Название (латиницей)
title = Guboshlepka

# Имя пакета
package.name = guboshlepka
package.domain = org.test

# Версия
version = 0.1

# Исходники
source.dir = .
source.include_exts = py,png,jpg,jpeg,wav,ttf

# Зависимости
requirements = python3,kivy,plyer

# Архитектуры
android.arch = armeabi-v7a, arm64-v8a

# Разрешения
android.permissions = VIBRATE

# Ориентация (вертикальная)
orientation = portrait

# Принять лицензию SDK
android.accept_sdk_license = True

# Стабильная версия Python для сборки
p4a.python_version = 3.11

# Ветка python-for-android (самые свежие исправления)
p4a.branch = develop

# Фиксируем совместимые версии Gradle
p4a.gradle_version = 8.4
android.gradle_dependencies = com.android.tools.build:gradle:8.1.0
