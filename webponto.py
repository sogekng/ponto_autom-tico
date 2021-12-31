from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import readme
from time import sleep


nav = webdriver.Chrome(ChromeDriverManager().install())

nav.get('https://webponto.resource.com.br/')


codEmpresa = nav.find_element_by_name('CodEmpresa').send_keys(readme.codempresa)
codUsuario = nav.find_element_by_name('requiredusuario').send_keys(readme.codusuario)
campoSenha = nav.find_element_by_name('requiredsenha').send_keys(readme.senha)

submit = nav.find_element_by_name('Submit').click()

sleep(1)

nav.get('https://webponto.resource.com.br/just_user/IncluirMarcacaoOnLine.asp')

submit = nav.find_element_by_name('Submit').click()

sleep(1)

nav.quit()
