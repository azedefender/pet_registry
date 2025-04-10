-- db/setup.sql

CREATE DATABASE IF NOT EXISTS Друзья_человека;
USE Друзья_человека;

CREATE TABLE IF NOT EXISTS ДомашниеЖивотные (
    id INT AUTO_INCREMENT PRIMARY KEY,
    имя VARCHAR(50),
    команда VARCHAR(50),
    дата_рождения DATE
);

CREATE TABLE IF NOT EXISTS ВьючныеЖивотные (
    id INT AUTO_INCREMENT PRIMARY KEY,
    имя VARCHAR(50),
    команда VARCHAR(50),
    дата_рождения DATE
);

CREATE TABLE IF NOT EXISTS МолодыеЖивотные (
    id INT AUTO_INCREMENT PRIMARY KEY,
    имя VARCHAR(50),
    команда VARCHAR(50),
    дата_рождения DATE,
    возраст_в_месяцах INT
);