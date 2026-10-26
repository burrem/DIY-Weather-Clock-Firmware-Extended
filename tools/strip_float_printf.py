# PlatformIO post-script: drop the "-u _printf_float -u _scanf_float" linker flags
# that the ESP8266 Arduino builder adds by default. The firmware never formats or
# parses floats through printf/scanf (Print and String use the core's own
# dtostrf, String::toFloat uses atof), so forcing them in only costs ~4 KB of
# flash, which matters with the OTA image limit of ~512 KB.
Import("env")

flags = list(env["LINKFLAGS"])
stripped = []
i = 0
while i < len(flags):
    if flags[i] == "-u" and i + 1 < len(flags) and flags[i + 1] in ("_printf_float", "_scanf_float"):
        i += 2
        continue
    stripped.append(flags[i])
    i += 1
env.Replace(LINKFLAGS=stripped)
