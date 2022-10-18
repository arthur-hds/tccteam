from cardspython import *

def returnVcf(VcfPath):
    try:
        users = open_file(VcfPath)
        Vcf = Pyvcard(users)
        Vcf.read_vcard()
        lista_contatos_vcf = Vcf.get_contacts_vcard()
        return lista_contatos_vcf
    except:
        return 'ARQUIVO VCF ESTÁ COM PROBLEMA'
# contatos = []

# print(returnVcf(r'C:\Users\Usuario\Downloads\joilsonContatos.vcf'))
#     contatos.append(i)
# print(sorted(contatos))



