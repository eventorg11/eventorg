-- phpMyAdmin SQL Dump
-- version 5.1.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Dec 05, 2025 at 01:22 PM
-- Server version: 8.0.42
-- PHP Version: 8.0.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `event-org`
--

-- --------------------------------------------------------

--
-- Table structure for table `app_conference`
--

CREATE TABLE `app_conference` (
  `id` int NOT NULL,
  `title` varchar(200) NOT NULL,
  `description` longtext NOT NULL,
  `short_description` varchar(500) NOT NULL,
  `start_date` datetime(6) NOT NULL,
  `location` varchar(200) NOT NULL,
  `is_online` tinyint(1) NOT NULL,
  `online_link` varchar(200) DEFAULT NULL,
  `status` varchar(20) NOT NULL,
  `registration_deadline` datetime(6) DEFAULT NULL,
  `max_participants` int UNSIGNED DEFAULT NULL,
  `organizer_name` varchar(200) NOT NULL,
  `contact_email` varchar(254) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `curator_id` int DEFAULT NULL
) ;

--
-- Dumping data for table `app_conference`
--

INSERT INTO `app_conference` (`id`, `title`, `description`, `short_description`, `start_date`, `location`, `is_online`, `online_link`, `status`, `registration_deadline`, `max_participants`, `organizer_name`, `contact_email`, `created_at`, `updated_at`, `curator_id`) VALUES
(1, 'Первая в мире конференция', 'Добро пожаловать в первую в мире конференцию! К счастью по стечениям обстоятельств она состоится в нашем университете имени С.Ю. Витте, что позволит нам протестировать наш дарющий большие надежды сервис для организации взаимадействия между участниками конференции.', 'Первая в мире конференция', '2025-12-08 11:27:32.000000', 'Актовый зал', 0, NULL, 'not_started', '2025-12-06 11:27:32.000000', 200, 'Первый в мире организатор', 'first_organisator@gmail.com', '2025-12-05 11:27:32.000000', '2025-12-05 11:31:04.000000', 2),
(11, 'Blockchain и Web3', 'Конференция, посвященная развитию блокчейнов, технологиям Web3, децентрализованным приложениям, смарт-контрактам и тенденциям криптоиндустрии.', 'Конференция по блокчейну и Web3.', '2025-12-06 13:00:00.000000', 'Актовый зал', 0, NULL, 'not_started', '2025-12-05 13:00:00.000000', 150, 'ChainTech Solutions', 'chaintech@info.ru', '2025-12-05 11:20:22.779601', '2025-12-05 11:20:22.779601', 2);

-- --------------------------------------------------------

--
-- Table structure for table `app_contactmessage`
--

CREATE TABLE `app_contactmessage` (
  `id` int NOT NULL,
  `name` varchar(200) NOT NULL,
  `email` varchar(254) NOT NULL,
  `subject` varchar(200) NOT NULL,
  `message` longtext NOT NULL,
  `status` varchar(20) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `user_id` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `app_contactmessage`
--

INSERT INTO `app_contactmessage` (`id`, `name`, `email`, `subject`, `message`, `status`, `created_at`, `updated_at`, `user_id`) VALUES
(1, 'test', 'atewt@gmail.conm', 'test', 'tewst', 'new', '2025-12-05 12:33:53.429359', '2025-12-05 12:33:53.429359', 3);

-- --------------------------------------------------------

--
-- Table structure for table `app_eventregistration`
--

CREATE TABLE `app_eventregistration` (
  `id` int NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `conference_id` int NOT NULL,
  `user_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `app_userprofile`
--

CREATE TABLE `app_userprofile` (
  `id` int NOT NULL,
  `role` varchar(20) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `user_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `app_userprofile`
--

INSERT INTO `app_userprofile` (`id`, `role`, `created_at`, `updated_at`, `user_id`) VALUES
(1, 'student', '2025-12-05 08:59:44.383814', '2025-12-05 08:59:44.383814', 1),
(2, 'curator', '2025-12-05 10:29:12.467791', '2025-12-05 10:29:12.467791', 2),
(3, 'admin', '2025-12-05 11:22:33.524101', '2025-12-05 11:22:33.524101', 3);

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int NOT NULL,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add content type', 1, 'add_contenttype'),
(2, 'Can change content type', 1, 'change_contenttype'),
(3, 'Can delete content type', 1, 'delete_contenttype'),
(4, 'Can view content type', 1, 'view_contenttype'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add Конференция', 6, 'add_conference'),
(22, 'Can change Конференция', 6, 'change_conference'),
(23, 'Can delete Конференция', 6, 'delete_conference'),
(24, 'Can view Конференция', 6, 'view_conference'),
(25, 'Can add Профиль пользователя', 7, 'add_userprofile'),
(26, 'Can change Профиль пользователя', 7, 'change_userprofile'),
(27, 'Can delete Профиль пользователя', 7, 'delete_userprofile'),
(28, 'Can view Профиль пользователя', 7, 'view_userprofile'),
(29, 'Can add Регистрация на мероприятие', 8, 'add_eventregistration'),
(30, 'Can change Регистрация на мероприятие', 8, 'change_eventregistration'),
(31, 'Can delete Регистрация на мероприятие', 8, 'delete_eventregistration'),
(32, 'Can view Регистрация на мероприятие', 8, 'view_eventregistration'),
(33, 'Can add Сообщение обратной связи', 9, 'add_contactmessage'),
(34, 'Can change Сообщение обратной связи', 9, 'change_contactmessage'),
(35, 'Can delete Сообщение обратной связи', 9, 'delete_contactmessage'),
(36, 'Can view Сообщение обратной связи', 9, 'view_contactmessage');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$1000000$GRffTTUOikTVHXcEEecNYF$doER1gi1SUF4GQSOZFz1N7ir7qlPKzSDrJmzfimc+Ko=', '2025-12-05 10:27:58.583717', 0, 'student1', 'Студент', 'Первый', 'student@gmail.com', 0, 1, '2025-12-05 08:59:43.565906'),
(2, 'pbkdf2_sha256$1000000$dLq6QOAfxZngNEj045b8W9$SZfhTDETTsfMfKYYoX+EsamGLFXgPc2K3RFtf0WqH64=', '2025-12-05 12:06:05.638984', 0, 'kurator2', 'Куратор', 'Второй', 'kurator@gmail.com', 0, 1, '2025-12-05 10:29:11.711065'),
(3, 'pbkdf2_sha256$1000000$KulVdOMRnYcJREFWOtBRJH$/0AqXWej2IRph22NpuG3crqvo//QLQHD/aA1mzdPwDc=', '2025-12-05 12:26:57.802427', 1, 'admin', '', '', 'admin@gmail.com', 1, 1, '2025-12-05 11:22:32.782958');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int NOT NULL,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int NOT NULL,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(6, 'app', 'conference'),
(9, 'app', 'contactmessage'),
(8, 'app', 'eventregistration'),
(7, 'app', 'userprofile'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(1, 'contenttypes', 'contenttype'),
(5, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'app', '0001_initial', '2025-12-04 10:04:51.740826'),
(2, 'contenttypes', '0001_initial', '2025-12-05 07:36:41.265624'),
(3, 'auth', '0001_initial', '2025-12-05 07:36:42.057612'),
(4, 'app', '0002_remove_conference_end_date_conference_curator_and_more', '2025-12-05 07:36:42.174269'),
(5, 'contenttypes', '0002_remove_content_type_name', '2025-12-05 07:36:42.296165'),
(6, 'auth', '0002_alter_permission_name_max_length', '2025-12-05 07:36:42.391240'),
(7, 'auth', '0003_alter_user_email_max_length', '2025-12-05 07:36:42.488662'),
(8, 'auth', '0004_alter_user_username_opts', '2025-12-05 07:36:42.497698'),
(9, 'auth', '0005_alter_user_last_login_null', '2025-12-05 07:36:42.582484'),
(10, 'auth', '0006_require_contenttypes_0002', '2025-12-05 07:36:42.585335'),
(11, 'auth', '0007_alter_validators_add_error_messages', '2025-12-05 07:36:42.593607'),
(12, 'auth', '0008_alter_user_username_max_length', '2025-12-05 07:36:42.693502'),
(13, 'auth', '0009_alter_user_last_name_max_length', '2025-12-05 07:36:42.793044'),
(14, 'auth', '0010_alter_group_name_max_length', '2025-12-05 07:36:42.881945'),
(15, 'auth', '0011_update_proxy_permissions', '2025-12-05 07:36:42.892986'),
(16, 'auth', '0012_alter_user_first_name_max_length', '2025-12-05 07:36:42.984115'),
(17, 'sessions', '0001_initial', '2025-12-05 07:36:43.036836'),
(18, 'app', '0003_userprofile', '2025-12-05 08:21:51.754524'),
(19, 'app', '0004_eventregistration', '2025-12-05 09:15:54.152988'),
(20, 'app', '0005_contactmessage', '2025-12-05 12:24:29.512934');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('6qe3e551p6qpabq3x7b3k0r6rwrf98cc', '.eJxVjEEOwiAQRe_C2hBgoFiX7nsGMjCDVA0kpV0Z765NutDtf-_9lwi4rSVsnZcwk7gIEKffLWJ6cN0B3bHemkytrssc5a7Ig3Y5NeLn9XD_Dgr28q3RkgGlR5uNzQQ0Epo8oLfA7AbNLitSyjg6A6nkNUfK7EnZGK3TGsT7A-s1OBk:1vRUtl:arazS0hFl0_0LUumIzcS2oEBzpQDdGwI4TZvMJ7CbqE', '2025-12-19 12:26:57.804557'),
('8mwyb8iesokjlgegiffwr71c0s4mgyfn', '.eJxVjM0OwiAQhN-FsyGU8uN69O4zkN0FpGogKe3J-O62SQ96m8z3zbxFwHUpYe1pDlMUFzGI029HyM9UdxAfWO9NcqvLPJHcFXnQLm8tptf1cP8OCvayrWFMmkbOZJU1QOTJbFExaIgZs3EO0bvBgMeck1fjGTQSa3bIFjOIzxfyjTiU:1vRSgE:aaLtPwPBRj4j7oMrRrp2V6bRfc94nw0DzmbaDmWbixo', '2025-12-19 10:04:50.624056');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `app_conference`
--
ALTER TABLE `app_conference`
  ADD PRIMARY KEY (`id`),
  ADD KEY `app_confere_start_d_0a0d9c_idx` (`start_date`),
  ADD KEY `app_confere_status_e25b34_idx` (`status`),
  ADD KEY `app_conference_curator_id_81160136_fk_auth_user_id` (`curator_id`);

--
-- Indexes for table `app_contactmessage`
--
ALTER TABLE `app_contactmessage`
  ADD PRIMARY KEY (`id`),
  ADD KEY `app_contactmessage_user_id_a058b4ee_fk_auth_user_id` (`user_id`),
  ADD KEY `app_contact_status_57cb0a_idx` (`status`),
  ADD KEY `app_contact_created_22b6ff_idx` (`created_at`);

--
-- Indexes for table `app_eventregistration`
--
ALTER TABLE `app_eventregistration`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `app_eventregistration_user_id_conference_id_908a326f_uniq` (`user_id`,`conference_id`),
  ADD KEY `app_eventre_user_id_d5611d_idx` (`user_id`,`conference_id`),
  ADD KEY `app_eventre_confere_5366d0_idx` (`conference_id`);

--
-- Indexes for table `app_userprofile`
--
ALTER TABLE `app_userprofile`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`),
  ADD KEY `app_userpro_role_59e0a2_idx` (`role`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `app_conference`
--
ALTER TABLE `app_conference`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `app_contactmessage`
--
ALTER TABLE `app_contactmessage`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `app_eventregistration`
--
ALTER TABLE `app_eventregistration`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `app_userprofile`
--
ALTER TABLE `app_userprofile`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `app_conference`
--
ALTER TABLE `app_conference`
  ADD CONSTRAINT `app_conference_curator_id_81160136_fk_auth_user_id` FOREIGN KEY (`curator_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `app_contactmessage`
--
ALTER TABLE `app_contactmessage`
  ADD CONSTRAINT `app_contactmessage_user_id_a058b4ee_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `app_eventregistration`
--
ALTER TABLE `app_eventregistration`
  ADD CONSTRAINT `app_eventregistratio_conference_id_058676a0_fk_app_confe` FOREIGN KEY (`conference_id`) REFERENCES `app_conference` (`id`),
  ADD CONSTRAINT `app_eventregistration_user_id_c626aa29_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `app_userprofile`
--
ALTER TABLE `app_userprofile`
  ADD CONSTRAINT `app_userprofile_user_id_370bd89d_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
