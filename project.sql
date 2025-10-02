-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 02, 2025 at 06:57 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `project`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id` int(10) NOT NULL,
  `name` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id`, `name`, `password`) VALUES
(1, 'admin', '123');

-- --------------------------------------------------------

--
-- Table structure for table `assign`
--

CREATE TABLE `assign` (
  `id` int(255) NOT NULL,
  `custid` int(255) NOT NULL,
  `trainerid` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `assign`
--

INSERT INTO `assign` (`id`, `custid`, `trainerid`) VALUES
(1, 1, 4),
(2, 2, 3),
(3, 4, 5);

-- --------------------------------------------------------

--
-- Table structure for table `diet`
--

CREATE TABLE `diet` (
  `id` int(255) NOT NULL,
  `bmi` double NOT NULL,
  `diet` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `diet`
--

INSERT INTO `diet` (`id`, `bmi`, `diet`) VALUES
(1, 18.590124925639504, 'you are normal and healthy just take healthy food and fresh vegetables.'),
(2, 18.359374999999996, 'you are healthy!'),
(3, 20.446742023841672, ''),
(4, 19.531249999999996, 'you are fit and fine');

-- --------------------------------------------------------

--
-- Table structure for table `trainer`
--

CREATE TABLE `trainer` (
  `id` int(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `age` int(255) NOT NULL,
  `gender` varchar(255) NOT NULL,
  `dob` date NOT NULL,
  `address` varchar(255) NOT NULL,
  `mobile_number` bigint(10) NOT NULL,
  `years_of_experience` varchar(255) NOT NULL,
  `preferred_communication_language` varchar(255) NOT NULL,
  `photo` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `trainer`
--

INSERT INTO `trainer` (`id`, `name`, `email`, `password`, `age`, `gender`, `dob`, `address`, `mobile_number`, `years_of_experience`, `preferred_communication_language`, `photo`) VALUES
(1, 'muskan', 'muskandeep@gmail.com', 'muskan', 19, 'FEMALE', '2004-02-25', 'puda complex,kpt', 9865455332, '5-10 YRS', 'ENGLISH', ''),
(3, 'mehak', 'mehak@34', 'mehak', 45, 'FEMALE', '2003-06-10', 'mohabbat nagar jalandhar', 8765545331, '5-10 YRS', 'PUNJABI', 'uploaded_files\\girl.jpeg'),
(4, 'kritika', 'kriti@17', 'kittu', 20, 'FEMALE', '2005-07-20', 'nwab kapoor singh nagar', 9876221342, '5-10 YRS', 'ENGLISH', 'uploaded_files\\trainer1.jpg'),
(5, 'Happy', 'happy@gmail.com', '123', 23, 'MALE', '2004-05-07', 'Mithapur, jalandhar', 9876543211, '1-5 YRS', 'PUNJABI', 'uploaded_files\\sign.png');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `age` int(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `gender` varchar(255) NOT NULL,
  `dob` date NOT NULL,
  `weight` int(255) NOT NULL,
  `height` int(255) NOT NULL,
  `phonenumber` bigint(255) NOT NULL,
  `photo` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `name`, `age`, `email`, `password`, `gender`, `dob`, `weight`, `height`, `phonenumber`, `photo`) VALUES
(1, 'jashan', 16, 'jashan@gmail.com', '2008', 'MALE', '2008-09-14', 50, 164, 9876564533, 'uploaded_files\\boy.jpg'),
(2, 'muskandeep', 22, 'muskan@gmail.com', 'muski', 'FEMALE', '2004-07-06', 47, 160, 9765543321, 'uploaded_files\\girl.jpeg'),
(3, 'jahnavi', 23, 'jahnavi@gmail.com', 'jaan', 'FEMALE', '2003-10-13', 53, 161, 9865453221, 'uploaded_files\\girl.jpeg'),
(4, 'yashika', 22, 'yashika@gmail.com', 'yashu', 'FEMALE', '2003-07-18', 50, 160, 8766543441, 'uploaded_files\\girl.jpeg');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `assign`
--
ALTER TABLE `assign`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `diet`
--
ALTER TABLE `diet`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `trainer`
--
ALTER TABLE `trainer`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `assign`
--
ALTER TABLE `assign`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `trainer`
--
ALTER TABLE `trainer`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
