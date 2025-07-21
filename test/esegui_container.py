import docker

def run_programma(programma: str):
    client = docker.from_env()

    print(f"Esecuzione di '{programma}' nel container...")

    try:
        output = client.containers.run(
            image="first_docker-programma_a",  # Assicurati che questa immagine esista
            command=f"python entrypoints/run.py {programma}",
            remove=True,
            tty=True
        )
        print(output.decode())
    except docker.errors.ImageNotFound:
        print("Errore: immagine Docker non trovata. Assicurati di averla costruita con 'docker build .'")
    except docker.errors.ContainerError as e:
        print(f"Errore durante l'esecuzione del container: {e}")
    except Exception as e:
        print(f"Errore generico: {e}")

if __name__ == "__main__":
    # Puoi cambiare qui il programma da eseguire
    run_programma("programma_a")
