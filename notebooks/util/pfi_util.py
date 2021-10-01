import sys
import os
import copy
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm # für colormaps
from cycler import cycler

# save for later restoring
default_cycler = plt.rcParams['axes.prop_cycle']


# Die Existenz oder nicht-Existenz einer der Datei `author_repo.md`
# legt den AUTHOR_MODE fest (`True` oder `False`)

util_path = os.path.dirname(os.path.abspath(sys.modules.get(__name__).__file__))
p = os.path.abspath(os.path.join(util_path, "..", "..", "orga", "author_repo.md"))
AUTHOR_MODE = os.path.isfile(p)
#print(util_path, p, "AUTHOR_MODE", AUTHOR_MODE)


def show_book(figname, saveandshow=True, printflag=False, gs_convert=True, png=False, **kwargs):
    """
    Diese Funktion dient dazu Abbildungen, in einer Farb- und ggf. in einer SW-Version abzuspeichern
    """
    if printflag:
        # Diese Funktionalität ist vom Verlag nicht gewünscht.
        print(r"Siehe Abbildung §\ref{fig_XXX}§".replace("XXX", figname))
    if saveandshow:

        if png:
            suffix = "png"
            conv_func = convert_png_to_grayscale
        else:
            suffix = "pdf"
            conv_func = convert_pdf_to_grayscale

        if gs_convert:
            if AUTHOR_MODE:
                fname1 = f"{figname}_color_snip.{suffix}"
                fname2 = f"{figname}_snip.{suffix}"
                plt.savefig(fname1, **kwargs)

                conv_func(fname1, fname2)

            else:
                print("Graustufen-Konvertierung nicht möglich.")
                # notwendiges Skript ist nur für Autoren empfohlen (getestet).
                plt.savefig(f"{figname}_snip.{suffix}", **kwargs)
        else:
            # Keine Graustufenkonvertierung erforderlich
            plt.savefig(f"{figname}_snip.{suffix}", **kwargs)

        plt.show()


def convert_pdf_to_grayscale(fname1, fname2):

    cmd = f"""gs \
        -sOutputFile=output.pdf \
        -sDEVICE=pdfwrite \
        -sColorConversionStrategy=Gray \
        -dProcessColorModel=/DeviceGray \
        -dCompatibilityLevel=1.4 \
        -dNOPAUSE \
        -dBATCH \
        {fname1}"""

    os.system(cmd)
    os.system(f"mv output.pdf {fname2}")

def convert_png_to_grayscale(fname1, fname2):

    cmd = f"convert {fname1} -colorspace Gray output.png"

    os.system(cmd)
    os.system(f"mv output.png {fname2}")


def define_plot_params(plt):

    plt.rcParams['text.usetex'] = True
    plt.rcParams['font.size'] = 14
    plt.rcParams['legend.fontsize'] = 18

    plt.rcParams['figure.subplot.left'] = .13

    set_cmap_cycler(N=3)

    # Bisherige Plot-Einstellungen speichern (echte Kopie anlegen)
    orig_plt_rcParams = copy.deepcopy(plt.rcParams)

    # Plot-Einstellungen anpassen für zwei Grafiken nebeneinander
    plt.rcParams['font.size'] = 18

    plt.rcParams['figure.subplot.bottom'] = .265
    plt.rcParams['figure.subplot.left'] = .09
    plt.rcParams['figure.subplot.top'] = .995
    plt.rcParams['figure.subplot.right'] = .995

    plt.rcParams['figure.subplot.hspace'] = .3 # horizontalen Abstand anpassen

    double_plt_rcParams = copy.deepcopy(plt.rcParams)

    # auf originale Parameter setzen:
    plt.rcParams.update(orig_plt_rcParams)

    return orig_plt_rcParams, double_plt_rcParams


def define_plot_params_rh(plt):
    plt.rcParams['text.usetex'] = True
    #plt.rcParams['font.size'] = 12
    #plt.rcParams['legend.fontsize'] = 12

    set_cmap_cycler(N=3)


def set_cmap_cycler(N=2, start=0, end=0.9, cmap=matplotlib.cm.plasma, values=None):

    """
    Set the thefault colors to those of a colormap divided into N steps.
    plasma in [0, 0.9] is default
    """

    if values is None:
        values = np.linspace(start, end, N)

    assert isinstance(values, (list, tuple, np.ndarray))

    cyc = cycler(color=[cmap(v) for v in values])
    plt.rcParams['axes.prop_cycle'] = cyc

