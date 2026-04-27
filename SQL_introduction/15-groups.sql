-- Eyni xalları qruplaşdırır, hər xaldan neçə dənə olduğunu sayır və saya görə azalan sırayla düzür
SELECT score, COUNT(*) AS number 
FROM second_table 
GROUP BY score 
ORDER BY number DESC;
