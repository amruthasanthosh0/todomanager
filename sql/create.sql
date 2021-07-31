drop table if exists login cascade ; 
drop table if exists todolist cascade ;  



CREATE TABLE login (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  uname TEXT UNIQUE NOT NULL,
  pas TEXT NOT NULL
  );

CREATE TABLE todolist (
  id SERIAL PRIMARY KEY,
  uid INTEGER ,
  task TEXT  NOT NULL,
  lastdate date NOT NULL,
  added_date date not null default current_date,
  status boolean,
  CONSTRAINT uid FOREIGN KEY(uid) REFERENCES login(id) ON DELETE CASCADE
  );



