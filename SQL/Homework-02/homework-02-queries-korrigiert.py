1. 
SELECT country, gdp FROM economy ORDER BY gdp DESC NULLS LAST LIMIT 10;

2. 
SELECT country.name, gdp FROM economy JOIN country ON country.code = country ORDER BY gdp DESC NULLS LAST LIMIT 10;

4. 
SELECT country.name, agriculture, industry, service FROM economy JOIN country ON country.code = country WHERE agriculture > industry AND agriculture > service ORDER BY agriculture DESC NULLS LAST LIMIT 10;

Homework2
1.
SELECT name, country, percentage 
FROM language 
ORDER BY percentage DESC;

# NEU: Distinct - um 
SELECT Distinct name, percentage FROM language WHERE percentage = 100;

4. #Einfacher:
SELECT name, COUNT(country) 
FROM language GROUP BY name 
ORDER BY COUNT(country) DESC NULLS LAST LIMIT 10;

5.
SELECT name, COUNT(country), AVG(percentage) 
FROM language GROUP BY name 
ORDER BY COUNT(country) DESC NULLS LAST LIMIT 20;

#6. What's the economy in spanish speaking countries vs. english speaking countries?
#1. Wir müssen zwei tables miteinander verbinden: language und economy.
#2. Wir kreieren die richtigen columns: name, country, percentage: SELECT name, country, percentage FROM language WHERE name IN("Spanish", "English");
#3. Dann definieren wir, dass um spanisch- oder englischsprachig zu sein als Land muss English oder Spanish >= 50 Prozent sein.

 SELECT name, country, percentage FROM language WHERE name IN('English','Spanish');

 SELECT name, country, percentage FROM language WHERE name IN('English','Spanish') AND percentage >=50;

 #4. Nun kommt der economy table dazu: JOIN vom economy table:
  SELECT language.name, language.country, language.percentage, economy.gdp 
  FROM language JOIN economy ON language.country = economy.country
  WHERE language.name IN('English','Spanish') AND percentage >=50;

 #Einfacher: mit WITH und spen-keyword. Hier: spengdp
 WITH spengdp as (
 SELECT language.name, language.country, language.percentage, economy.gdp 
 FROM language JOIN economy ON language.country = economy.country
 WHERE language.name IN('English','Spanish') AND percentage >=50
) 
SELECT name, COUNT(name), AVG(gdp) FROM spengdp GROUP BY name;

#7.
SELECT language.name, language.country, language.percentage, mostspoken.mycount
FROM (SELECT name, COUNT(country) AS mycount FROM language GROUP BY name) AS 
mostspoken 
JOIN language ON language.name = mostspoken.name ORDER BY mostspoken.mycount DESC, language.percentage DESC;


#Oder:
SELECT language.name, country.name, language.percentage, mostspoken.mycount
FROM (SELECT name, COUNT(country) AS mycount FROM language GROUP BY name) AS 
mostspoken 
JOIN language ON language.name = mostspoken.name 
JOIN country ON language.country = country.code
ORDER BY mostspoken.mycount DESC, language.percentage DESC;



