CREATE SCHEMA test;
USE test;

CREATE TABLE study_groups
(
    group_id   INT AUTO_INCREMENT PRIMARY KEY,
    group_name VARCHAR(50) NOT NULL
);

CREATE TABLE students
(
    student_id   INT AUTO_INCREMENT PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    group_id     INT,
    FOREIGN KEY (group_id) REFERENCES study_groups (group_id)
);

CREATE TABLE subjects
(
    subject_id   INT AUTO_INCREMENT PRIMARY KEY,
    subject_name VARCHAR(100) NOT NULL
);

CREATE TABLE marks
(
    mark_id    INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    subject_id INT,
    mark       INT NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students (student_id),
    FOREIGN KEY (subject_id) REFERENCES subjects (subject_id)
);
