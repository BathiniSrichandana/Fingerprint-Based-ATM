/*
SQLyog Community Edition- MySQL GUI v7.15 
MySQL - 5.5.29 : Database - fatm
*********************************************************************
*/


/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`fatm` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `fatm`;

/*Table structure for table `acct` */

DROP TABLE IF EXISTS `acct`;

CREATE TABLE `acct` (
  `aid` int(100) NOT NULL AUTO_INCREMENT,
  `cname` varchar(100) NOT NULL,
  `cno` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `ccvv` varchar(100) NOT NULL,
  `ced` varchar(100) NOT NULL,
  `camt` varchar(100) NOT NULL,
  PRIMARY KEY (`aid`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `acct` */

insert  into `acct`(`aid`,`cname`,`cno`,`email`,`ccvv`,`ced`,`camt`) values (10,'Sri Chandana','787884857524','srichandanabathini18@gmail.com','789','09/06/2038','5000'),(6,'sri','123456678','srichandanabathini10@gmail.com','1236899','09/06/2032','4000');

/*Table structure for table `admin` */

DROP TABLE IF EXISTS `admin`;

CREATE TABLE `admin` (
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) NOT NULL,
  PRIMARY KEY (`password`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `admin` */

insert  into `admin`(`username`,`password`) values ('admin','admin');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `eimg` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`id`,`username`,`email`,`password`,`eimg`) values (26,'Sri Chandana','srichandanabathini18@gmail.com','123','1__M_Left_little_finger.BMP');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
