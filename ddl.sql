DROP TABLE IF EXISTS urls;

CREATE TABLE urls 
(
   id SERIAL NOT NULL
 , created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
 , original_url TEXT NOT NULL
 , short_id TEXT NOT NULL
 , constraint pk_url primary key (id) 
);