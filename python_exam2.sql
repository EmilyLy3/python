-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema python_exam2
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `python_exam2` ;

-- -----------------------------------------------------
-- Schema python_exam2
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `python_exam2` DEFAULT CHARACTER SET utf8 ;
USE `python_exam2` ;

-- -----------------------------------------------------
-- Table `python_exam2`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `python_exam2`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(50) NOT NULL,
  `last_name` VARCHAR(50) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT NOW(),
  `updated_at` DATETIME NOT NULL DEFAULT NOW() ON UPDATE NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `python_exam2`.`paintings`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `python_exam2`.`paintings` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(255) NOT NULL,
  `description` TEXT(1000) NOT NULL,
  `price` INT NOT NULL,
  `quantity` INT NOT NULL,
  `count` INT NULL,
  `created_at` DATETIME NOT NULL DEFAULT NOW(),
  `updated_at` DATETIME NOT NULL DEFAULT NOW() ON UPDATE NOW(),
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_paintings_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_paintings_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `python_exam2`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `python_exam2`.`purchases`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `python_exam2`.`purchases` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `painting_id` INT NOT NULL,
  INDEX `fk_users_has_paintings_paintings1_idx` (`painting_id` ASC) VISIBLE,
  INDEX `fk_users_has_paintings_users1_idx` (`user_id` ASC) VISIBLE,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_users_has_paintings_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `python_exam2`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_paintings_paintings1`
    FOREIGN KEY (`painting_id`)
    REFERENCES `python_exam2`.`paintings` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
