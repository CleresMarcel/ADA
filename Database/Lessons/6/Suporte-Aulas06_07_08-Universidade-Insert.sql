INSERT INTO Aluno(NUSP,Nome,Idade,DataNasc) VALUES(1, 'Ana', 17, TO_DATE('01/05/2003','DD/MM/YYYY'));
INSERT INTO Aluno(NUSP,Nome,Idade,DataNasc) VALUES(2, 'Andre', 18, TO_DATE('30/03/2002','DD/MM/YYYY'));
INSERT INTO Aluno(NUSP,Nome,Idade,DataNasc) VALUES(3, 'Afonso', 19, TO_DATE('20/07/2002','DD/MM/YYYY'));
INSERT INTO Aluno(NUSP,Nome,Idade,DataNasc) VALUES(4, 'Alberto', 20, TO_DATE('24/02/2001','DD/MM/YYYY'));
INSERT INTO Aluno(NUSP,Nome,Idade,DataNasc) VALUES(5, 'Bernardo', 21, TO_DATE('12/10/2000','DD/MM/YYYY'));
INSERT INTO Aluno(NUSP,Nome,Idade,DataNasc) VALUES(6, 'Carla', 22, TO_DATE('11/09/1999','DD/MM/YYYY'));
INSERT INTO Aluno(NUSP,Nome,Idade,DataNasc) VALUES(7, 'Diego', 23, TO_DATE('09/08/1998','DD/MM/YYYY'));
INSERT INTO Aluno(NUSP,Nome,Idade,DataNasc) VALUES(8, 'Fabiana', 24, TO_DATE('21/04/1997','DD/MM/YYYY'));
INSERT INTO Aluno(NUSP,Nome,Idade,DataNasc) VALUES(9, 'Gabriel', 25, TO_DATE('10/12/1996','DD/MM/YYYY'));
INSERT INTO Aluno(NUSP,Nome,Idade,DataNasc) VALUES(10, 'Jose', 26, TO_DATE('09/01/1996','DD/MM/YYYY'));


INSERT INTO PROFESSOR VALUES('Joao',11,40,'DOUTOR');
INSERT INTO PROFESSOR VALUES('Juliana',22,30,'DOUTOR');
INSERT INTO PROFESSOR VALUES('Junio',33,35,'DOUTOR');
INSERT INTO PROFESSOR VALUES('Julia',44,30,'DOUTOR');
INSERT INTO PROFESSOR VALUES('Jorge',55,50,'MESTRE');


INSERT INTO Disciplina VALUES('SC518', 'Banco de Dados', 4, 11, 'Fundamentos de Bancos de Dados');
INSERT INTO Disciplina VALUES('SC519', 'Lab de Banco de Dados', 4, 11, 'Fundamentos de Bancos de Dados');
INSERT INTO Disciplina VALUES('SE118', 'Estatística', 6, 22, 'Fundamentos de Estatística');
INSERT INTO Disciplina VALUES('SE120', 'Estatística Avancada', 4, 22, 'Fundamentos de Estatística');
INSERT INTO Disciplina VALUES('SM218', 'Robótica', 6, 33, 'Fundamentos de Robótica');
INSERT INTO Disciplina VALUES('SM228', 'Robótica e IA', 2, 33, 'Fundamentos de Robótica');
INSERT INTO Disciplina VALUES('SA111', 'Calculo', 6, 44, 'Calculo');
INSERT INTO Disciplina VALUES('SA112', 'Calculo II', 6, 44, 'Calculo');
INSERT INTO Disciplina VALUES('SS910', 'Hardware', 6, 55, 'Arquitetura de computadores');
INSERT INTO Disciplina VALUES('SS810', 'Arquitetura de Computadores', 6, 55, 'Arquitetura de computadores');


INSERT INTO Turma VALUES('SC518',1,10);
INSERT INTO Turma VALUES('SC518',2,20);
INSERT INTO Turma VALUES('SC519',1,30);
INSERT INTO Turma VALUES('SC519',2,10);
INSERT INTO Turma VALUES('SE118',1,20);
INSERT INTO Turma VALUES('SE118',2,30);
INSERT INTO Turma VALUES('SE120',1,10);
INSERT INTO Turma VALUES('SE120',2,20);
INSERT INTO Turma VALUES('SM218',1,30);
INSERT INTO Turma VALUES('SM218',2,10);
INSERT INTO Turma VALUES('SM228',1,30);
INSERT INTO Turma VALUES('SM228',2,1);
INSERT INTO Turma VALUES('SA111',1,30);
INSERT INTO Turma VALUES('SA111',2,10);
INSERT INTO Turma VALUES('SA112',1,30);
INSERT INTO Turma VALUES('SA112',2,10);
INSERT INTO Turma VALUES('SS910',1,30);
INSERT INTO Turma VALUES('SS910',2,10);
INSERT INTO Turma VALUES('SS810',1,30);
INSERT INTO Turma VALUES('SS810',2,10);


INSERT INTO Matricula(Sigla, Numero, Aluno, Ano) VALUES('SC518', 1, 1, 2010);
INSERT INTO Matricula(Sigla, Numero, Aluno, Ano) VALUES('SC518', 2, 2, 2010);
INSERT INTO Matricula(Sigla, Numero, Aluno, Ano) VALUES('SC518', 1, 3, 2011);
INSERT INTO Matricula(Sigla, Numero, Aluno, Ano) VALUES('SC518', 2, 4, 2011);


INSERT INTO Matricula(Sigla, Numero, Aluno, Ano) VALUES('SC519', 1, 1, 2010);
INSERT INTO Matricula(Sigla, Numero, Aluno, Ano) VALUES('SC519', 2, 2, 2010);
INSERT INTO Matricula(Sigla, Numero, Aluno, Ano) VALUES('SC519', 1, 3, 2011);
INSERT INTO Matricula(Sigla, Numero, Aluno, Ano) VALUES('SC519', 2, 4, 2011);
INSERT INTO Matricula(Sigla, Numero, Aluno, Ano) VALUES('SC519', 1, 5, 2012);
INSERT INTO Matricula(Sigla, Numero, Aluno, Ano) VALUES('SC519', 2, 6, 2012);


INSERT INTO Matricula(Sigla, Numero, Aluno, Ano) VALUES('SE118', 1, 7, 2010);
INSERT INTO Matricula(Sigla, Numero, Aluno, Ano) VALUES('SE118', 2, 8, 2010);
INSERT INTO Matricula(Sigla, Numero, Aluno, Ano) VALUES('SE118', 1, 7, 2011);
INSERT INTO Matricula(Sigla, Numero, Aluno, Ano) VALUES('SE118', 2, 8, 2011);
INSERT INTO Matricula(Sigla, Numero, Aluno, Ano) VALUES('SE118', 1, 7, 2012);
INSERT INTO Matricula(Sigla, Numero, Aluno, Ano) VALUES('SE118', 2, 8, 2012);


INSERT INTO Matricula(Sigla, Numero, Aluno, Ano) VALUES('SE120', 1, 9, 2010);
INSERT INTO Matricula(Sigla, Numero, Aluno, Ano) VALUES('SE120', 2, 10, 2010);
INSERT INTO Matricula(Sigla, Numero, Aluno, Ano) VALUES('SE120', 1, 9, 2011);
INSERT INTO Matricula(Sigla, Numero, Aluno, Ano) VALUES('SE120', 2, 10, 2011);
INSERT INTO Matricula(Sigla, Numero, Aluno, Ano) VALUES('SE120', 1, 9, 2012);
INSERT INTO Matricula(Sigla, Numero, Aluno, Ano) VALUES('SE120', 2, 10, 2012);
INSERT INTO Matricula(Sigla, Numero, Aluno, Ano) VALUES('SE120', 1, 1, 2010);
INSERT INTO Matricula(Sigla, Numero, Aluno, Ano) VALUES('SE120', 2, 2, 2010);
INSERT INTO Matricula(Sigla, Numero, Aluno, Ano) VALUES('SE120', 1, 1, 2011);
INSERT INTO Matricula(Sigla, Numero, Aluno, Ano) VALUES('SE120', 2, 2, 2011);
INSERT INTO Matricula(Sigla, Numero, Aluno, Ano) VALUES('SE120', 1, 1, 2012);
INSERT INTO Matricula(Sigla, Numero, Aluno, Ano) VALUES('SE120', 2, 2, 2012);

INSERT INTO Matricula(Sigla, Numero, Aluno, Ano) VALUES('SM218', 1, 3, 2010);
INSERT INTO Matricula(Sigla, Numero, Aluno, Ano) VALUES('SM218', 2, 4, 2010);
INSERT INTO Matricula(Sigla, Numero, Aluno, Ano) VALUES('SM218', 1, 3, 2011);
INSERT INTO Matricula(Sigla, Numero, Aluno, Ano) VALUES('SM218', 2, 4, 2011);
INSERT INTO Matricula(Sigla, Numero, Aluno, Ano) VALUES('SM218', 1, 1, 2012);
INSERT INTO Matricula(Sigla, Numero, Aluno, Ano) VALUES('SM218', 2, 2, 2012);
INSERT INTO Matricula(Sigla, Numero, Aluno, Ano) VALUES('SM218', 1, 5, 2010);
INSERT INTO Matricula(Sigla, Numero, Aluno, Ano) VALUES('SM218', 2, 6, 2010);
INSERT INTO Matricula(Sigla, Numero, Aluno, Ano) VALUES('SM218', 1, 5, 2011);
INSERT INTO Matricula(Sigla, Numero, Aluno, Ano) VALUES('SM218', 2, 6, 2011);

INSERT INTO Matricula(Sigla, Numero, Aluno, Ano) VALUES('SM228', 1, 3, 2011);
INSERT INTO Matricula(Sigla, Numero, Aluno, Ano) VALUES('SM228', 2, 4, 2011);
INSERT INTO Matricula(Sigla, Numero, Aluno, Ano) VALUES('SM228', 1, 3, 2012);
INSERT INTO Matricula(Sigla, Numero, Aluno, Ano) VALUES('SM228', 2, 4, 2012);
INSERT INTO Matricula(Sigla, Numero, Aluno, Ano) VALUES('SM228', 1, 1, 2013);
INSERT INTO Matricula(Sigla, Numero, Aluno, Ano) VALUES('SM228', 2, 2, 2013);
INSERT INTO Matricula(Sigla, Numero, Aluno, Ano) VALUES('SM228', 1, 5, 2011);
INSERT INTO Matricula(Sigla, Numero, Aluno, Ano) VALUES('SM228', 2, 6, 2011);


UPDATE Matricula SET Nota = round(dbms_random.value(1,10));

alter table disciplina add monitor NUMBER;
alter table disciplina add constraint FK_MONIT FOREIGN KEY(monitor) REFERENCES Aluno(NUSP);
UPDATE Disciplina SET Monitor = 1 WHERE SIGLA = 'SA111';
UPDATE Disciplina SET Monitor = 3 WHERE SIGLA = 'SA112';
UPDATE Disciplina SET Monitor = 5 WHERE SIGLA = 'SS910';
UPDATE Disciplina SET Monitor = 7 WHERE SIGLA = 'SS810';

