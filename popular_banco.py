import os
import django
import requests

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
django.setup()

try:
    from cars.models import Brand, City 
except ImportError:
    print("ERRO: Não encontrei os models 'Brand' ou 'City'.")
    exit()

def cadastrar_marcas():
    print("🏎️  Iniciando cadastro de marcas...")
    marcas = [
        "Chevrolet", "Volkswagen", "Fiat", "Toyota", "Hyundai", "Ford", "Honda", 
        "Renault", "Nissan", "Jeep", "Caoa Chery", "Mitsubishi", "Peugeot", 
        "Citroën", "BMW", "Mercedes-Benz", "Audi", "Kia", "Volvo", "Land Rover", 
        "Suzuki", "RAM", "Porsche", "Mini", "JAC", "BYD", "GWM", "Subaru", 
        "Troller", "Lexus", "Jaguar", "Ferrari", "Lamborghini", "Dodge"
    ]
    
    contador = 0
    for nome in marcas:
        obj, created = Brand.objects.get_or_create(name=nome)
        if created:
            contador += 1
            
    print(f"✅ {contador} novas marcas cadastradas!")

def cadastrar_cidades():
    print("\n🌍 Baixando cidades do IBGE...")
    
    url = "https://servicodados.ibge.gov.br/api/v1/localidades/municipios"
    
    try:
        response = requests.get(url)
        cidades = response.json()
    except Exception as e:
        print(f"❌ Erro de conexão: {e}")
        return

    total_api = len(cidades)
    criadas = 0
    
    print(f"📥 Processando {total_api} cidades...")

    for i, item in enumerate(cidades):
        try:
            nome_cidade = item['nome']
            
            try:
                uf = item['microrregiao']['mesorregiao']['UF']['sigla']
            except (KeyError, TypeError):
                try:
                    uf = item['microrregiao']['UF']['sigla']
                except:
                    print(f"⚠️  Pulei: {nome_cidade} (Dados incompletos na API)")
                    continue
            
            # Formata o nome: "Campo Grande - MS"
            nome_completo = f"{nome_cidade} - {uf}"
            
            obj, created = City.objects.get_or_create(name=nome_completo)
            
            if created:
                criadas += 1
        
        except Exception as e:
            print(f"Erro ao salvar {item.get('nome', 'Desconhecida')}: {e}")
            continue

        # Mostra progresso a cada 1000 cidades
        if i % 1000 == 0 and i > 0:
            print(f"   ... processadas {i} cidades")

    print(f"✅ Finalizado! {criadas} novas cidades inseridas.")

if __name__ == "__main__":
    cadastrar_marcas()
    cadastrar_cidades()