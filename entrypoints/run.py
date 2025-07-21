import os
import sys

# Aggiungi la directory 'src/' al path
SRC_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
if SRC_PATH not in sys.path:
    sys.path.insert(0, SRC_PATH)


def main():
    if len(sys.argv) < 2:
        print("Errore: specificare il nome del programma da eseguire (es. programma_a)")
        sys.exit(1)

    program_name = sys.argv[1]

    try:
        mod = __import__(program_name)
        mod.main()
    except ImportError:
        print(f"Errore: modulo '{program_name}' non trovato.")
        sys.exit(1)
    except AttributeError:
        print(f"Errore: il modulo '{program_name}' non ha una funzione 'main()'.")
        sys.exit(1)


if __name__ == "__main__":
    main()
