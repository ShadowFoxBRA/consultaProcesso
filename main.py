from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

#Abrir Firefox
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

#Aguardar tempo e entrar na página de pesquisa do STJ
time.sleep(5)
url = 'https://processo.stj.jus.br/processo/pesquisa/?aplicacao=processos.ea'
driver.get(url)

#Webscrapping - Encontrar campo do número Unico do Processo
numeroUnico = driver.find_element(By.ID, "idNumeroUnico")

#Digitar número do processo
numeroUnico.send_keys('NUMERO DO PROCESSO!')
time.sleep(5)

#Encontrar botão para pesquisar
botaoConsulta = driver.find_element(By.ID,  'idBotaoPesquisarFormularioExtendido')

#Clicar no botão
botaoConsulta.click()


time.sleep(5)
driver.quit()
