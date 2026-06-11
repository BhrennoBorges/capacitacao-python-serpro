import logging

# Configuração que direciona os avisos do código para um arquivo físico
logging.basicConfig(filename='execucao.log', level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Início do processo de cálculo da rede.")

def calcular_subredes(quantidade):
    logging.debug(f"A função recebeu o valor: {quantidade}")
    if quantidade < 0:
        logging.error("O valor informado não pode ser negativo.")
        return 0
    
    resultado = quantidade * 256
    logging.debug(f"Cálculo concluído. Resultado: {resultado}")
    return resultado

print("Processando... verifique o arquivo execucao.log para detalhes técnicos.")
calcular_subredes(5)
calcular_subredes(-2)

logging.info("Processo finalizado.")