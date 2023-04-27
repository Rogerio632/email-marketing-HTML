import requests
import psycopg2
import datetime
from time import sleep
# HOST = '172.30.99.50'
# DB = 'cabemce-associados-cake4-v01-prod1'
# USER = 'associado_user'
# PASSWORD = 'ASSO123ciado'

# conn = psycopg2.connect(host=HOST, database=DB, user=USER, password=PASSWORD)
# print("Connection established")

# cursor = conn.cursor()

# cursor.execute(
#     """select nome_associado,cpf,email1,email2 from associados,hapvidabeneficios
# where id_associado=associado_id and ativo is true
# and (email1 is not null or email2 is not null)
# and (email1 <> '' or email2 <> '')
# order by nome_associado""")

# rows = cursor.fetchall()

# count = 0

def send_simple_message(emails,nome):
    x = datetime.datetime.now()
    mes = x.strftime("%m")
    ano = x.strftime("%Y")
    return requests.post(
        "https://api.mailgun.net/v3/mg.cabemce.com.br/messages",
        auth=("api", "44fac549dde07eb8381e1317b909c2fc-713d4f73-9989270c"),
        files=[("inline[0]", ("logo.png", open("img/logo.png","rb").read())),
               ("inline[1]", ("smartphone-boleto.png", open("img/smartphone-boleto.png","rb").read()))],
        data={"from": "naoresponda <mailgun@mg.cabemce.com.br>",
              "to": emails,
              "subject": "Lembrete: O vencimento do seu boleto está próximo",
              "html": """
<body style="font-family: montserrat,sans-serif;width: 600px;padding: 0;box-sizing: border-box;">

    <section style="background: #fff; display: flex;justify-content: center;">
        <header style="height: 100px; width: 100px; padding: 10px 10px;">
            <img style="width: 100%;" src="cid:logo.png" alt="logotipo da cabemce" />
            <nav style="margin-top: 8%;">CAIXA BENEFICENTE DOS MILITARES DO CEARÁ</nav>
        </header>
    </section>

    <section style="height: 50px;background: linear-gradient(90deg,#24459d 1.78%,#5365eb 115.03%);justify-content: center;padding-top: 20px;
    align-items: center;text-align: center;color: #eef;">
        <div style="text-align: center;color: #eef;">
        <div class="boleto-title">SEU BOLETO JÁ ESTÁ DISPONÍVEL!</div>  
        <div class="boleto-subtitle">Referência: <span class="mes-referencia">{} de {}</span></div>
        </div>
    </section>
    
    <section style="margin-top: 30px;display: flex;flex-direction: column;text-align: center;font-size: 18px;margin-bottom: 30px;">
        <div style="text-align: center;font-size: 18px;">
            <div style="font-weight: 700;font-size: 24px;color: #019;">
                Olá, {}!
            </div>
            <div style="width: 550px;margin-top: 10px;font-weight: 400;line-height: 30px;color: #249;">
                Seu Boleto Hapvida referente ao mês de Fevereiro já está disponível.
            </div>
            <div style="margin-top: 10px;font-size: 16px; color: #249;">
                <span>Vencimento:</span> 10/{}/{}
            </div>
        </div>
    </section>

    <hr>

    <section style="margin-top: 40px;padding: 10px 10px;flex-direction: column;margin-bottom: 2px;">

        <div style="font-size: 24px;font-weight: 700;line-height: 35px;margin-left: 5px;color: #019;">
            Baixe já seu Boleto Hapvida em nosso Aplicativo
        </div>
    
        <div style="display: flex;width: 600px;">        
            <div class="list">
        <ul  style="width: 275px;color: #249;">
            <li style="list-style: none;">
                <span style="position: absolute; top: 79%;">Controle de Boletos Hapvida</span>
            </li>
            <li style="list-style: none;">
                <span style="position: absolute;top: 85%;">Declaração de Imposto de Renda</span>
            </li>
            <li style="list-style: none;">
                <span style="position: absolute;top: 91%;">Atualização Cadastral</span>
            </li>
            <li style="list-style: none;">
                <span style="position: absolute;top: 96%;">Novidades e Promoções Exclusivas</span>
            </li>
            <li style="list-style: none;">
            <div>
                <button style="border: none;
                background: linear-gradient(90deg,#e12,45%,#900 75%);
                color: #fff;
                border-radius: 5px;
                height: 50px;
                font-weight: 700;
                letter-spacing: .05em;
                padding: 10px;
                margin-top: 25%;"><span>
                    <a href="https://play.google.com/store/apps/details?id=com.cabemce.appcabemce" style="display: flex;
                    align-items: center;
                    width: fit-content;
                    color: #fff;
                    font-size: 14px;">
                    BAIXAR AGORA
                    </a>
                    
                </span></button>
            </div>
            </li>
        </ul>
    </div>
        <div style="display: flex;margin-top: 3px;margin-bottom: 0;position: relative;top: 38px;">
            <img src="cid:smartphone-boleto.png" alt="smartphone com boleto hapvida" style="width: 100%;
            height: 240px;">
        </div>
    
    </div>

    </section>

    <section style="height: 238px;margin-top: 30px;">       
        <div style="height: 200px;background: linear-gradient(90deg,#24459d 1.78%,#5365eb 115.03%);
        margin-top: -12px;text-align: right;position: absolute;width: 600px;padding: 5px 10px 5px 0px;">
            <div style="color: #f2f2ff;flex-direction: column;position: absolute;margin-top: 20px;margin-left: 30px;">
                <div style="color: #f2f2ff;">
                    <h2>Já realizou sua atualização cadastral?</h2>
                </div>
                <div style="text-align: right;
                margin-top: 5px;
                width: 300px;
                margin-right: 5px;margin-left: 40%;">
                    <span style="text-align: right;">
                    É importante estar em dia com a CABEMCE, pois a atualização do seu cadastro garante seus benefícios
                    </span>
                </div>
                <div style="margin-top: 12px;">
                    <button style="border: none;
                    background: linear-gradient(90deg,#e12,45%,#900 75%);
                    color: #fff;
                    border-radius: 5px;
                    width: 225px;
                    height: 50px;
                    font-weight: 700;
                    letter-spacing: .05em;
                    padding: 10px;"><span>
                        <a href="https://cabemce.com.br/2021/08/atualizacao-cadastral" style="display: flex;
                        align-items: center;
                        width: fit-content;
                        color: #fff;
                        font-size: 14px;">
                            ATUALIZAR MEUS DADOS
                        </a>
                </span></button>
                </div>
            </div>

            <div style="color: #f2f2ff;
            font-size: 10px;
            text-align: left;
            margin-left: 20px;
            position: relative;
            top: 87%;
            display: flex;">
                <span style="color: #f2f2ff;
                font-size: 10px;
                text-align: left;">
                * Suas informações estão protegidas conforme a LGPD (13.709/2018)
                </span>
            </div>
          
        </div>
    </section>

    <section style="background: #eef;height: 300px;">
        
        <div class="retirada-title">
            <h2 style="position: relative;
            top: 30px;
            margin-bottom: 50px;
            text-align: center;
            color: #249;">Conheça outras formas de retirada</h2>
        </div>

        <div style="display: flex; justify-content: center;">
            <div style="display: flex;
align-items: center;
flex-direction: column;width: 40%;background: #fff;border-radius: 3px;margin: 20px 20px;box-shadow: 0 4px 4px rgba(0,0,0,.1),0 4px 4px 2px rgba(136,136,153,.04);">
                <div style="width: fit-content;
                margin-top: 15px;
                color: #249;">
                    <span style="font-weight: 700;
                    font-size: 22px;">1° Forma</span>
                </div>
                <div style="width: fit-content;
                margin-top: 5px;">
                    <span style="font-size: 14px;
                    color: #249;">Em nosso Whatsapp</span>
                </div>
                <div style="width: fit-content;
                margin-top: 10px;">
                </div>
                <div style="width: fit-content;
                margin-top: 10px;">
                    <button style="border: none;
                    background: linear-gradient(90deg,#e12,45%,#900 75%);
                    color: #fff;
                    border-radius: 5px;
                    height: 50px;
                    font-weight: 700;
                    letter-spacing: .05em;
                    padding: 10px;"><span>
                      <a href="https://bit.ly/3CC6JZf" style="display: flex;
                      align-items: center;
                      width: fit-content;
                      color: #fff;
                      font-size: 14px;"> 
                         ENVIAR MENSAGEM 
                    </a>
                        
                    </span></button>
                </div>
            </div>
            <div style="display: flex;align-items: center!important;flex-direction: column;width: 40%;background: #fff;border-radius: 3px;margin: 20px 20px;box-shadow: 0 4px 4px rgba(0,0,0,.1),0 4px 4px 2px rgba(136,136,153,.04);">
                <div style="width: fit-content;
                margin-top: 15px;   
                color: #249;">
                    <span style="font-weight: 700;
                    font-size: 22px;">2° Forma</span>
                </div>
                <div style="width: fit-content;
                margin-top: 5px;">
                    <span style="  font-size: 14px;
                    color: #249;">Em nosso Email</span>
                </div>
                <div style="width: fit-content;
                margin-top: 10px;">
                </div>
                <div style="width: fit-content;
                margin-top: 10px;">
                    <button style="border: none;
                    background: linear-gradient(90deg,#e12,45%,#900 75%);
                    color: #fff;
                    border-radius: 5px;
                    height: 50px;
                    font-weight: 700;
                    letter-spacing: .05em;
                    padding: 10px;"><span>
                       <a href="https://boleto.cabemce.com.br/" style="display: flex;
                       align-items: center;
                       width: fit-content;
                       color: #fff;
                       font-size: 14px;">
                         ACESSAR SITE 
                       
                    </span></button>
                </div>
            </div>
        </div>

        <div style="text-align: center;
        width: 450px;margin-left: 12%;">
            <span style="font-size: 12px;
            color: #249;">Caso encontre algum problema, haja alguma dúvida ou deseje a 2° via
                do boleto hapvida referente a outro mês,  
                <a style="text-decoration: underline;
                font-weight: 700;" href="http://encurtador.com.br/gxIRW"> entre em contato </a>
                 conosco.</span>
        </div>
    </section>

    <section style="display: flex;">
        <div style="width: 600px;
        height: 150px;
        background: #f2f2ff;
        box-shadow: -3px 9px 8px 0 rgb(0 0 0 / 10%),0 4px 4px 2px rgb(136 136 153 / 4%);
        border-radius: 5px;
        margin-top: 15px;
        display: flex;
        color: #1e1e1e;">           
            <div style="margin-left: 15px;">
               <span style="font-weight: 700;
               font-size: 18px;">IMPORTANTE</span>
                <p style="font-size: 14px;
                line-height: 1.45em;
                width: 450px;
                margin-left: 0;
                margin-top: 2px;">Afim de promover o melhor equilíbrio financeiro para o funcionamento dos Planos de Saúde, contratos com boletos vencidos a mais de 30 dias serão cancelados.
                    Dessa forma, é importante que o pagamento seja feito rigorosamente em dia.</span>
            </div>
        </div>
    </section>

   <footer class="rodape">
    <ul style="display: flex;
    margin-top: 30px;
    margin-bottom: 30px;
    font-size: 14px;">
        <li style="width: fit-content;"><a style="color: #249;" href="https://www.instagram.com/cabemce/">Instagram</a></li>
        <li style="width: fit-content;"><a style="color: #249;" href="https://cabemce.com.br/2021/08/atualizacao-cadastral">Atualização Cadastral</a></li>
        <li style="width: fit-content;"><a style="color: #249;"href="https://linktr.ee/cabemce">Contatos</a></li>
    </ul>

    <blockquote class="warn-mail">
        <p style="color: #999;
        font-weight: 700;
        font-size: 12px;
        text-align: center;
        line-height: 1.4em;">
        Por gentileza, não responda este email. 
        Este email foi enviado por um sistema automatizado que não processa respostas.
        </p>
    </blockquote>

   </footer>
</body>
</html>

              """.format(mes,ano,nome,mes, ano)})

# for row in rows:
#     nome = row[0]
#     if row[2] == '' or row[2] == None:
#         enviar = [row[3]]
#         print("Data row = (%s, %s, %s)" %
#               (str(row[0]), str(row[2]), str(row[3])))
#     elif row[3] == '' or row[3] == None:
#         enviar = [row[2]]
#         print("Data row = (%s, %s, %s)" %
#               (str(row[0]), str(row[2]), str(row[3])))
#     elif (row[2] != '' or row[2] != None) and (row[3] != '' or row[3] != None):
#         enviar = [row[2], row[3]]
#         print("Data row = (%s, %s, %s)" %
#               (str(row[0]), str(row[2]), str(row[3])))
#     count += 1
#     if(send_simple_message(enviar,nome)):
#         print("Email enviado")
#     else:
#         print("Erro no envio")
#     sleep(80)
send_simple_message('izadoraferreir@gmail.com','HOZANA IZADORA DA SILVA FERREIRA')
print("Email enviado")
