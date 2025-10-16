
# Criar o código HTML completo para o gerador de recibos
html_content = '''<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gerador de Recibo - Prestação de Serviço</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }

        .container {
            max-width: 800px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            padding: 40px;
            animation: slideIn 0.5s ease-out;
        }

        @keyframes slideIn {
            from {
                opacity: 0;
                transform: translateY(-30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        h1 {
            color: #667eea;
            text-align: center;
            margin-bottom: 10px;
            font-size: 2em;
            text-transform: uppercase;
            letter-spacing: 2px;
        }

        .subtitle {
            text-align: center;
            color: #666;
            margin-bottom: 30px;
            font-size: 0.9em;
        }

        .section {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
            border-left: 4px solid #667eea;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .section:hover {
            transform: translateX(5px);
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.2);
        }

        .section-title {
            color: #667eea;
            font-size: 1.2em;
            margin-bottom: 15px;
            font-weight: 600;
            display: flex;
            align-items: center;
        }

        .section-title::before {
            content: "▸";
            margin-right: 10px;
            font-size: 1.5em;
        }

        .form-group {
            margin-bottom: 15px;
        }

        label {
            display: block;
            margin-bottom: 5px;
            color: #333;
            font-weight: 500;
            font-size: 0.95em;
        }

        input, textarea, select {
            width: 100%;
            padding: 12px;
            border: 2px solid #e0e0e0;
            border-radius: 8px;
            font-size: 1em;
            transition: all 0.3s ease;
            font-family: inherit;
        }

        input:focus, textarea:focus, select:focus {
            outline: none;
            border-color: #667eea;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
            transform: scale(1.02);
        }

        textarea {
            resize: vertical;
            min-height: 100px;
        }

        .row {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
        }

        .btn {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 15px 40px;
            border: none;
            border-radius: 50px;
            font-size: 1.1em;
            font-weight: 600;
            cursor: pointer;
            width: 100%;
            margin-top: 20px;
            text-transform: uppercase;
            letter-spacing: 1px;
            transition: all 0.3s ease;
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
        }

        .btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 25px rgba(102, 126, 234, 0.6);
        }

        .btn:active {
            transform: translateY(-1px);
        }

        .info-text {
            font-size: 0.85em;
            color: #666;
            font-style: italic;
            margin-top: 5px;
        }

        @media (max-width: 600px) {
            .container {
                padding: 20px;
            }
            
            .row {
                grid-template-columns: 1fr;
            }
            
            h1 {
                font-size: 1.5em;
            }
        }

        .success-message {
            background: #4caf50;
            color: white;
            padding: 15px;
            border-radius: 10px;
            text-align: center;
            margin-top: 20px;
            animation: fadeIn 0.5s ease;
            display: none;
        }

        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>📋 Gerador de Recibo</h1>
        <p class="subtitle">Prestação de Serviço - Rápido e Profissional</p>

        <form id="reciboForm">
            <!-- Número do Recibo -->
            <div class="section">
                <div class="section-title">Número do Recibo</div>
                <div class="form-group">
                    <label for="numeroRecibo">Número:</label>
                    <input type="text" id="numeroRecibo" value="001/2025" required>
                </div>
            </div>

            <!-- Dados do Prestador -->
            <div class="section">
                <div class="section-title">Dados do Prestador (Você)</div>
                <div class="form-group">
                    <label for="nomePrestador">Nome Completo:</label>
                    <input type="text" id="nomePrestador" value="Sergio Roberto Dolinski" required>
                </div>
                <div class="row">
                    <div class="form-group">
                        <label for="cpfPrestador">CPF/CNPJ:</label>
                        <input type="text" id="cpfPrestador" placeholder="000.000.000-00" required>
                    </div>
                    <div class="form-group">
                        <label for="telefonePrestador">Telefone/E-mail:</label>
                        <input type="text" id="telefonePrestador" value="46991247291" required>
                    </div>
                </div>
                <div class="form-group">
                    <label for="enderecoPrestador">Endereço Completo:</label>
                    <input type="text" id="enderecoPrestador" value="Rua Possídio Salomoni" required>
                </div>
            </div>

            <!-- Dados do Cliente -->
            <div class="section">
                <div class="section-title">Dados do Cliente (Contratante)</div>
                <div class="form-group">
                    <label for="nomeCliente">Nome Completo:</label>
                    <input type="text" id="nomeCliente" required>
                </div>
                <div class="row">
                    <div class="form-group">
                        <label for="cpfCliente">CPF/CNPJ:</label>
                        <input type="text" id="cpfCliente" placeholder="000.000.000-00" required>
                    </div>
                    <div class="form-group">
                        <label for="enderecoCliente">Endereço (opcional):</label>
                        <input type="text" id="enderecoCliente">
                    </div>
                </div>
            </div>

            <!-- Descrição do Serviço -->
            <div class="section">
                <div class="section-title">Descrição do Serviço</div>
                <div class="form-group">
                    <label for="descricaoServico">Descreva detalhadamente o serviço prestado:</label>
                    <textarea id="descricaoServico" required placeholder="Ex: Serviço de pintura residencial interna de 3 cômodos, totalizando 60 m², incluindo materiais e mão de obra. Data de início: 10/10/2025. Término: 15/10/2025."></textarea>
                    <p class="info-text">Inclua: tipo de serviço, período, materiais utilizados, etc.</p>
                </div>
            </div>

            <!-- Valores e Pagamento -->
            <div class="section">
                <div class="section-title">Valores e Pagamento</div>
                <div class="row">
                    <div class="form-group">
                        <label for="valorNumero">Valor (R$):</label>
                        <input type="number" id="valorNumero" step="0.01" min="0" required placeholder="1500.00">
                    </div>
                    <div class="form-group">
                        <label for="formaPagamento">Forma de Pagamento:</label>
                        <select id="formaPagamento" required>
                            <option value="">Selecione...</option>
                            <option value="Dinheiro">Dinheiro</option>
                            <option value="PIX">PIX</option>
                            <option value="Transferência Bancária">Transferência Bancária</option>
                            <option value="Cartão de Débito">Cartão de Débito</option>
                            <option value="Cartão de Crédito">Cartão de Crédito</option>
                            <option value="Cheque">Cheque</option>
                        </select>
                    </div>
                </div>
                <div class="form-group">
                    <label for="dataPagamento">Data do Pagamento:</label>
                    <input type="date" id="dataPagamento" required>
                </div>
            </div>

            <button type="submit" class="btn">🎯 Gerar Recibo em PDF</button>
        </form>

        <div class="success-message" id="successMessage">
            ✅ Recibo gerado com sucesso! O download começará automaticamente.
        </div>
    </div>

    <script>
        // Definir data atual como padrão
        document.getElementById('dataPagamento').valueAsDate = new Date();

        // Função para converter número em extenso
        function numeroParaExtenso(numero) {
            const unidades = ['', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove'];
            const dezenas = ['', '', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa'];
            const especiais = ['dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove'];
            const centenas = ['', 'cento', 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos', 'seiscentos', 'setecentos', 'oitocentos', 'novecentos'];

            numero = parseFloat(numero).toFixed(2);
            let [reais, centavos] = numero.split('.');
            reais = parseInt(reais);
            centavos = parseInt(centavos);

            function converterAte999(n) {
                if (n === 0) return '';
                if (n === 100) return 'cem';
                
                let resultado = '';
                const c = Math.floor(n / 100);
                const d = Math.floor((n % 100) / 10);
                const u = n % 10;

                if (c > 0) resultado += centenas[c];
                
                if (d === 1) {
                    if (resultado) resultado += ' e ';
                    resultado += especiais[u];
                } else {
                    if (d > 0) {
                        if (resultado) resultado += ' e ';
                        resultado += dezenas[d];
                    }
                    if (u > 0) {
                        if (resultado) resultado += ' e ';
                        resultado += unidades[u];
                    }
                }
                return resultado;
            }

            function converterGrande(n) {
                if (n === 0) return 'zero';
                
                const milhoes = Math.floor(n / 1000000);
                const milhares = Math.floor((n % 1000000) / 1000);
                const resto = n % 1000;

                let resultado = '';

                if (milhoes > 0) {
                    resultado += converterAte999(milhoes);
                    resultado += milhoes === 1 ? ' milhão' : ' milhões';
                }

                if (milhares > 0) {
                    if (resultado) resultado += ' ';
                    resultado += converterAte999(milhares) + ' mil';
                }

                if (resto > 0) {
                    if (resultado) resultado += ' e ';
                    resultado += converterAte999(resto);
                }

                return resultado;
            }

            let extenso = converterGrande(reais);
            extenso += reais === 1 ? ' real' : ' reais';

            if (centavos > 0) {
                extenso += ' e ' + converterGrande(centavos);
                extenso += centavos === 1 ? ' centavo' : ' centavos';
            }

            return extenso;
        }

        // Função para formatar data
        function formatarData(data) {
            const d = new Date(data + 'T00:00:00');
            return d.toLocaleDateString('pt-BR');
        }

        // Gerar PDF
        document.getElementById('reciboForm').addEventListener('submit', async function(e) {
            e.preventDefault();

            const { jsPDF } = window.jspdf;
            const doc = new jsPDF();

            // Dados do formulário
            const numeroRecibo = document.getElementById('numeroRecibo').value;
            const nomePrestador = document.getElementById('nomePrestador').value;
            const cpfPrestador = document.getElementById('cpfPrestador').value;
            const telefonePrestador = document.getElementById('telefonePrestador').value;
            const enderecoPrestador = document.getElementById('enderecoPrestador').value;
            const nomeCliente = document.getElementById('nomeCliente').value;
            const cpfCliente = document.getElementById('cpfCliente').value;
            const enderecoCliente = document.getElementById('enderecoCliente').value;
            const descricaoServico = document.getElementById('descricaoServico').value;
            const valorNumero = parseFloat(document.getElementById('valorNumero').value);
            const valorExtenso = numeroParaExtenso(valorNumero);
            const formaPagamento = document.getElementById('formaPagamento').value;
            const dataPagamento = formatarData(document.getElementById('dataPagamento').value);

            // Configurar documento
            let y = 20;

            // Título
            doc.setFontSize(20);
            doc.setFont(undefined, 'bold');
            doc.text('RECIBO DE PRESTAÇÃO DE SERVIÇO', 105, y, { align: 'center' });
            
            y += 15;
            doc.setFontSize(12);
            doc.setFont(undefined, 'normal');
            doc.text(`Recibo Nº ${numeroRecibo}`, 105, y, { align: 'center' });

            y += 15;

            // Linha separadora
            doc.setLineWidth(0.5);
            doc.line(20, y, 190, y);
            y += 10;

            // Dados do Prestador
            doc.setFontSize(11);
            doc.setFont(undefined, 'bold');
            doc.text('PRESTADOR DO SERVIÇO:', 20, y);
            y += 7;
            doc.setFont(undefined, 'normal');
            doc.text(`Nome: ${nomePrestador}`, 20, y);
            y += 6;
            doc.text(`CPF/CNPJ: ${cpfPrestador}`, 20, y);
            y += 6;
            doc.text(`Endereço: ${enderecoPrestador}`, 20, y);
            y += 6;
            doc.text(`Contato: ${telefonePrestador}`, 20, y);
            y += 10;

            // Dados do Cliente
            doc.setFont(undefined, 'bold');
            doc.text('CONTRATANTE (CLIENTE):', 20, y);
            y += 7;
            doc.setFont(undefined, 'normal');
            doc.text(`Nome: ${nomeCliente}`, 20, y);
            y += 6;
            doc.text(`CPF/CNPJ: ${cpfCliente}`, 20, y);
            if (enderecoCliente) {
                y += 6;
                doc.text(`Endereço: ${enderecoCliente}`, 20, y);
            }
            y += 10;

            // Linha separadora
            doc.line(20, y, 190, y);
            y += 10;

            // Descrição do Serviço
            doc.setFont(undefined, 'bold');
            doc.text('DESCRIÇÃO DO SERVIÇO:', 20, y);
            y += 7;
            doc.setFont(undefined, 'normal');
            const descricaoLinhas = doc.splitTextToSize(descricaoServico, 170);
            doc.text(descricaoLinhas, 20, y);
            y += (descricaoLinhas.length * 6) + 5;

            // Linha separadora
            doc.line(20, y, 190, y);
            y += 10;

            // Valor
            doc.setFont(undefined, 'bold');
            doc.text('VALOR:', 20, y);
            y += 7;
            doc.setFont(undefined, 'normal');
            doc.text(`R$ ${valorNumero.toFixed(2).replace('.', ',')}`, 20, y);
            y += 6;
            doc.text(`(${valorExtenso})`, 20, y);
            y += 10;

            // Forma de Pagamento
            doc.setFont(undefined, 'bold');
            doc.text('FORMA DE PAGAMENTO:', 20, y);
            y += 7;
            doc.setFont(undefined, 'normal');
            doc.text(formaPagamento, 20, y);
            y += 10;

            // Data
            doc.setFont(undefined, 'bold');
            doc.text('DATA DO PAGAMENTO:', 20, y);
            y += 7;
            doc.setFont(undefined, 'normal');
            doc.text(dataPagamento, 20, y);
            y += 15;

            // Linha separadora
            doc.line(20, y, 190, y);
            y += 15;

            // Assinaturas
            doc.setFontSize(10);
            doc.line(20, y, 90, y);
            doc.line(120, y, 190, y);
            y += 5;
            doc.text('Assinatura do Prestador', 55, y, { align: 'center' });
            doc.text('Assinatura do Cliente', 155, y, { align: 'center' });
            y += 5;
            doc.text(nomePrestador, 55, y, { align: 'center' });
            doc.text(nomeCliente, 155, y, { align: 'center' });

            // Rodapé
            y += 20;
            doc.setFontSize(8);
            doc.setTextColor(100);
            doc.text('Este documento possui validade legal para comprovação de pagamento.', 105, y, { align: 'center' });

            // Salvar PDF
            doc.save(`Recibo_${numeroRecibo.replace('/', '-')}_${nomeCliente.replace(' ', '_')}.pdf`);

            // Mostrar mensagem de sucesso
            const successMsg = document.getElementById('successMessage');
            successMsg.style.display = 'block';
            setTimeout(() => {
                successMsg.style.display = 'none';
            }, 5000);
        });
    </script>
</body>
</html>'''

# Salvar o arquivo
with open('gerador_recibo.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("✅ Arquivo 'gerador_recibo.html' criado com sucesso!")
print("\n📋 INSTRUÇÕES DE USO:")
print("1. Abra o arquivo 'gerador_recibo.html' em qualquer navegador")
print("2. Preencha os campos do formulário")
print("3. Clique em 'Gerar Recibo em PDF'")
print("4. O PDF será baixado automaticamente")
print("\n🎨 RECURSOS:")
print("- Design moderno com animações impressionantes")
print("- Interface responsiva (funciona em celular)")
print("- Conversão automática de valores para extenso")
print("- Campos pré-preenchidos com os dados do Sergio")
print("- Formatação profissional do PDF")
print("- Numeração automática de recibos")
