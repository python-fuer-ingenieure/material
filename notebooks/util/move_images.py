# Dieses Skript kopiert oder verlinkt alle Grafik-Dateien aus code/kap*/ nach latex/figs

# Aufruf im Verzeichnis code/util


import sys
import os

if "move" in sys.argv:
    mode = "move"
else:
    mode = "link"


if "figs" in sys.argv:
    target = "figs"
else:
    target = "figs2"




startpath = os.path.abspath("./")
os.chdir("..")
rootdir = './'


def is_image(fname):
    fname = fname.lower()
    return fname.endswith("pdf") or fname.endswith("png")

for subdir, dirs, files in os.walk(rootdir):
    for fname in files:
        if not is_image(fname):
            continue
        p = os.path.join(subdir, fname)

        if mode == "move":
            cmd = f"mv {p} ../latex/{target}/{fname}"
        else:
            cmd = f"ln -f -s ../../code/{p} ../latex/{target}/{fname}"

        print(cmd)
        os.system(cmd)

os.chdir(startpath)
