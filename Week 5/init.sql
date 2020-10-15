SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

SET NAMES utf8mb4;

CREATE DATABASE `Main_Data` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `Main_Data`;

DROP TABLE IF EXISTS `Drinks_Menu`;
CREATE TABLE `Drinks_Menu` (
  `drink_id` int NOT NULL AUTO_INCREMENT,
  `drink_name` varchar(10) DEFAULT NULL,
  `drink_cost` float DEFAULT NULL,
  PRIMARY KEY (`drink_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `Drinks_Menu` (`drink_id`, `drink_name`, `drink_cost`) VALUES
(1,	'Tea',	2.5),
(2,	'Hot Choc',	3.5);
