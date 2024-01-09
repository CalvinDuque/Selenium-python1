# O assert sempre verifica se o retorno da condição é true
assert True

# Assert numbers
num_esperado = 2
num_obtido = 1
assert num_esperado > num_obtido, f"Esperado '{num_esperado}'. não é maior que o numero Atual '{num_obtido}'. "

# Assert text
text_esperado = "Selenium Webdriver"
text_obtido = "Selenium Webdriver"
assert text_esperado == text_obtido, f"Esperado '{text_esperado}'. não é igual ao texto atual '{text_obtido}'."

# Assert text in // string se tiver uma parte do texto esperado dentro do texto obito é true / pode ir in que esta dentro, ou not in que nao esta dentro
text_esperado = "Selenium222"
text_obtido = "Selenium Webdriver"
assert text_esperado not in text_obtido, f"Esperado '{text_esperado}'. dentro da string atual '{text_obtido}'."

# Assert is_displayed/is_enabled/is-selected 
#exemplo esta dentro do arquivo comandos interacao com elementos, ultimo codigo


