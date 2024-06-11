class Agendamento:
    def __init__(self, codigo, data_emissao, data_agendamento, status, hora_ini, hora_fim, moradores_cpf, espacos_codigo):
        self.codigo = codigo
        self.data_emissao = data_emissao
        self.data_agendamento = data_agendamento
        self.status = status
        self.hora_ini = hora_ini
        self.hora_fim = hora_fim
        self.moradores_cpf = moradores_cpf
        self.espacos_codigo = espacos_codigo
