SELECT origin, COUNT(*) 
FROM flights 
GROUP BY origin HAVING COUNT(*)>1;