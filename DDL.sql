CREATE TABLE IF NOT EXISTS `achievement` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `description` TEXT NOT NULL,
  `image_url` TEXT DEFAULT NULL,
  `created_at` DATETIME NOT NULL,
  `updated_at` DATETIME NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE IF NOT EXISTS `mission` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(255) NOT NULL,
  `description` TEXT DEFAULT NULL,
  `frequency` ENUM('daily','weekly') NOT NULL,
  `points` INT(11) NOT NULL,
  `active` TINYINT(1) NOT NULL DEFAULT 1,
  `created_at` DATETIME NOT NULL,
  `updated_at` DATETIME NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE IF NOT EXISTS `plant` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `user_id` BIGINT(20) NOT NULL,
  `name` VARCHAR(255) NOT NULL,
  `image_url` TEXT DEFAULT NULL,
  `created_at` DATETIME NOT NULL,
  `updated_at` DATETIME NOT NULL,
  PRIMARY KEY (`id`),
  KEY `idx_plant_user` (`user_id`),
  CONSTRAINT `fk_plant_user` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE IF NOT EXISTS `plant_achievement` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `plant_id` INT(11) NOT NULL,
  `achievement_id` INT(11) NOT NULL,
  `awarded_at` DATETIME NOT NULL,
  PRIMARY KEY (`id`),
  KEY `idx_plant_achievement_plant` (`plant_id`),
  KEY `idx_plant_achievement_achievement` (`achievement_id`),
  CONSTRAINT `fk_plant_achievement_plant` FOREIGN KEY (`plant_id`) REFERENCES `plant` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_plant_achievement_achievement` FOREIGN KEY (`achievement_id`) REFERENCES `achievement` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE IF NOT EXISTS `user_achievement` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `user_id` BIGINT(20) NOT NULL,
  `achievement_id` INT(11) NOT NULL,
  `awarded_at` DATETIME NOT NULL,
  PRIMARY KEY (`id`),
  KEY `idx_user_achievement_user` (`user_id`),
  KEY `idx_user_achievement_achievement` (`achievement_id`),
  CONSTRAINT `fk_user_achievement_user` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_user_achievement_achievement` FOREIGN KEY (`achievement_id`) REFERENCES `achievement` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE IF NOT EXISTS `user_mission` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `user_id` BIGINT(20) NOT NULL,
  `mission_id` INT(11) NOT NULL,
  `completed_at` DATETIME NOT NULL,
  `created_at` DATETIME NOT NULL,
  PRIMARY KEY (`id`),
  KEY `idx_user_mission_user` (`user_id`),
  KEY `idx_user_mission_mission` (`mission_id`),
  CONSTRAINT `fk_user_mission_user` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_user_mission_mission` FOREIGN KEY (`mission_id`) REFERENCES `mission` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE IF NOT EXISTS `entry` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `plant_id` INT(11) NOT NULL,
  `height` DECIMAL(10,2) NOT NULL,
  `notes` TEXT DEFAULT NULL,
  `recorded_at` DATETIME NOT NULL,
  PRIMARY KEY (`id`),
  KEY `idx_entry_plant_ts` (`plant_id`, `recorded_at`),
  CONSTRAINT `fk_entry_plant` FOREIGN KEY (`plant_id`) REFERENCES `plant` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE IF NOT EXISTS `entry_image` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `entry_id` INT(11) NOT NULL,
  `image_url` TEXT NOT NULL,
  PRIMARY KEY (`id`),
  KEY `idx_entry_image_entry` (`entry_id`),
  CONSTRAINT `fk_entry_image_entry` FOREIGN KEY (`entry_id`) REFERENCES `entry` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

DELIMITER //

CREATE TRIGGER trg_user_before_insert
BEFORE INSERT ON `user`
FOR EACH ROW
BEGIN
  SET NEW.updated_at = NOW();
END;
//

CREATE TRIGGER trg_user_before_update
BEFORE UPDATE ON `user`
FOR EACH ROW
BEGIN
  SET NEW.updated_at = NOW();
END;
//

CREATE TRIGGER trg_achievement_before_insert
BEFORE INSERT ON `achievement`
FOR EACH ROW
BEGIN
  SET NEW.created_at = NOW();
  SET NEW.updated_at = NOW();
END;
//

CREATE TRIGGER trg_achievement_before_update
BEFORE UPDATE ON `achievement`
FOR EACH ROW
BEGIN
  SET NEW.updated_at = NOW();
END;
//

CREATE TRIGGER trg_mission_before_insert
BEFORE INSERT ON `mission`
FOR EACH ROW
BEGIN
  SET NEW.created_at = NOW();
  SET NEW.updated_at = NOW();
END;
//

CREATE TRIGGER trg_mission_before_update
BEFORE UPDATE ON `mission`
FOR EACH ROW
BEGIN
  SET NEW.updated_at = NOW();
END;
//

CREATE TRIGGER trg_plant_before_insert
BEFORE INSERT ON `plant`
FOR EACH ROW
BEGIN
  SET NEW.created_at = NOW();
  SET NEW.updated_at = NOW();
END;
//

CREATE TRIGGER trg_plant_before_update
BEFORE UPDATE ON `plant`
FOR EACH ROW
BEGIN
  SET NEW.updated_at = NOW();
END;
//

CREATE TRIGGER trg_user_mission_before_insert
BEFORE INSERT ON `user_mission`
FOR EACH ROW
BEGIN
  SET NEW.created_at = NOW();
END;
//

CREATE TRIGGER trg_plant_achievement_before_insert
BEFORE INSERT ON `plant_achievement`
FOR EACH ROW
BEGIN
  SET NEW.awarded_at = NOW();
END;
//

CREATE TRIGGER trg_user_achievement_before_insert
BEFORE INSERT ON `user_achievement`
FOR EACH ROW
BEGIN
  SET NEW.awarded_at = NOW();
END;
//

DELIMITER ;
