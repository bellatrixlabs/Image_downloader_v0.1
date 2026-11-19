import requests 
from bs4 import BeautifulSoup 
from loguru import logger 
from rich import print 
import random
from rich.console import Console 


imagens_baixadas = 0


console = Console()


n_a = random.randint(0,100000000667654470000)


console.print("[bold]Image Downloader\n")
print(f"Downloads feitos hoje: {imagens_baixadas}\n")

pasta = "/sdcard/"



while True:
    link = input("Digite um link: ")
    print("\n")
    
    resultado = requests.get(link)
    soup = BeautifulSoup(resultado.text, "html.parser")
    
    if resultado.status_code == 200:
        console.print("Iniciando download...\n")
        image_downloader = open(pasta + f"Imagem{n_a}.jpg", "wb")
        image_downloader.write(resultado.content)
        imagens_baixadas = imagens_baixadas + 1
        console.print(f"[green]>>> Imagem salva com sucesso\n")
        
        print(type(resultado))
        print("\n")
        print(f"Downloads feitos hoje: {imagens_baixadas}\n")

    else:
        console.print("[red] Falha ao acessar site.\n")
        
        
