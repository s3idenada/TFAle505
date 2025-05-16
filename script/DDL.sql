CREATE TABLE `aluno` (
  `id_aluno` int PRIMARY KEY,
  `nome` varchar(255),
  `data_nascimento` date,
  `endereco` varchar(255),
  `contato_pais` varchar(255),
  `matricula` varchar(255)
);

CREATE TABLE `professor` (
  `id_professor` int PRIMARY KEY,
  `nome` varchar(255),
  `especialidade` varchar(255),
  `contato` varchar(255),
  `registro` varchar(255)
);

CREATE TABLE `disciplina` (
  `id_disciplina` int PRIMARY KEY,
  `nome` varchar(255),
  `codigo` varchar(255),
  `carga_horaria` int
);

CREATE TABLE `turma` (
  `id_turma` int PRIMARY KEY,
  `ano_letivo` int,
  `id_disciplina` int,
  `id_professor` int
);

CREATE TABLE `matricula` (
  `id_matricula` int PRIMARY KEY,
  `id_aluno` int,
  `id_turma` int
);

CREATE TABLE `nota_frequencia` (
  `id_nota` int PRIMARY KEY,
  `id_aluno` int,
  `id_disciplina` int,
  `nota` decimal,
  `frequencia` decimal
);

ALTER TABLE `turma` ADD FOREIGN KEY (`id_disciplina`) REFERENCES `disciplina` (`id_disciplina`);

ALTER TABLE `turma` ADD FOREIGN KEY (`id_professor`) REFERENCES `professor` (`id_professor`);

ALTER TABLE `matricula` ADD FOREIGN KEY (`id_aluno`) REFERENCES `aluno` (`id_aluno`);

ALTER TABLE `matricula` ADD FOREIGN KEY (`id_turma`) REFERENCES `turma` (`id_turma`);

ALTER TABLE `nota_frequencia` ADD FOREIGN KEY (`id_aluno`) REFERENCES `aluno` (`id_aluno`);

ALTER TABLE `nota_frequencia` ADD FOREIGN KEY (`id_disciplina`) REFERENCES `disciplina` (`id_disciplina`);
