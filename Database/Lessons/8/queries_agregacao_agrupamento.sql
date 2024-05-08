use academico;


SELECT ALUNO, NOTA FROM MATRICULA
ORDER BY ALUNO;


SELECT ALUNO, MAX(NOTA), MIN(NOTA), ROUND(AVG(NOTA)), COUNT(NOTA), SUM(NOTA)
FROM MATRICULA
GROUP BY ALUNO
ORDER BY ALUNO;

SELECT ALUNO, MAX(NOTA), MIN(NOTA), ROUND(AVG(NOTA)), COUNT(NOTA), SUM(NOTA)
FROM MATRICULA
GROUP BY ALUNO, SIGLA
ORDER BY ALUNO, SIGLA;

SELECT ALUNO, MAX(NOTA), MIN(NOTA), ROUND(AVG(NOTA)), COUNT(NOTA), SUM(NOTA)
FROM MATRICULA
GROUP BY ALUNO
HAVING COUNT(NOTA) > 3
ORDER BY ALUNO;

SELECT A.Nome, ROUND(AVG(M.Nota)) as Media_Notas
 FROM Aluno A JOIN Matricula M
 ON M.Aluno = A.RA
 WHERE M.Nota BETWEEN 5.0 AND 10.0
 GROUP BY A.Nome
 ORDER BY A.Nome;
 
 SELECT A.NOME, ROUND(AVG(M.NOTA)) AS MEDIA_NOTAS
 FROM Aluno A JOIN Matricula M
 ON M.Aluno = A.RA
 WHERE M.Nota BETWEEN 5.0 AND 10.0 ;
 
 
SELECT * FROM MATRICULA;


select A.Nome, D.Nome, count(*), max(M.Nota)
from Aluno A join Matricula M
 on A.RA = M.Aluno
 join Disciplina D
 on D.Sigla = M.Sigla
group by A.Nome, D.Nome;


select A.Nome, D.Nome, count(*), max(M.Nota)
from Aluno A join Matricula M
 on A.RA = M.Aluno
 join Disciplina D
 on D.Sigla = M.Sigla
group by A.Nome, D.Nome
 having count(*) > 1;
 
 
 SELECT * FROM ALUNO;



