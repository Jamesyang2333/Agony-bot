-- Create the database schema theme1 which contains three tables: agony, aunt and log
CREATE DATABASE `theme1` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci */

-- Create the table 'agony' which stores message sharing records
CREATE TABLE `agony` (
  `description` varchar(500) DEFAULT NULL,
  `sender` int(11) DEFAULT NULL,
  `num_like` int(11) DEFAULT NULL,
  `id` int(11) DEFAULT NULL,
  `spam` tinyint(1) DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4

-- Create the table 'aunt' which stores message receiving records
CREATE TABLE `aunt` (
  `message` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `reply` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `msgid` int(11) DEFAULT NULL,
  `sender` int(11) DEFAULT NULL,
  `replyid` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin

-- Create the table 'log' which stores all user input records
CREATE TABLE `log` (
  `content` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `sender` int(11) DEFAULT NULL,
  `id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin

-- Operation performed by the administer to check all reportedly spamming message
SELECT * FROM `agony` WHERE spam = TRUE

-- Operation performed ßby the administer to delete a spamming message sharing record identified by msgid
DELETE FROM 'agony' WHERE id = msgid