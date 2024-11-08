-- PRAGMA foreign_keys=OFF;
-- BEGIN TRANSACTION;
CREATE TABLE user (
	id INTEGER NOT NULL, 
	username VARCHAR(150) NOT NULL, 
	password VARCHAR(150) NOT NULL, 
	role VARCHAR(20) NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (username)
);
INSERT INTO user VALUES(1,'Kruthik','pbkdf2:sha256:260000$XKRQvECwnfEKtYcx$8057746e5d48cf97ae731435bda076d842694ddaabfcf302b0a08714ca2dc3eb','administrator');
INSERT INTO user VALUES(2,'sricharan','pbkdf2:sha256:260000$0iDbH9p4aHB6KZuO$8f42a8c2f892b671fb052a08ddb1f1507c1963019dddf3affe6c6bda0f6568f6','developer');
CREATE TABLE feedback (
	id INTEGER NOT NULL, 
	date DATE NOT NULL, 
	source VARCHAR(50) NOT NULL, 
	feedback_text TEXT NOT NULL, 
	sentiment_score VARCHAR(20) NOT NULL, 
	product_service_category VARCHAR(50) NOT NULL, 
	rating INTEGER NOT NULL, 
	feedback_length INTEGER NOT NULL, 
	sentiment_category VARCHAR(20) NOT NULL, 
	sentiment_numeric INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
INSERT INTO feedback VALUES(1,'2023-12-11','Review Site','Received damaged item.','Negative','Product Quality',2,22,'Bad',-1);
INSERT INTO feedback VALUES(2,'2023-11-12','Social Media','Customer support was rude.','Neutral','Delivery Service',4,26,'Neutral',0);
INSERT INTO feedback VALUES(3,'2024-02-08','Social Media','Would not recommend.','Negative','Product Quality',2,20,'Bad',-1);
INSERT INTO feedback VALUES(4,'2024-02-27','Survey','Shipping took too long.','Neutral','Product Quality',4,23,'Neutral',0);
INSERT INTO feedback VALUES(5,'2023-12-19','Social Media','Not happy with the product quality.','Neutral','Website Experience',4,35,'Neutral',0);
INSERT INTO feedback VALUES(6,'2024-01-16','Social Media','Customer support was rude.','Positive','Website Experience',1,26,'Good',1);
INSERT INTO feedback VALUES(7,'2024-10-20','Survey','Excellent customer support!','Negative','Website Experience',5,27,'Bad',-1);
INSERT INTO feedback VALUES(8,'2024-08-31','Social Media','Disappointed with product durability.','Neutral','Delivery Service',5,37,'Neutral',0);
INSERT INTO feedback VALUES(9,'2024-03-03','Review Site','Very helpful support team.','Neutral','Delivery Service',3,26,'Neutral',0);
INSERT INTO feedback VALUES(10,'2024-04-06','Survey','Would not recommend.','Positive','Website Experience',2,20,'Good',1);
INSERT INTO feedback VALUES(11,'2024-02-03','Social Media','Fast delivery and great service!','Neutral','Website Experience',4,32,'Neutral',0);
INSERT INTO feedback VALUES(12,'2024-01-10','Survey','Would not recommend.','Negative','Delivery Service',2,20,'Bad',-1);
INSERT INTO feedback VALUES(13,'2024-07-25','Survey','Love the product quality!','Negative','Customer Support',4,25,'Bad',-1);
INSERT INTO feedback VALUES(14,'2024-11-01','Survey','Would not recommend.','Negative','Delivery Service',1,20,'Bad',-1);
INSERT INTO feedback VALUES(15,'2024-03-19','Review Site','Not happy with the product quality.','Neutral','Delivery Service',3,35,'Neutral',0);
INSERT INTO feedback VALUES(16,'2024-05-18','Review Site','Customer support was rude.','Neutral','Website Experience',2,26,'Neutral',0);
INSERT INTO feedback VALUES(17,'2024-06-11','Review Site','Delivery was faster than expected.','Positive','Product Quality',4,34,'Good',1);
INSERT INTO feedback VALUES(18,'2024-02-06','Review Site','Fast delivery and great service!','Positive','Product Quality',4,32,'Good',1);
INSERT INTO feedback VALUES(19,'2023-12-18','Social Media','Not happy with the product quality.','Positive','Delivery Service',2,35,'Good',1);
INSERT INTO feedback VALUES(20,'2024-01-27','Survey','Very helpful support team.','Positive','Product Quality',3,26,'Good',1);
INSERT INTO feedback VALUES(21,'2024-08-09','Survey','Customer support was rude.','Neutral','Product Quality',1,26,'Neutral',0);
INSERT INTO feedback VALUES(22,'2024-07-13','Review Site','Excellent customer support!','Negative','Website Experience',4,27,'Bad',-1);
INSERT INTO feedback VALUES(23,'2024-01-11','Survey','Customer support was rude.','Neutral','Delivery Service',5,26,'Neutral',0);
INSERT INTO feedback VALUES(24,'2024-04-01','Survey','Customer support was rude.','Positive','Product Quality',3,26,'Good',1);
INSERT INTO feedback VALUES(25,'2024-10-31','Social Media','Not happy with the product quality.','Positive','Product Quality',4,35,'Good',1);
INSERT INTO feedback VALUES(26,'2024-02-26','Survey','Customer support was rude.','Neutral','Product Quality',4,26,'Neutral',0);
INSERT INTO feedback VALUES(27,'2024-05-29','Review Site','Delivery was faster than expected.','Positive','Delivery Service',1,34,'Good',1);
INSERT INTO feedback VALUES(28,'2024-05-18','Survey','Very helpful support team.','Neutral','Customer Support',5,26,'Neutral',0);
INSERT INTO feedback VALUES(29,'2023-12-07','Social Media','Poor customer service.','Negative','Product Quality',5,22,'Bad',-1);
INSERT INTO feedback VALUES(30,'2024-08-17','Review Site','Had an amazing experience.','Neutral','Website Experience',1,26,'Neutral',0);
INSERT INTO feedback VALUES(31,'2024-09-27','Review Site','Received damaged item.','Neutral','Website Experience',1,22,'Neutral',0);
INSERT INTO feedback VALUES(32,'2024-02-10','Review Site','Not happy with the product quality.','Neutral','Delivery Service',1,35,'Neutral',0);
INSERT INTO feedback VALUES(33,'2024-06-01','Survey','Delivery was delayed.','Neutral','Customer Support',1,21,'Neutral',0);
INSERT INTO feedback VALUES(34,'2024-07-02','Social Media','Received damaged item.','Positive','Product Quality',5,22,'Good',1);
INSERT INTO feedback VALUES(35,'2024-06-09','Survey','Fast delivery and great service!','Positive','Customer Support',2,32,'Good',1);
INSERT INTO feedback VALUES(36,'2024-05-15','Review Site','Very helpful support team.','Positive','Website Experience',3,26,'Good',1);
INSERT INTO feedback VALUES(37,'2024-03-11','Survey','Delivery was faster than expected.','Neutral','Customer Support',3,34,'Neutral',0);
INSERT INTO feedback VALUES(38,'2024-09-02','Survey','Delivery was delayed.','Negative','Customer Support',5,21,'Bad',-1);
INSERT INTO feedback VALUES(39,'2024-04-29','Survey','Support team was very responsive.','Positive','Customer Support',1,33,'Good',1);
INSERT INTO feedback VALUES(40,'2024-08-23','Social Media','Fast delivery and great service!','Negative','Customer Support',2,32,'Bad',-1);
INSERT INTO feedback VALUES(41,'2024-08-28','Review Site','Website is easy to navigate.','Negative','Customer Support',3,28,'Bad',-1);
INSERT INTO feedback VALUES(42,'2024-07-16','Social Media','Excellent customer support!','Neutral','Website Experience',5,27,'Neutral',0);
INSERT INTO feedback VALUES(43,'2023-12-26','Survey','Disappointed with product durability.','Negative','Product Quality',3,37,'Bad',-1);
INSERT INTO feedback VALUES(44,'2024-06-01','Social Media','Delivery was faster than expected.','Negative','Website Experience',2,34,'Bad',-1);
INSERT INTO feedback VALUES(45,'2024-07-09','Review Site','Delivery was faster than expected.','Negative','Product Quality',1,34,'Bad',-1);
INSERT INTO feedback VALUES(46,'2024-07-18','Survey','Disappointed with product durability.','Negative','Product Quality',2,37,'Bad',-1);
INSERT INTO feedback VALUES(47,'2024-05-11','Survey','Not happy with the product quality.','Neutral','Product Quality',4,35,'Neutral',0);
INSERT INTO feedback VALUES(48,'2024-10-09','Review Site','Website is easy to navigate.','Neutral','Customer Support',5,28,'Neutral',0);
INSERT INTO feedback VALUES(49,'2024-04-03','Social Media','Received damaged item.','Positive','Website Experience',1,22,'Good',1);
INSERT INTO feedback VALUES(50,'2024-07-16','Social Media','Had an amazing experience.','Neutral','Website Experience',2,26,'Neutral',0);
INSERT INTO feedback VALUES(51,'2023-12-07','Social Media','Product quality could be improved.','Neutral','Website Experience',3,34,'Neutral',0);
INSERT INTO feedback VALUES(52,'2024-06-26','Social Media','Fast delivery and great service!','Negative','Website Experience',3,32,'Bad',-1);
INSERT INTO feedback VALUES(53,'2024-10-30','Social Media','Support team was very responsive.','Positive','Delivery Service',5,33,'Good',1);
INSERT INTO feedback VALUES(54,'2024-07-18','Review Site','Support team was very responsive.','Positive','Customer Support',2,33,'Good',1);
INSERT INTO feedback VALUES(55,'2024-05-23','Survey','Shipping took too long.','Positive','Delivery Service',2,23,'Good',1);
INSERT INTO feedback VALUES(56,'2024-08-17','Review Site','Poor customer service.','Negative','Customer Support',1,22,'Bad',-1);
INSERT INTO feedback VALUES(57,'2024-04-09','Review Site','Product quality could be improved.','Positive','Customer Support',5,34,'Good',1);
INSERT INTO feedback VALUES(58,'2024-01-05','Review Site','Very happy with the service.','Neutral','Delivery Service',2,28,'Neutral',0);
INSERT INTO feedback VALUES(59,'2024-07-04','Survey','Excellent customer support!','Neutral','Delivery Service',5,27,'Neutral',0);
INSERT INTO feedback VALUES(60,'2024-02-01','Review Site','Love the product quality!','Neutral','Product Quality',5,25,'Neutral',0);
INSERT INTO feedback VALUES(61,'2024-03-14','Social Media','Fast delivery and great service!','Neutral','Product Quality',5,32,'Neutral',0);
INSERT INTO feedback VALUES(62,'2024-09-26','Social Media','Fast delivery and great service!','Negative','Product Quality',4,32,'Bad',-1);
INSERT INTO feedback VALUES(63,'2023-12-24','Social Media','Website is easy to navigate.','Neutral','Delivery Service',4,28,'Neutral',0);
INSERT INTO feedback VALUES(64,'2024-06-05','Social Media','Love the product quality!','Positive','Customer Support',1,25,'Good',1);
INSERT INTO feedback VALUES(65,'2024-07-29','Social Media','Love the product quality!','Neutral','Product Quality',2,25,'Neutral',0);
INSERT INTO feedback VALUES(66,'2024-04-26','Social Media','Would not recommend.','Neutral','Customer Support',4,20,'Neutral',0);
INSERT INTO feedback VALUES(67,'2024-08-04','Social Media','Love the product quality!','Negative','Delivery Service',5,25,'Bad',-1);
INSERT INTO feedback VALUES(68,'2023-12-25','Social Media','Very happy with the service.','Negative','Product Quality',4,28,'Bad',-1);
INSERT INTO feedback VALUES(69,'2023-11-20','Review Site','Excellent customer support!','Negative','Customer Support',4,27,'Bad',-1);
INSERT INTO feedback VALUES(70,'2024-01-17','Social Media','Very happy with the service.','Neutral','Customer Support',1,28,'Neutral',0);
INSERT INTO feedback VALUES(71,'2023-12-21','Review Site','Delivery was delayed.','Negative','Website Experience',5,21,'Bad',-1);
INSERT INTO feedback VALUES(72,'2024-04-25','Social Media','Delivery was faster than expected.','Positive','Customer Support',1,34,'Good',1);
INSERT INTO feedback VALUES(73,'2023-12-12','Survey','Not happy with the product quality.','Neutral','Website Experience',2,35,'Neutral',0);
INSERT INTO feedback VALUES(74,'2024-10-05','Social Media','Fast delivery and great service!','Positive','Website Experience',2,32,'Good',1);
INSERT INTO feedback VALUES(75,'2024-03-10','Review Site','Website experience was smooth.','Negative','Product Quality',3,30,'Bad',-1);
INSERT INTO feedback VALUES(76,'2024-10-07','Review Site','Fast delivery and great service!','Positive','Website Experience',1,32,'Good',1);
INSERT INTO feedback VALUES(77,'2023-12-09','Social Media','Fast delivery and great service!','Positive','Product Quality',1,32,'Good',1);
INSERT INTO feedback VALUES(78,'2024-04-06','Review Site','Love the product quality!','Negative','Customer Support',4,25,'Bad',-1);
INSERT INTO feedback VALUES(79,'2024-02-07','Social Media','Delivery was delayed.','Negative','Delivery Service',3,21,'Bad',-1);
INSERT INTO feedback VALUES(80,'2024-08-15','Survey','Delivery was delayed.','Positive','Website Experience',2,21,'Good',1);
INSERT INTO feedback VALUES(81,'2024-06-27','Social Media','Website is easy to navigate.','Neutral','Customer Support',1,28,'Neutral',0);
INSERT INTO feedback VALUES(82,'2024-07-21','Review Site','Not happy with the product quality.','Positive','Website Experience',4,35,'Good',1);
INSERT INTO feedback VALUES(83,'2023-11-15','Review Site','Poor customer service.','Positive','Customer Support',2,22,'Good',1);
INSERT INTO feedback VALUES(84,'2024-06-17','Survey','Shipping took too long.','Negative','Website Experience',3,23,'Bad',-1);
INSERT INTO feedback VALUES(85,'2024-04-06','Survey','Disappointed with product durability.','Negative','Delivery Service',2,37,'Bad',-1);
INSERT INTO feedback VALUES(86,'2024-10-21','Survey','Received damaged item.','Negative','Product Quality',1,22,'Bad',-1);
INSERT INTO feedback VALUES(87,'2024-09-30','Review Site','Love the product quality!','Negative','Product Quality',4,25,'Bad',-1);
INSERT INTO feedback VALUES(88,'2023-12-18','Social Media','Customer support was rude.','Neutral','Website Experience',2,26,'Neutral',0);
INSERT INTO feedback VALUES(89,'2024-05-12','Social Media','Delivery was faster than expected.','Negative','Website Experience',2,34,'Bad',-1);
INSERT INTO feedback VALUES(90,'2024-05-23','Social Media','Fast delivery and great service!','Negative','Website Experience',4,32,'Bad',-1);
INSERT INTO feedback VALUES(91,'2024-09-09','Review Site','Would not recommend.','Negative','Delivery Service',1,20,'Bad',-1);
INSERT INTO feedback VALUES(92,'2024-10-06','Review Site','Shipping took too long.','Neutral','Customer Support',3,23,'Neutral',0);
INSERT INTO feedback VALUES(93,'2024-03-23','Review Site','Shipping took too long.','Neutral','Customer Support',2,23,'Neutral',0);
INSERT INTO feedback VALUES(94,'2024-07-04','Review Site','Disappointed with product durability.','Positive','Customer Support',5,37,'Good',1);
INSERT INTO feedback VALUES(95,'2023-12-25','Social Media','Very helpful support team.','Positive','Website Experience',5,26,'Good',1);
INSERT INTO feedback VALUES(96,'2024-08-24','Survey','Delivery was faster than expected.','Positive','Website Experience',3,34,'Good',1);
INSERT INTO feedback VALUES(97,'2024-01-09','Survey','Had an amazing experience.','Negative','Product Quality',1,26,'Bad',-1);
INSERT INTO feedback VALUES(98,'2024-01-09','Social Media','Delivery was faster than expected.','Positive','Website Experience',1,34,'Good',1);
INSERT INTO feedback VALUES(99,'2024-07-12','Social Media','Delivery was faster than expected.','Positive','Delivery Service',3,34,'Good',1);
INSERT INTO feedback VALUES(100,'2024-02-07','Review Site','Support team was very responsive.','Positive','Website Experience',3,33,'Good',1);
CREATE TABLE alembic_version (
	version_num VARCHAR(32) NOT NULL, 
	CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);
COMMIT;
