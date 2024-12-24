-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 16-12-2024 a las 22:44:52
-- Versión del servidor: 8.3.0
-- Versión de PHP: 8.2.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `sistema_experto`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `historial_tests`
--

DROP TABLE IF EXISTS `historial_tests`;
CREATE TABLE IF NOT EXISTS `historial_tests` (
  `id` int NOT NULL AUTO_INCREMENT,
  `usuario_id` int DEFAULT NULL,
  `Autoestima` int NOT NULL,
  `Pensamientos_negativos` int NOT NULL,
  `Problemas_interpersonales` int NOT NULL,
  `Ansiedad` int NOT NULL,
  `Funcion_cognitiva` int NOT NULL,
  `Regulacion_emocional` int NOT NULL,
  `clasificacion` varchar(100) DEFAULT NULL,
  `fecha` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `usuario_id` (`usuario_id`)
) ENGINE=MyISAM AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `historial_tests`
--

INSERT INTO `historial_tests` (`id`, `usuario_id`, `Autoestima`, `Pensamientos_negativos`, `Problemas_interpersonales`, `Ansiedad`, `Funcion_cognitiva`, `Regulacion_emocional`, `clasificacion`, `fecha`) VALUES
(36, 11, 10, 4, 4, 7, 10, 3, 'Depresión grave', '2024-12-08 19:02:31'),
(35, 11, 16, 7, 7, 9, 12, 6, 'Depresión grave', '2024-12-08 18:54:27'),
(34, 11, 16, 9, 9, 9, 12, 6, 'Depresión grave', '2024-12-08 18:44:06'),
(33, 7, 6, 3, 3, 3, 4, 2, 'Depresión moderada', '2024-12-08 18:26:04'),
(32, 7, 4, 3, 2, 3, 3, 2, 'Depresión leve', '2024-12-08 18:25:18'),
(31, 7, 18, 9, 9, 9, 12, 6, 'Depresión grave', '2024-12-08 18:24:46'),
(30, 7, 12, 6, 6, 6, 8, 4, 'Depresión grave', '2024-12-08 18:23:14'),
(29, 7, 6, 3, 3, 3, 4, 2, 'Depresión moderada', '2024-12-08 18:21:10'),
(26, 7, 13, 6, 5, 4, 4, 2, 'Depresión grave', '2024-12-08 01:54:06'),
(28, 7, 18, 9, 9, 9, 12, 6, 'Depresión grave', '2024-12-08 18:17:16'),
(27, 7, 6, 3, 3, 3, 4, 2, 'Depresión moderada', '2024-12-08 18:08:54'),
(24, 7, 8, 4, 4, 4, 5, 2, 'Depresión moderada', '2024-12-07 06:52:24'),
(25, 8, 15, 6, 5, 7, 8, 4, 'Depresión grave', '2024-12-08 00:59:52'),
(37, 11, 10, 4, 4, 7, 10, 3, 'Depresión grave', '2024-12-08 19:04:24'),
(38, 11, 16, 7, 7, 6, 8, 4, 'Depresión grave', '2024-12-08 19:05:24'),
(39, 11, 6, 3, 5, 3, 6, 2, 'Depresión moderada', '2024-12-08 19:06:26'),
(40, 11, 14, 8, 4, 2, 5, 2, 'Depresión grave', '2024-12-08 19:17:36'),
(41, 11, 15, 9, 9, 9, 12, 6, 'Depresión grave', '2024-12-08 19:20:55'),
(42, 11, 7, 7, 1, 5, 6, 2, 'Depresión moderada', '2024-12-08 19:22:15'),
(43, 11, 7, 7, 1, 5, 6, 2, 'Depresión moderada', '2024-12-08 19:22:59'),
(44, 11, 8, 4, 3, 3, 4, 2, 'Depresión moderada', '2024-12-08 19:32:59'),
(45, 9, 6, 3, 5, 5, 6, 2, 'Depresión moderada', '2024-12-08 19:33:46'),
(46, 9, 6, 3, 5, 5, 6, 2, 'Depresión moderada', '2024-12-08 19:34:21'),
(47, 9, 18, 9, 9, 9, 12, 6, 'Depresión grave', '2024-12-08 19:39:42'),
(48, 7, 13, 7, 4, 7, 10, 4, 'Depresión grave', '2024-12-09 06:21:56'),
(49, 7, 13, 7, 4, 7, 10, 4, 'Depresión grave', '2024-12-09 06:22:07'),
(50, 7, 13, 7, 4, 7, 10, 4, 'Depresión grave', '2024-12-09 06:22:11'),
(51, 7, 13, 6, 4, 6, 8, 4, 'Depresión grave', '2024-12-09 06:24:23'),
(52, 7, 18, 9, 7, 7, 10, 5, 'Depresión grave', '2024-12-09 06:30:15'),
(53, 7, 13, 7, 4, 4, 5, 3, 'Depresión grave', '2024-12-09 07:08:07'),
(54, 7, 10, 5, 6, 4, 5, 2, 'Depresión grave', '2024-12-09 08:11:21'),
(55, 7, 11, 7, 5, 6, 10, 4, 'Depresión grave', '2024-12-09 23:35:48'),
(56, 7, 10, 5, 4, 9, 12, 6, 'Depresión grave', '2024-12-10 03:07:02'),
(57, 9, 13, 6, 4, 3, 5, 3, 'Depresión grave', '2024-12-10 16:47:56'),
(58, 7, 7, 5, 2, 1, 0, 1, 'Depresión leve', '2024-12-12 06:31:13'),
(59, 13, 2, 0, 1, 2, 3, 1, 'Mínima depresión', '2024-12-12 20:22:03'),
(60, 14, 8, 2, 5, 0, 2, 3, 'Depresión moderada', '2024-12-12 21:02:15');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `rol`
--

DROP TABLE IF EXISTS `rol`;
CREATE TABLE IF NOT EXISTS `rol` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `descripcion` text,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `rol`
--

INSERT INTO `rol` (`id`, `nombre`, `descripcion`) VALUES
(1, 'Estudiante', 'Rol para estudiantes del sistema experto'),
(2, 'Administrador', 'Rol para administradores del sistema experto');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
CREATE TABLE IF NOT EXISTS `usuarios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `contrasena` varchar(100) NOT NULL,
  `sexo` enum('hombre','mujer') NOT NULL,
  `edad` int NOT NULL,
  `correo_electronico` varchar(255) NOT NULL,
  `carrera` enum('Ing. de Sistemas','Administracion','Contabilidad','Agronomia','Turismo y Hoteleria') NOT NULL,
  `ciclo` enum('I','II','III','IV','V','VI','VII','VIII','VIIII','X') NOT NULL,
  `rol_id` int DEFAULT NULL,
  `fecha_registro` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`),
  KEY `fk_usuarios_rol` (`rol_id`)
) ENGINE=MyISAM AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `nombre`, `contrasena`, `sexo`, `edad`, `correo_electronico`, `carrera`, `ciclo`, `rol_id`, `fecha_registro`) VALUES
(10, 'Diana', '$2b$12$bFoQWuK5xktvIjbROv4cPuf1DTBahdO0hK1SjkVO7e6AGKQDNIge2', 'mujer', 35, 'diana@gmail.com', 'Contabilidad', 'VIII', 2, '2024-12-10 12:39:50'),
(9, 'Brando', '$2b$12$ct0JWozaIQZdUM9tddtYzOxBQwn.RJC/DpupuILZQ5WxfPawjDnCq', 'hombre', 22, 'brando@gmail.com', 'Ing. de Sistemas', 'VIII', 1, '2024-12-10 12:39:50'),
(7, 'Sumac', '$2b$12$Pq9La.Cf.9nyYxS4VAvAEuVRamh9iTttiEq48YiM2Ic.AquU7acm.', 'mujer', 30, 'sumac@gmail.com', 'Ing. de Sistemas', 'I', 1, '2024-12-10 12:39:50'),
(8, 'Yamily', '$2b$12$oUzWX/19TRyEXrnZw2nCzOgfrOJstk650UNj7x.e5ddrnUspa9.Ga', 'mujer', 21, 'yamily@gmail.com', 'Ing. de Sistemas', 'VIII', 2, '2024-12-10 12:39:50'),
(11, 'Hannah', '$2b$12$pWnYqiaDpEUd.djTqvLxUOcCTKmnsduDqhsrjeRwLPiAueiMh40oy', 'mujer', 14, 'hannah@gmail.com', 'Turismo y Hoteleria', 'X', 2, '2024-12-10 12:39:50'),
(12, 'Loki', '$2b$12$aJcIV18SBBu4LdwE0JxENu9HcbM6IgfPN.UCbR.KIws4Lm.2kpqMq', 'hombre', 19, 'loki@gmail.com', 'Administracion', 'V', 2, '2024-12-10 12:39:50'),
(13, 'Elchala', '$2b$12$WZt86LeJ.ub6e7tdxJO36ejn7fReKR2dzlJxdmdfdb/if6LM24fme', 'hombre', 21, '2101010367@undc.edu.pe', 'Ing. de Sistemas', 'VIII', NULL, '2024-12-12 20:17:21'),
(14, 'aderly', '$2b$12$JmEkhleqHnTs88Crdk6xq.HJrV6oiirhUySh56.NFHNzjXqew2FlO', 'hombre', 21, '2101010367@undc.edu.pe', 'Ing. de Sistemas', 'VIII', NULL, '2024-12-12 20:59:00');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
