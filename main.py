class Atlas:

    def __init__(self):
        self.nome = "Atlas"
        self.versao = "0.0.1"

    def iniciar(self):
        print("=" * 35)
        print(f"{self.nome} iniciado")
        print(f"Versão: {self.versao}")
        print("Sistema funcionando corretamente.")
        print("=" * 35)


atlas = Atlas()
atlas.iniciar()