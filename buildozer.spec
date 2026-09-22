[app]
title = Gestión de Estudiantes
package.name = estudiantes
package.domain = org.colegio
source.dir = .
source.include_exts = py,kv,json,png,jpg
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

[app:android]
android.api = 35
android.minapi = 23
android.archs = arm64-v8a
