BEGIN TRANSACTION;
CREATE TABLE type (
	id INTEGER NOT NULL, 
	entity_id VARCHAR, 
	type VARCHAR, 
	PRIMARY KEY (id), 
	FOREIGN KEY(entity_id) REFERENCES entity (id)
);
INSERT INTO `type` (id,entity_id,type) VALUES (1,'f6fcdd97-29a7-4537-9ced-b463eb32d445','room'),
 (2,'f8b5df57-9a65-4225-943e-24436ff23989','room');
CREATE TABLE temperature (
	id INTEGER NOT NULL, 
	entity_id VARCHAR, 
	temperature INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(entity_id) REFERENCES entity (id)
);
CREATE TABLE surface (
	id INTEGER NOT NULL, 
	parent_id INTEGER, 
	entity_id VARCHAR, 
	PRIMARY KEY (id), 
	FOREIGN KEY(parent_id) REFERENCES surface (id), 
	FOREIGN KEY(entity_id) REFERENCES entity (id)
);
CREATE TABLE space (
	id INTEGER NOT NULL, 
	entity_id VARCHAR, 
	width INTEGER, 
	length INTEGER, 
	height INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(entity_id) REFERENCES entity (id)
);
INSERT INTO `space` (id,entity_id,width,length,height) VALUES (1,'f6fcdd97-29a7-4537-9ced-b463eb32d445',20,20,20),
 (2,'f8b5df57-9a65-4225-943e-24436ff23989',20,20,20);
CREATE TABLE senses (
	id INTEGER NOT NULL, 
	entity_id VARCHAR, 
	sight INTEGER, 
	hearing INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(entity_id) REFERENCES entity (id)
);
INSERT INTO `senses` (id,entity_id,sight,hearing) VALUES (1,'efa5b93c-f67e-44ba-9890-97d8224cf926',20,30),
 (2,'dc0b909b-e4d9-4596-9e1f-dde553236c52',20,30),
 (3,'af0c692f-1c29-426c-9f64-c39bbcd18545',20,30);
CREATE TABLE room (
	id INTEGER NOT NULL, 
	entity_id VARCHAR, 
	PRIMARY KEY (id), 
	FOREIGN KEY(entity_id) REFERENCES entity (id)
);
INSERT INTO `room` (id,entity_id) VALUES (1,'f6fcdd97-29a7-4537-9ced-b463eb32d445'),
 (2,'f8b5df57-9a65-4225-943e-24436ff23989');
CREATE TABLE player_controlled (
	id INTEGER NOT NULL, 
	entity_id VARCHAR, 
	pid VARCHAR, 
	PRIMARY KEY (id), 
	FOREIGN KEY(entity_id) REFERENCES entity (id)
);
INSERT INTO `player_controlled` (id,entity_id,pid) VALUES (1,'efa5b93c-f67e-44ba-9890-97d8224cf926','110940153174867477377'),
 (2,'dc0b909b-e4d9-4596-9e1f-dde553236c52','112139744712433142310');
CREATE TABLE on_hold (
	id INTEGER NOT NULL, 
	entity_id VARCHAR, 
	callback VARCHAR, 
	timeout INTEGER, 
	data BLOB, 
	PRIMARY KEY (id), 
	FOREIGN KEY(entity_id) REFERENCES entity (id)
);
INSERT INTO `on_hold` (id,entity_id,callback,timeout,data) VALUES (1,'55a3d33d-95b6-461a-910f-65e8c54be5ad','teleport',5,X'8004953a000000000000007d948c0c6e65775f6c6f636174696f6e948c2466386235646635372d396136352d343232352d393433652d32343433366666323339383994732e'),
 (2,'864f9c45-ef10-4cd9-ba0b-83fd6ad11960','teleport',5,X'8004953a000000000000007d948c0c6e65775f6c6f636174696f6e948c2466386235646635372d396136352d343232352d393433652d32343433366666323339383994732e');
CREATE TABLE names (
	id INTEGER NOT NULL, 
	entity_id VARCHAR, 
	name VARCHAR, 
	identifiers VARCHAR, 
	PRIMARY KEY (id), 
	FOREIGN KEY(entity_id) REFERENCES entity (id)
);
INSERT INTO `names` (id,entity_id,name,identifiers) VALUES (1,'f6fcdd97-29a7-4537-9ced-b463eb32d445','Gryffindor Common Room','gcr'),
 (2,'f8b5df57-9a65-4225-943e-24436ff23989','Ravenclaw Common Room','rcr'),
 (3,'55a3d33d-95b6-461a-910f-65e8c54be5ad','chair','chair'),
 (4,'9e4a75a0-e3e3-4412-887d-0fd80ac5b817','door','door'),
 (5,'864f9c45-ef10-4cd9-ba0b-83fd6ad11960','table','table'),
 (6,'c910064e-03fc-4e26-96cb-c57653162deb','door','door'),
 (7,'efa5b93c-f67e-44ba-9890-97d8224cf926','Nicholas','Nicholas'),
 (8,'dc0b909b-e4d9-4596-9e1f-dde553236c52','pierre','pierre'),
 (9,'af0c692f-1c29-426c-9f64-c39bbcd18545','God','God'),
 (10,'cd667bf0-7fed-4a0c-a5e3-f09cb42ed3c0','Castle','castle'),
 (12,'9331dede-9acc-42b1-93b2-a9f53122de51','Eastern corridor','Eastern corridor'),
 (13,'87b7c9f3-49fa-4f99-ae7d-1211ab9df947','Southeastern staircase','Southeastern staircase'),
 (14,'3f82acfa-7598-4b93-b659-61debf3baeda','Ravenclaw tower f1','Ravenclaw tower f1'),
 (15,'9a415ac2-0109-47e1-acf2-3c3433ce8c94','Ravenclaw tower f2','Ravenclaw tower f2'),
 (16,'dd5ee02e-4b20-4d52-9c45-f18002c79929','Ravenclaw tower f3','Ravenclaw tower f3'),
 (17,'f4db30b3-70c3-488a-a586-dcf79b47f078','door','door'),
 (18,'28fa768e-52d1-4334-9d5e-10f891b9beb4','door','door');
CREATE TABLE material (
	id INTEGER NOT NULL, 
	entity_id VARCHAR, 
	material_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(entity_id) REFERENCES entity (id)
);
INSERT INTO `material` (id,entity_id,material_id) VALUES (1,'55a3d33d-95b6-461a-910f-65e8c54be5ad',2),
 (2,'864f9c45-ef10-4cd9-ba0b-83fd6ad11960',1);
CREATE TABLE location (
	id INTEGER NOT NULL, 
	entity_id VARCHAR, 
	room INTEGER, 
	x INTEGER, 
	y INTEGER, 
	z INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(entity_id) REFERENCES entity (id)
);
INSERT INTO `location` (id,entity_id,room,x,y,z) VALUES (1,'efa5b93c-f67e-44ba-9890-97d8224cf926','9331dede-9acc-42b1-93b2-a9f53122de51',0,0,0),
 (2,'dc0b909b-e4d9-4596-9e1f-dde553236c52','f6fcdd97-29a7-4537-9ced-b463eb32d445',0,0,0),
 (3,'af0c692f-1c29-426c-9f64-c39bbcd18545','f6fcdd97-29a7-4537-9ced-b463eb32d445',0,0,0),
 (4,'fb779901-005e-4411-b4ee-84e96a7df260','cd667bf0-7fed-4a0c-a5e3-f09cb42ed3c0',0,0,0),
 (5,'9331dede-9acc-42b1-93b2-a9f53122de51','cd667bf0-7fed-4a0c-a5e3-f09cb42ed3c0',0,0,0),
 (6,'87b7c9f3-49fa-4f99-ae7d-1211ab9df947','cd667bf0-7fed-4a0c-a5e3-f09cb42ed3c0',0,0,0),
 (7,'3f82acfa-7598-4b93-b659-61debf3baeda','cd667bf0-7fed-4a0c-a5e3-f09cb42ed3c0',0,0,0),
 (8,'9a415ac2-0109-47e1-acf2-3c3433ce8c94','cd667bf0-7fed-4a0c-a5e3-f09cb42ed3c0',0,0,0),
 (9,'dd5ee02e-4b20-4d52-9c45-f18002c79929','cd667bf0-7fed-4a0c-a5e3-f09cb42ed3c0',0,0,0),
 (10,'f4db30b3-70c3-488a-a586-dcf79b47f078','9331dede-9acc-42b1-93b2-a9f53122de51',0,0,0),
 (11,'28fa768e-52d1-4334-9d5e-10f891b9beb4','f6fcdd97-29a7-4537-9ced-b463eb32d445',0,0,0);
CREATE TABLE exit (
	id INTEGER NOT NULL, 
	entity_id VARCHAR, 
	dest_id VARCHAR, 
	PRIMARY KEY (id), 
	FOREIGN KEY(entity_id) REFERENCES entity (id)
);
INSERT INTO `exit` (id,entity_id,dest_id) VALUES (1,'9e4a75a0-e3e3-4412-887d-0fd80ac5b817','f8b5df57-9a65-4225-943e-24436ff23989'),
 (2,'c910064e-03fc-4e26-96cb-c57653162deb','f6fcdd97-29a7-4537-9ced-b463eb32d445'),
 (3,'f4db30b3-70c3-488a-a586-dcf79b47f078','f6fcdd97-29a7-4537-9ced-b463eb32d445'),
 (4,'28fa768e-52d1-4334-9d5e-10f891b9beb4','9331dede-9acc-42b1-93b2-a9f53122de51');
CREATE TABLE entity (
	id VARCHAR NOT NULL, 
	type VARCHAR, 
	PRIMARY KEY (id)
);
INSERT INTO `entity` (id,type) VALUES ('a8f487b1-7ed6-4fce-89f2-a68fa491b0c6','entity'),
 ('cd667bf0-7fed-4a0c-a5e3-f09cb42ed3c0','entity'),
 ('f6fcdd97-29a7-4537-9ced-b463eb32d445','entity'),
 ('f8b5df57-9a65-4225-943e-24436ff23989','entity'),
 ('55a3d33d-95b6-461a-910f-65e8c54be5ad','entity'),
 ('9e4a75a0-e3e3-4412-887d-0fd80ac5b817','entity'),
 ('864f9c45-ef10-4cd9-ba0b-83fd6ad11960','entity'),
 ('c910064e-03fc-4e26-96cb-c57653162deb','entity'),
 ('efa5b93c-f67e-44ba-9890-97d8224cf926','avatar'),
 ('dc0b909b-e4d9-4596-9e1f-dde553236c52','avatar'),
 ('af0c692f-1c29-426c-9f64-c39bbcd18545','avatar'),
 ('fb779901-005e-4411-b4ee-84e96a7df260','entity'),
 ('9331dede-9acc-42b1-93b2-a9f53122de51','entity'),
 ('87b7c9f3-49fa-4f99-ae7d-1211ab9df947','entity'),
 ('3f82acfa-7598-4b93-b659-61debf3baeda','entity'),
 ('9a415ac2-0109-47e1-acf2-3c3433ce8c94','entity'),
 ('dd5ee02e-4b20-4d52-9c45-f18002c79929','entity'),
 ('f4db30b3-70c3-488a-a586-dcf79b47f078','entity'),
 ('28fa768e-52d1-4334-9d5e-10f891b9beb4','entity');
CREATE TABLE description (
	id INTEGER NOT NULL, 
	entity_id VARCHAR, 
	description VARCHAR, 
	PRIMARY KEY (id), 
	FOREIGN KEY(entity_id) REFERENCES entity (id)
);
INSERT INTO `description` (id,entity_id,description) VALUES (1,'efa5b93c-f67e-44ba-9890-97d8224cf926','temp_description'),
 (2,'dc0b909b-e4d9-4596-9e1f-dde553236c52','temp_description'),
 (3,'af0c692f-1c29-426c-9f64-c39bbcd18545','temp_description'),
 (4,'fb779901-005e-4411-b4ee-84e96a7df260','A new glowing entity'),
 (5,'9331dede-9acc-42b1-93b2-a9f53122de51','A new glowing entity'),
 (6,'87b7c9f3-49fa-4f99-ae7d-1211ab9df947','A new glowing entity'),
 (7,'3f82acfa-7598-4b93-b659-61debf3baeda','A new glowing entity'),
 (8,'9a415ac2-0109-47e1-acf2-3c3433ce8c94','A new glowing entity'),
 (9,'dd5ee02e-4b20-4d52-9c45-f18002c79929','A new glowing entity'),
 (10,'f4db30b3-70c3-488a-a586-dcf79b47f078','A new glowing entity'),
 (11,'28fa768e-52d1-4334-9d5e-10f891b9beb4','A new glowing entity');
CREATE TABLE container (
	id INTEGER NOT NULL, 
	parent_id INTEGER, 
	entity_id VARCHAR, 
	PRIMARY KEY (id), 
	FOREIGN KEY(parent_id) REFERENCES container (id), 
	FOREIGN KEY(entity_id) REFERENCES entity (id)
);
INSERT INTO `container` (id,parent_id,entity_id) VALUES (1,0,'a8f487b1-7ed6-4fce-89f2-a68fa491b0c6'),
 (2,1,'cd667bf0-7fed-4a0c-a5e3-f09cb42ed3c0'),
 (3,2,'f6fcdd97-29a7-4537-9ced-b463eb32d445'),
 (4,2,'f8b5df57-9a65-4225-943e-24436ff23989'),
 (6,10,'9e4a75a0-e3e3-4412-887d-0fd80ac5b817'),
 (9,12,'efa5b93c-f67e-44ba-9890-97d8224cf926'),
 (10,3,'dc0b909b-e4d9-4596-9e1f-dde553236c52'),
 (11,3,'af0c692f-1c29-426c-9f64-c39bbcd18545'),
 (12,2,'9331dede-9acc-42b1-93b2-a9f53122de51'),
 (13,2,'87b7c9f3-49fa-4f99-ae7d-1211ab9df947'),
 (14,2,'3f82acfa-7598-4b93-b659-61debf3baeda'),
 (15,2,'9a415ac2-0109-47e1-acf2-3c3433ce8c94'),
 (16,2,'dd5ee02e-4b20-4d52-9c45-f18002c79929'),
 (17,12,'f4db30b3-70c3-488a-a586-dcf79b47f078'),
 (18,3,'28fa768e-52d1-4334-9d5e-10f891b9beb4');
CREATE TABLE aliases (
	id INTEGER NOT NULL, 
	entity_id VARCHAR, 
	alias_id VARCHAR, 
	PRIMARY KEY (id), 
	FOREIGN KEY(entity_id) REFERENCES entity (id)
);
CREATE TABLE account_avatar (
	account_id VARCHAR NOT NULL, 
	avatar_id VARCHAR NOT NULL, 
	PRIMARY KEY (account_id, avatar_id), 
	FOREIGN KEY(account_id) REFERENCES account (id), 
	FOREIGN KEY(avatar_id) REFERENCES entity (id)
);
INSERT INTO `account_avatar` (account_id,avatar_id) VALUES ('1d9867d5-9b90-4fab-bf3e-1c1c99d1bf55','efa5b93c-f67e-44ba-9890-97d8224cf926'),
 ('262d700e-e0ab-4990-8742-0fb618f6a544','dc0b909b-e4d9-4596-9e1f-dde553236c52'),
 ('1d9867d5-9b90-4fab-bf3e-1c1c99d1bf55','af0c692f-1c29-426c-9f64-c39bbcd18545');
CREATE TABLE account (
	id VARCHAR NOT NULL, 
	first_name VARCHAR, 
	last_name VARCHAR, 
	email VARCHAR, 
	PRIMARY KEY (id), 
	UNIQUE (email)
);
INSERT INTO `account` (id,first_name,last_name,email) VALUES ('1d9867d5-9b90-4fab-bf3e-1c1c99d1bf55','Nicholas','Aelick','n.aelick@gmail.com'),
 ('262d700e-e0ab-4990-8742-0fb618f6a544','Jade','Cahoon','elrooto@gmail.com');
COMMIT;
