create database dbFeedback;

use dbFeedback;

create table tbComentarios (
	cod_comentario INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(80),
    data_comentario DATETIME,
    comentario TEXT NOT NULL
    );