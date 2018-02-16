--Query all columns for all American cities in CITY with populations larger than 100000. The CountryCode for America is USA.

SELECT
    ID
    , NAME
    , COUNTRYCODE
    , DISTRICT
    , POPULATION
FROM
    CITY
WHERE
    COUNTRYCODE = 'USA'
    AND POPULATION > 100000;