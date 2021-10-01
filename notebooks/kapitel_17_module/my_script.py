import argparse
# Initialisiere Parser
parser = argparse.ArgumentParser(
    description="Lädt Datei und führt Berechnung aus")
# Definiere Argumente
parser.add_argument('path', help="Dateipfad")  # Pflichtargument
# Optionale Flag
parser.add_argument('--save', '-s', action='store_true',
                    help="Ergebnis abspeichern")
args = parser.parse_args()  # Parse Kommandozeilenparameter
# Werte sind jetzt in args.path (string) und
# args.save (boolean) verfügbar
print(f"path: {args.path}")
print(f"save: {args.save}")