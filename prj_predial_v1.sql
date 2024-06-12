-- CREATE SCHEMA IF NOT EXISTS prj_nakari DEFAULT CHARACTER SET utf8 ;
-- USE prj_nakari;


CREATE database IF NOT EXISTS prj_nakari DEFAULT CHARACTER SET utf8 ;
USE prj_nakari ;
-- -----------------------------------------------------
-- Table prj_nakari.usuario
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS prj_nakari.usuario (
  cpf VARCHAR(11) NOT NULL,
  senha VARCHAR(20) NOT NULL,
  nome VARCHAR(50) NOT NULL,
  registro DATE NOT NULL,
  PRIMARY KEY (cpf))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table prj_nakari.moradores
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS prj_nakari.moradores (
  cpf VARCHAR(11) NOT NULL,
  nome VARCHAR(100) NOT NULL,
  torre CHAR(2) NOT NULL,
  andar CHAR(2) NOT NULL,
  apartamento CHAR(3) NOT NULL,
  email VARCHAR(50) NOT NULL,
  telefone VARCHAR(11) NOT NULL,
  moradorescol VARCHAR(45) NOT NULL,
  PRIMARY KEY (cpf),
  CONSTRAINT fk_moradores_usuario
    FOREIGN KEY (cpf)
    REFERENCES prj_nakari.usuario (cpf)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table prj_nakari.funcionarios
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS prj_nakari.funcionarios (
  cpf VARCHAR(11) NOT NULL,
  nome VARCHAR(100) NOT NULL,
  endereco VARCHAR(100) NOT NULL,
  admissao DATE NOT NULL,
  rg VARCHAR(8) NOT NULL,
  salario FLOAT NOT NULL,
  PRIMARY KEY (cpf))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table prj_nakari.terceiros
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS prj_nakari.terceiros (
  coc VARCHAR(14) NOT NULL,
  razao VARCHAR(50) NOT NULL,
  endereco VARCHAR(100) NOT NULL,
  preco FLOAT NOT NULL,
  servico VARCHAR(40) NOT NULL,
  status CHAR(1) NOT NULL,
  email VARCHAR(50) NOT NULL,
  telefone VARCHAR(11) NOT NULL,
  PRIMARY KEY (coc))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table prj_nakari.os
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS prj_nakari.os (
  codigo INT NOT NULL AUTO_INCREMENT,
  servico VARCHAR(50) NOT NULL,
  ds VARCHAR(100) NOT NULL,
  prioridade CHAR(1) NOT NULL,
  status CHAR(1) NOT NULL,
  tempo DATE NOT NULL,
  modalidade CHAR(1) NOT NULL,
  preco FLOAT NULL,
  prestador_nom VARCHAR(100) NOT NULL,
  prestador_coc VARCHAR(14) NOT NULL,
  obs VARCHAR(100) NOT NULL,
  apartamento VARCHAR(100) NOT NULL,
  moradores_cpf VARCHAR(11) NOT NULL,
  funcionarios_cpf VARCHAR(11) NOT NULL,
  terceiros_coc VARCHAR(14) NOT NULL,
  PRIMARY KEY (codigo),
  CONSTRAINT fk_os_moradores1
    FOREIGN KEY (moradores_cpf)
    REFERENCES prj_nakari.moradores (cpf)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_os_funcionarios1
    FOREIGN KEY (funcionarios_cpf)
    REFERENCES prj_nakari.funcionarios (cpf)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_os_terceiros1
    FOREIGN KEY (terceiros_coc)
    REFERENCES prj_nakari.terceiros (coc)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table prj_nakari.espacos
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS prj_nakari.espacos (
  codigo INT NOT NULL AUTO_INCREMENT,
  nome VARCHAR(45) NOT NULL,
  ds VARCHAR(45) NOT NULL,
  status CHAR(1) NOT NULL,
  capacidade INT NOT NULL,
  PRIMARY KEY (codigo))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table prj_nakari.agendamento
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS prj_nakari.agendamento (
  codigo INT NOT NULL AUTO_INCREMENT,
  data_emissao DATE NOT NULL,
  data_agendamento DATE NOT NULL,
  status CHAR(1) NOT NULL,
  hora_ini TIME NULL,
  hora_fim TIME NULL,
  moradores_cpf VARCHAR(11) NOT NULL,
  espacos_codigo INT NOT NULL,
  PRIMARY KEY (codigo, moradores_cpf, espacos_codigo),
  CONSTRAINT fk_agendamento_moradores1
    FOREIGN KEY (moradores_cpf)
    REFERENCES prj_nakari.moradores (cpf)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_agendamento_espacos1
    FOREIGN KEY (espacos_codigo)
    REFERENCES prj_nakari.espacos (codigo)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- Populando a tabela usuario
INSERT INTO usuario (cpf, senha, nome, registro) VALUES
('12345678901', 'senha123', 'João Silva', '2023-01-15'),
('23456789012', 'senha456', 'Maria Oliveira', '2023-02-20'),
('34567890123', 'senha789', 'Carlos Pereira', '2023-03-10'),
('45678901234', 'senha101', 'Ana Santos', '2023-04-25'),
('56789012345', 'senha202', 'Pedro Souza', '2023-05-30'),
('67890123456', 'senha303', 'Lucas Lima', '2023-06-05'),
('78901234567', 'senha404', 'Beatriz Costa', '2023-07-15'),
('89012345678', 'senha505', 'Fernanda Almeida', '2023-08-20'),
('90123456789', 'senha606', 'Ricardo Gomes', '2023-09-10'),
('01234567890', 'senha707', 'Juliana Santos', '2023-10-25'),
('10987654321', 'senha808', 'Sergio Ramos', '2023-11-30'),
('21098765432', 'senha909', 'Patricia Silva', '2023-12-05'),
('32109876543', 'senha010', 'Daniela Lopes', '2023-12-15'),
('43210987654', 'senha111', 'Fabio Araujo', '2024-01-20'),
('54321098765', 'senha212', 'Gabriel Martins', '2024-02-10');

-- Populando a tabela moradores
INSERT INTO moradores (cpf, nome, torre, andar, apartamento, email, telefone, moradorescol) VALUES
('12345678901', 'João Silva', 'A', '1', '101', 'joao@example.com', '11987654321', 'N/A'),
('23456789012', 'Maria Oliveira', 'B', '2', '202', 'maria@example.com', '11987654322', 'N/A'),
('34567890123', 'Carlos Pereira', 'C', '3', '303', 'carlos@example.com', '11987654323', 'N/A'),
('45678901234', 'Ana Santos', 'A', '4', '404', 'ana@example.com', '11987654324', 'N/A'),
('56789012345', 'Pedro Souza', 'B', '5', '505', 'pedro@example.com', '11987654325', 'N/A'),
('67890123456', 'Lucas Lima', 'C', '6', '606', 'lucas@example.com', '11987654326', 'N/A'),
('78901234567', 'Beatriz Costa', 'A', '7', '707', 'beatriz@example.com', '11987654327', 'N/A'),
('89012345678', 'Fernanda Almeida', 'B', '8', '808', 'fernanda@example.com', '11987654328', 'N/A'),
('90123456789', 'Ricardo Gomes', 'C', '9', '909', 'ricardo@example.com', '11987654329', 'N/A'),
('01234567890', 'Juliana Santos', 'A', '10', '110', 'juliana@example.com', '11987654320', 'N/A'),
('10987654321', 'Sergio Ramos', 'B', '11', '111', 'sergio@example.com', '11987654330', 'N/A'),
('21098765432', 'Patricia Silva', 'C', '12', '112', 'patricia@example.com', '11987654331', 'N/A'),
('32109876543', 'Daniela Lopes', 'A', '13', '133', 'daniela@example.com', '11987654332', 'N/A'),
('43210987654', 'Fabio Araujo', 'B', '14', '414', 'fabio@example.com', '11987654333', 'N/A'),
('54321098765', 'Gabriel Martins', 'C', '15', '115', 'gabriel@example.com', '11987654334', 'N/A');

-- Populando a tabela funcionarios
INSERT INTO funcionarios (cpf, nome, endereco, admissao, rg, salario) VALUES
('12345678001', 'Ana Santos', 'Rua A, 100', '2023-01-01', '12345678', 2500.00),
('23456789012', 'Pedro Souza', 'Rua B, 200', '2023-02-01', '23456789', 3000.00),
('34567890123', 'Lucas Lima', 'Rua C, 300', '2023-03-01', '34567890', 3500.00),
('45678901234', 'Carlos Pereira', 'Rua D, 400', '2023-04-01', '45678901', 2800.00),
('56789012345', 'Beatriz Costa', 'Rua E, 500', '2023-05-01', '56789012', 3200.00),
('67890123456', 'Fernanda Almeida', 'Rua F, 600', '2023-06-01', '67890123', 2900.00),
('78901234567', 'Ricardo Gomes', 'Rua G, 700', '2023-07-01', '78901234', 3100.00),
('89012345678', 'Juliana Santos', 'Rua H, 800', '2023-08-01', '89012345', 3300.00),
('90123456789', 'Sergio Ramos', 'Rua I, 900', '2023-09-01', '90123456', 2700.00),
('01234567890', 'Patricia Silva', 'Rua J, 1000', '2023-10-01', '01234567', 3000.00),
('10987654321', 'Daniela Lopes', 'Rua K, 1100', '2023-11-01', '10987654', 2600.00),
('21098765432', 'Fabio Araujo', 'Rua L, 1200', '2023-12-01', '21098765', 2800.00),
('32109876543', 'Gabriel Martins', 'Rua M, 1300', '2024-01-01', '32109876', 3400.00),
('43210987654', 'Camila Rocha', 'Rua N, 1400', '2024-02-01', '43210987', 3500.00),
('54321098765', 'Marcos Teixeira', 'Rua O, 1500', '2024-03-01', '54321098', 3200.00);

-- Populando a tabela terceiros
INSERT INTO terceiros (coc, razao, endereco, preco, servico, status, email, telefone) VALUES
('12345678099', 'Limpeza Total', 'Avenida Central, 500', 150.00, 'Limpeza', 'A', 'limpeza@example.com', '11987654324'),
('23456789088', 'Segurança VIP', 'Rua Segurança, 400', 200.00, 'Segurança', 'A', 'seguranca@example.com', '11987654325'),
('34567890077', 'Jardinagem Verde', 'Rua Jardim, 300', 100.00, 'Jardinagem', 'A', 'jardinagem@example.com', '11987654326'),
('45678901266', 'Manutenção Rápida', 'Rua Manutenção, 200', 250.00, 'Manutenção', 'A', 'manutencao@example.com', '11987654327'),
('56789012355', 'Serviços Elétricos', 'Avenida Elétrica, 100', 300.00, 'Elétrica', 'A', 'eletrica@example.com', '11987654328'),
('67890123444', 'Conserto Express', 'Rua Conserto, 50', 350.00, 'Conserto', 'A', 'conserto@example.com', '11987654329'),
('78901234533', 'Ar Condicionado Ltda', 'Avenida Fresca, 600', 400.00, 'Ar Condicionado', 'A', 'arcondicionado@example.com', '11987654330'),
('89012345622', 'Pintura e Decoração', 'Rua Pintura, 700', 450.00, 'Pintura', 'A', 'pintura@example.com', '11987654331'),
('90123456711', 'Hidráulica e Cia', 'Rua Água, 800', 500.00, 'Hidráulica', 'A', 'hidraulica@example.com', '11987654332'),
('01234567800', 'Serralheria Forte', 'Rua Ferro, 900', 550.00, 'Serralheria', 'A', 'serralheria@example.com', '11987654333'),
('10987654399', 'Limpeza Total Plus', 'Rua Limpeza, 1000', 600.00, 'Limpeza', 'A', 'limpezaplus@example.com', '11987654334'),
('21098765488', 'Segurança Elite', 'Rua Segurança, 1100', 650.00, 'Segurança', 'A', 'segurancaelite@example.com', '11987654335'),
('32109876577', 'Jardinagem de Luxo', 'Rua Jardim, 1200', 700.00, 'Jardinagem', 'A', 'jardinagemluxo@example.com', '11987654336'),
('43210987666', 'Manutenção Completa', 'Avenida Manutenção, 1300', 750.00, 'Manutenção', 'A', 'manutencaocompleta@example.com', '11987654337'),
('54321098755', 'Serviços Elétricos Premium', 'Rua Elétrica, 1400', 800.00, 'Elétrica', 'A', 'eletricapremium@example.com', '11987654338');

-- Populando a tabela os
INSERT INTO os (servico, ds, prioridade, status, tempo, modalidade, preco, prestador_nom, prestador_coc, obs, apartamento, moradores_cpf, funcionarios_cpf, terceiros_coc) VALUES
('Reparação', 'Troca de lâmpada', 'M', 'P', '2023-04-01', 'I', 50.00, 'João Técnico', '12345678099', 'Troca de lâmpada na sala', '101', '54321098765', '45678901234', '12345678099');
INSERT INTO os (servico, ds, prioridade, status, tempo, modalidade, preco, prestador_nom, prestador_coc, obs, apartamento, moradores_cpf, funcionarios_cpf, terceiros_coc) VALUES
('Pintura', 'Pintura de parede', 'B', 'C', '2023-04-05', 'E', 200.00, 'Carlos Pintor', '23456789088', 'Pintura da parede do corredor', '202', '54321098765', '56789012345', '23456789088');
INSERT INTO os (servico, ds, prioridade, status, tempo, modalidade, preco, prestador_nom, prestador_coc, obs, apartamento, moradores_cpf, funcionarios_cpf, terceiros_coc) VALUES
('Manutenção', 'Reparo no encanamento', 'A', 'P', '2023-04-10', 'I', 150.00, 'Paulo Encanador', '34567890077', 'Reparo no encanamento do banheiro', '303', '54321098765', '67890123456', '34567890077');
INSERT INTO os (servico, ds, prioridade, status, tempo, modalidade, preco, prestador_nom, prestador_coc, obs, apartamento, moradores_cpf, funcionarios_cpf, terceiros_coc) VALUES
('Conserto', 'Ajuste de portas', 'M', 'P', '2023-04-15', 'I', 100.00, 'Luiz Técnico', '45678901266', 'Ajuste nas portas da cozinha', '404', '45678901234', '78901234567', '45678901266');
INSERT INTO os (servico, ds, prioridade, status, tempo, modalidade, preco, prestador_nom, prestador_coc, obs, apartamento, moradores_cpf, funcionarios_cpf, terceiros_coc) VALUES
('Elétrica', 'Troca de tomadas', 'B', 'C', '2023-04-20', 'E', 250.00, 'Roberto Eletricista', '56789012355', 'Troca de tomadas na sala', '505', '56789012345', '89012345678', '56789012355');
INSERT INTO os (servico, ds, prioridade, status, tempo, modalidade, preco, prestador_nom, prestador_coc, obs, apartamento, moradores_cpf, funcionarios_cpf, terceiros_coc) VALUES
('Pintura', 'Pintura externa', 'A', 'P', '2023-04-25', 'I', 300.00, 'Marcos Pintor', '67890123444', 'Pintura da fachada', '606', '67890123456', '90123456789', '67890123444');
INSERT INTO os (servico, ds, prioridade, status, tempo, modalidade, preco, prestador_nom, prestador_coc, obs, apartamento, moradores_cpf, funcionarios_cpf, terceiros_coc) VALUES
('Ar Condicionado', 'Instalação de ar', 'M', 'P', '2023-05-01', 'I', 400.00, 'Claudio Técnico', '78901234533', 'Instalação de ar condicionado na sala', '707', '78901234567', '01234567890', '78901234533');
INSERT INTO os (servico, ds, prioridade, status, tempo, modalidade, preco, prestador_nom, prestador_coc, obs, apartamento, moradores_cpf, funcionarios_cpf, terceiros_coc) VALUES
('Hidráulica', 'Troca de torneira', 'B', 'C', '2023-05-05', 'E', 450.00, 'Jorge Hidráulico', '89012345622', 'Troca de torneira da cozinha', '808', '89012345678', '10987654321', '89012345622');
INSERT INTO os (servico, ds, prioridade, status, tempo, modalidade, preco, prestador_nom, prestador_coc, obs, apartamento, moradores_cpf, funcionarios_cpf, terceiros_coc) VALUES
('Serralheria', 'Conserto de portão', 'A', 'P', '2023-05-10', 'I', 500.00, 'Antonio Serralheiro', '90123456711', 'Conserto do portão da garagem', '909', '90123456789', '21098765432', '90123456711');
INSERT INTO os (servico, ds, prioridade, status, tempo, modalidade, preco, prestador_nom, prestador_coc, obs, apartamento, moradores_cpf, funcionarios_cpf, terceiros_coc) VALUES
('Limpeza', 'Limpeza de vidros', 'M', 'P', '2023-05-15', 'I', 550.00, 'Bruno Limpeza', '01234567800', 'Limpeza de vidros das janelas', '1010', '01234567890', '32109876543', '01234567800');
INSERT INTO os (servico, ds, prioridade, status, tempo, modalidade, preco, prestador_nom, prestador_coc, obs, apartamento, moradores_cpf, funcionarios_cpf, terceiros_coc) VALUES
('Segurança', 'Instalação de câmeras', 'B', 'C', '2023-05-20', 'E', 600.00, 'Eduardo Segurança', '10987654399', 'Instalação de câmeras de segurança', '1111', '10987654321', '43210987654', '10987654399');
INSERT INTO os (servico, ds, prioridade, status, tempo, modalidade, preco, prestador_nom, prestador_coc, obs, apartamento, moradores_cpf, funcionarios_cpf, terceiros_coc) VALUES
('Jardinagem', 'Poda de árvores', 'A', 'P', '2023-05-25', 'I', 650.00, 'Fernando Jardineiro', '21098765488', 'Poda de árvores do jardim', '1212', '21098765432', '54321098765', '21098765488');

INSERT INTO os (servico, ds, prioridade, status, tempo, modalidade, preco, prestador_nom, prestador_coc, obs, apartamento, moradores_cpf, funcionarios_cpf, terceiros_coc) VALUES
('Manutenção', 'Troca de telhas', 'M', 'P', '2023-05-30', 'I', 700.00, 'Gustavo Manutenção', '32109876577', 'Troca de telhas do telhado', '1313', '32109876543', '12345678901', '32109876577');

INSERT INTO os (servico, ds, prioridade, status, tempo, modalidade, preco, prestador_nom, prestador_coc, obs, apartamento, moradores_cpf, funcionarios_cpf, terceiros_coc) VALUES
('Elétrica', 'Reparo na fiação', 'B', 'C', '2023-06-01', 'E', 750.00, 'Henrique Eletricista', '43210987666', 'Reparo na fiação do quarto', '1414', '43210987654', '23456789012', '43210987666');
INSERT INTO os (servico, ds, prioridade, status, tempo, modalidade, preco, prestador_nom, prestador_coc, obs, apartamento, moradores_cpf, funcionarios_cpf, terceiros_coc) VALUES
('Conserto', 'Troca de fechaduras', 'A', 'P', '2023-06-05', 'I', 800.00, 'Ivan Técnico', '54321098755', 'Troca de fechaduras das portas', '1515', '54321098765', '34567890123', '54321098755');

-- Populando a tabela espacos
INSERT INTO espacos (nome, ds, status, capacidade) VALUES
('Salão de Festas', 'Espaço para eventos', 'A', 100),
('Piscina', 'Piscina do condomínio', 'A', 50),
('Academia', 'Espaço para exercícios', 'A', 30),
('Quadra Poliesportiva', 'Espaço para esportes', 'A', 40),
('Churrasqueira', 'Espaço para churrascos', 'A', 20),
('Salão de Jogos', 'Espaço para jogos', 'A', 30),
('Brinquedoteca', 'Espaço para crianças', 'A', 25),
('Sala de Reuniões', 'Espaço para reuniões', 'A', 15),
('Jardim', 'Espaço ao ar livre', 'A', 60),
('Playground', 'Espaço para brincadeiras', 'A', 35),
('Cinema', 'Sala de cinema', 'A', 40),
('Sauna', 'Espaço para relaxamento', 'A', 10),
('Biblioteca', 'Espaço para leitura', 'A', 20),
('Terraço', 'Espaço ao ar livre', 'A', 50),
('Sala de Estudos', 'Espaço para estudos', 'A', 10);

-- Populando a tabela agendamento
INSERT INTO agendamento (data_emissao, data_agendamento, status, hora_ini, hora_fim, moradores_cpf, espacos_codigo) VALUES
('2023-05-01', '2023-05-10', 'A', '10:00:00', '12:00:00', '12345678901', 1);
INSERT INTO agendamento (data_emissao, data_agendamento, status, hora_ini, hora_fim, moradores_cpf, espacos_codigo) VALUES
('2023-05-02', '2023-05-11', 'A', '14:00:00', '16:00:00', '23456789012', 2);
INSERT INTO agendamento (data_emissao, data_agendamento, status, hora_ini, hora_fim, moradores_cpf, espacos_codigo) VALUES
('2023-05-03', '2023-05-12', 'A', '18:00:00', '20:00:00', '34567890123', 3);
INSERT INTO agendamento (data_emissao, data_agendamento, status, hora_ini, hora_fim, moradores_cpf, espacos_codigo) VALUES
('2023-05-04', '2023-05-13', 'A', '10:00:00', '12:00:00', '45678901234', 4);
INSERT INTO agendamento (data_emissao, data_agendamento, status, hora_ini, hora_fim, moradores_cpf, espacos_codigo) VALUES
('2023-05-05', '2023-05-14', 'A', '14:00:00', '16:00:00', '56789012345', 5);
INSERT INTO agendamento (data_emissao, data_agendamento, status, hora_ini, hora_fim, moradores_cpf, espacos_codigo) VALUES
('2023-05-06', '2023-05-15', 'A', '18:00:00', '20:00:00', '67890123456', 6);
INSERT INTO agendamento (data_emissao, data_agendamento, status, hora_ini, hora_fim, moradores_cpf, espacos_codigo) VALUES
('2023-05-07', '2023-05-16', 'A', '10:00:00', '12:00:00', '78901234567', 7);
INSERT INTO agendamento (data_emissao, data_agendamento, status, hora_ini, hora_fim, moradores_cpf, espacos_codigo) VALUES
('2023-05-08', '2023-05-17', 'A', '14:00:00', '16:00:00', '89012345678', 8);
INSERT INTO agendamento (data_emissao, data_agendamento, status, hora_ini, hora_fim, moradores_cpf, espacos_codigo) VALUES
('2023-05-09', '2023-05-18', 'A', '18:00:00', '20:00:00', '90123456789', 9);
INSERT INTO agendamento (data_emissao, data_agendamento, status, hora_ini, hora_fim, moradores_cpf, espacos_codigo) VALUES
('2023-05-10', '2023-05-19', 'A', '10:00:00', '12:00:00', '01234567890', 10);
INSERT INTO agendamento (data_emissao, data_agendamento, status, hora_ini, hora_fim, moradores_cpf, espacos_codigo) VALUES
('2023-05-11', '2023-05-20', 'A', '14:00:00', '16:00:00', '10987654321', 11);
INSERT INTO agendamento (data_emissao, data_agendamento, status, hora_ini, hora_fim, moradores_cpf, espacos_codigo) VALUES
('2023-05-12', '2023-05-21', 'A', '18:00:00', '20:00:00', '21098765432', 12);
INSERT INTO agendamento (data_emissao, data_agendamento, status, hora_ini, hora_fim, moradores_cpf, espacos_codigo) VALUES
('2023-05-13', '2023-05-22', 'A', '10:00:00', '12:00:00', '32109876543', 13);
INSERT INTO agendamento (data_emissao, data_agendamento, status, hora_ini, hora_fim, moradores_cpf, espacos_codigo) VALUES
('2023-05-14', '2023-05-23', 'A', '14:00:00', '16:00:00', '43210987654', 14);
INSERT INTO agendamento (data_emissao, data_agendamento, status, hora_ini, hora_fim, moradores_cpf, espacos_codigo) VALUES
('2023-05-15', '2023-05-24', 'A', '18:00:00', '20:00:00', '54321098765', 15);

--ALTERS FEITOS
update funcionarios set admissao = '2024-04-15' where cpf between 0 and 39999999999;
update funcionarios set admissao = '2024-05-31' where cpf between 40000000000 and 699999999999;

-- RELATORIOS FEITOS

-- SUBQUERY
select m.cpf from moradores m where m.cpf = ( select os.moradores_cpf from os group by os.moradores_cpf order by count(os.moradores_cpf) desc limit 1 );

-- GROUP BY COM COUNT
select count(ag.espacos_codigo) from agendamento ag group by ag.data_agendamento;

-- GROUP BY COM AVG
select avg(salario) from funcionarios group by admissao;

-- GROUP BY COM SUM
select sum(preco) as preco, servico from os group by servico;

-- INNER JOIN COM COUNT E SUM
SELECT m.nome, count(os.codigo), sum(os.preco) FROM moradores m
inner join os on m.cpf = os.moradores_cpf
group by m.cpf;

-- RIGHT JOIN COM COUNT E SUM
SELECT m.nome, count(os.codigo), sum(os.preco) FROM moradores m
right join os on m.cpf = os.moradores_cpf
group by m.cpf;

-- LEFT JOIN COM COUNT E SUM
SELECT m.nome, count(os.codigo), sum(os.preco) FROM moradores m
left join os on m.cpf = os.moradores_cpf
group by m.cpf;
