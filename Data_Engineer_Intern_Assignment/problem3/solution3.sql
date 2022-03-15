-- create a table
CREATE TABLE mytable(
   ID         INTEGER  NOT NULL PRIMARY KEY, -- there was a missing comma here ;)
   First_name VARCHAR(1) NOT NULL,
   Count      INTEGER  NOT NULL,
   Url        VARCHAR(9) NOT NULL
);

-- insert some values
INSERT INTO mytable VALUES (1,'A',10,'www.A.com');
INSERT INTO mytable VALUES (2,'B',21,'www.B.com');
INSERT INTO mytable VALUES (3,'C',12,'www.C.com');
INSERT INTO mytable VALUES (4,'D',31,'www.D.com');
INSERT INTO mytable VALUES (5,'A',13,'www.A.com');
INSERT INTO mytable VALUES (6,'D',18,'www.D.com');
INSERT INTO mytable VALUES (7,'A',5,'www.A.com');

-- let's simply create two more tables to work on:
CREATE TABLE test1(
   ID         INTEGER  NOT NULL PRIMARY KEY,
   First_name VARCHAR(1) NOT NULL,
   Count      INTEGER  NOT NULL,
   Url        VARCHAR(9) NOT NULL
);

CREATE TABLE test2(
   ID         INTEGER  NOT NULL PRIMARY KEY,
   First_name VARCHAR(1) NOT NULL,
   Count      INTEGER  NOT NULL,
   Url        VARCHAR(9) NOT NULL
);

-- filling out these two tables with appropriate data taken from mytable
INSERT INTO test1
SELECT id, First_name, min(Count), Url FROM mytable
GROUP BY Url
ORDER BY Url;

INSERT INTO test2
SELECT min(id), First_name, Count, Url FROM mytable
GROUP BY Url
ORDER BY Url;

-- leaving only the row with the lowest ID, and update its column "count" to have the value of
-- highest duplicate row ID.
SELECT test2.id, test1.First_name, test1.Count, test1.Url
FROM test1, test2
WHERE test1.Url=test2.Url
ORDER BY test2.id;
