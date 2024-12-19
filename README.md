[VLI] ROBÔ VERIFICADOR DE ARQUIVOS AVD

Vou desenvolver um robô em Python que faz a verificação dos arquivos antes de enviar.

Ele vai ter como entrada o caminho para a pasta de XMLs, o caminho da planilha de NFs e o caminho do AVD e irá perguntar se esse é o primeiro, o segundo ou o terceiro lote.

O AVD estará da seguinte maneira (dados fictícios, apenas para exemplo):ONS;Transmissora;CNPJ;Valor;Check;Check1;Check2;Check3
0001;ONS;”CNPJONS’;1000;OK;OK


A planilha de NFEs estará da seguinte maneira:

Arquivo;Emitente;CNPJ Emitente;Número da NF;Valor da NF; Destinatário;Data de Vencimento
33241227848099000132550010000755921948833606-nfe.xml;NEOENERGIA ATIBAIA TRANSMISSAO DE ENERGIA S.A.;27.848.099/0001-32;75592;30,82;VLI MULTIMODAL S.A.;2024-12-25


Ele irá fazer uma verificação dos valores. Garantindo que o valor total da planilha de NFe esteja igual ao valor total da soma do que foi marcado como ok para aquele lote.

Se ele validar e ver que o valor fechou, deverá retornar: LOTE LIBERADO PARA ENVIO.

Caso contrário, ele deverá retornar quais valores estão faltando para fechar. Aqui, alguns pontos devem ser observados para o bom funcionamento dessa aplicação.

	- Caso ele encontre valores na planilha de NFes que não existam em lugar algum do AVD e que o nome do destinatário é diferente de um desses “VLI MULTIMODAL, VLI MULTIMODAL S A, VLI MULTIMODAL S.A., VLI MULTIMODAL S.A. VLI MULTIMODAL, VLI MULTIMODAL SA”, sendo esses dois requisitos forem verdadeiros, ele deve retornar: Remova esses arquivos: {nome dos XMLS a serem removidos}

Existem algumas transmissoras que possuem vários valores no AVD, mas emitem uma. NF. Ele irá reconhecer esses padrão e aceitar a NF, eu irei descrever em um arquivo JSON, quais Transmissoras devem ser somadas.

	- Caso ele encontre uma dessas notas, ou seja, se ele verificar que o emitente é o mesmo descrito no JSON e o valor fecha com o somatório dos valores, deverá retornar: {Nome do XML}: Nota é o somatório dos valores das transmissoras: “Transmissoras (Códigos vindos do JSON para aquele somatório}”.

	Também será necessário que ele verifique 	                 
	
Se alguma NF estiver marcada no AVD como OK mas não está presente na planilha de NFs, tratando é claro de desconsiderar aquelas que são parte de um somatório, ele deve retornar dizendo: “Estas transmissoras {Transmissora} estão marcadas como ok, mas não estão presentes na planilha de NFs”.


 A principio, são essas condicionais que devem ser conferidas

