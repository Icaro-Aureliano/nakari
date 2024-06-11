-- MySQL Script generated by MySQL Workbench
-- Tue Mar 26 22:16:08 2024
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema prj_nakari
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema prj_nakari
-- -----------------------------------------------------
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


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
