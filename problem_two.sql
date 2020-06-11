CREATE TABLE companies
  (
     company_id INT,
     name       TEXT,
     city       TEXT,
     country    TEXT,
     revenue    INT
  );

CREATE TABLE offices
  (
     location_id INT,
     company_id  INT REFERENCES companies (company_id),
     name        TEXT,
     city        TEXT,
     country     TEXT
  );

INSERT INTO companies VALUES(1,'Acme LLC', 'San Jose', 'USA', 250);
INSERT INTO companies VALUES(2,'TechCo Inc', 'Austin', 'USA', 150);
INSERT INTO companies VALUES(3,'Nikola Inc', 'New York', 'USA', 450);


INSERT INTO offices VALUES(1,1, 'HeadQuarters', 'San Jose', 'USA');
INSERT INTO offices VALUES(2,1, 'SFO-Downtown', 'San Francisco', 'USA');
INSERT INTO offices VALUES(2,1, 'LA-Downtown', 'Los Angeles', 'USA');
INSERT INTO offices VALUES(2,1, 'San Diego', 'San Diego', 'USA');
INSERT INTO offices VALUES(2,1, 'Santa Monica', 'Santa Monica', 'USA');

INSERT INTO offices VALUES(3,3, 'HQ','New York' ,'USA');
INSERT INTO offices VALUES(3,3, 'Phily office','Philadelphia' ,'USA');

WITH office_numbers
     AS (SELECT company_id,
                office_count
         FROM   (SELECT company_id,
                        Count(*) AS office_count
                 FROM   offices
                 GROUP  BY company_id)
         WHERE  office_count < 5)
SELECT companies.name              AS company_name,
       companies.revenue           AS company_revenue,
       office_numbers.office_count AS number_of_offices
FROM   companies
       INNER JOIN office_numbers
               ON office_numbers.company_id = companies.company_id;