CREATE SCHEMA test;
USE test;

# Get students with GPA > 80
SELECT s.student_name, AVG(m.mark) avg_mark
FROM marks m
         JOIN students s ON m.student_id = s.student_id
GROUP BY s.student_id
HAVING avg_mark > 80
ORDER BY avg_mark DESC;

# Request with win-funcs
SELECT group_name, student_name, total_mark
FROM (SELECT sg.group_name,
             s.student_name,
             SUM(m.mark)                                                           AS total_mark,
             ROW_NUMBER() OVER (PARTITION BY s.group_id ORDER BY SUM(m.mark) DESC) AS row_num
      FROM marks m
               JOIN students s ON m.student_id = s.student_id
               JOIN study_groups sg ON s.group_id = sg.group_id
      GROUP BY s.student_id, sg.group_name) AS ranked_students
WHERE row_num = 1;

# --= Practice Tasks =--

# Print the list of students with their groups.
SELECT s.student_name, sg.group_name
FROM students s
         JOIN study_groups sg ON s.group_id = sg.group_id
ORDER BY sg.group_name, s.student_name;

SELECT s.student_name, sg.group_name
FROM students s
         join study_groups sg on sg.group_id = s.group_id
order by s.group_id;

# Find the average grade for each subject.
SELECT sub.subject_name, AVG(m.mark) AS average_mark
FROM marks m
         JOIN subjects sub ON m.subject_id = sub.subject_id
GROUP BY sub.subject_name
ORDER BY average_mark DESC;

SELECT s.subject_name, AVG(m.mark) average_mark
FROM subjects s
         JOIN marks m ON s.subject_id = m.subject_id
GROUP BY m.subject_id
ORDER BY average_mark DESC;

SELECT s.student_name, sb.subject_name, avg(m.mark) as avg_mark
FROM marks m
         join subjects sb on sb.subject_id = m.subject_id
         join students s on s.student_id = m.student_id
GROUP BY s.student_id, sb.subject_id
order by s.student_id, sb.subject_id;


# Determine the number of students in each group.
SELECT sg.group_name, COUNT(s.student_id) AS student_count
FROM study_groups sg
         JOIN students s ON sg.group_id = s.group_id
GROUP BY sg.group_name
ORDER BY student_count DESC;

SELECT sg.group_name, count(s.student_id) student_count
FROM students s
         JOIN study_groups sg on sg.group_id = s.group_id
GROUP BY s.group_id
ORDER BY student_count DESC;

# Find the top 3 students with the highest average score in the university.
SELECT s.student_name, AVG(m.mark) AS average_mark
FROM students s
         JOIN marks m ON s.student_id = m.student_id
GROUP BY s.student_id
ORDER BY average_mark DESC
LIMIT 3;

SELECT s.student_name, AVG(mark) avg_mark
FROM marks m
         JOIN students s on s.student_id = m.student_id
GROUP BY s.student_id
ORDER BY avg_mark DESC
LIMIT 3;

# Print the students who got 'excellent' in all subjects (score 75 and above).
SELECT s.student_name, min(m.mark)
FROM students s
         JOIN marks m ON s.student_id = m.student_id
GROUP BY s.student_id, m.subject_id
HAVING MIN(m.mark) >= 70;


# Find the groups where all students have an average score above 75.
SELECT sg.group_name, AVG(m.mark) as avg_mark
FROM study_groups sg
         JOIN students s ON sg.group_id = s.group_id
         JOIN marks m ON s.student_id = m.student_id
GROUP BY sg.group_id
HAVING avg_mark > 75;


# Count of Students Passing Each Subject:
# Count how many students have passed each subject (e.g., mark > 65),
# only include subjects with more than a certain number of passing students.

SELECT a.subject_id, count(a.subject_id) passing
FROM (SELECT m.subject_id, avg(m.mark) avg_mark
      FROM marks m
      GROUP BY m.student_id, m.subject_id
      having avg_mark > 76) a
GROUP BY a.subject_id;

SELECT count(*)
FROM (SELECT m.subject_id, COUNT(DISTINCT m.student_id) AS passing
      FROM marks m
      GROUP BY m.student_id, m.subject_id
      HAVING AVG(m.mark) > 76) sip
GROUP BY sip.subject_id;


-- 1.
-- # Subjects with Low Average Marks:
-- # Find subjects with an average mark below a certain level,
-- # indicating potentially difficult subjects.

SELECT s.subject_name
FROM (SELECT m.subject_id, avg(m.mark) as avg_mark
      FROM marks m
      GROUP BY m.subject_id
      HAVING avg_mark < 80) s_id
         JOIN subjects s ON s_id.subject_id = s.subject_id;


-- 2.
-- # Subjects with a Minimum Number of Marks:
-- # Find subjects that have been graded a minimum number of times,
-- # indicating popularity or mandatory evaluation.

SELECT m.subject_id, count(*) as marks_num
FROM kse_practice_db.marks m
GROUP BY m.subject_id
HAVING marks_num = (SELECT MIN(marks_amount.amount)
                    FROM (SELECT COUNT(m.mark) as amount
                          FROM marks m
                          GROUP BY m.subject_id) marks_amount)
ORDER BY marks_num;


-- 3.
-- # Groups with Below Average Performance:
-- # Identify study groups where the average mark is below the overall average

SELECT s.subject_name
FROM (SELECT m.subject_id, avg(m.mark) as avg_mark
      FROM marks m
      GROUP BY m.subject_id
      HAVING avg_mark < (SELECT avg(m.mark) FROM marks m)) s_id
         JOIN subjects s ON s_id.subject_id = s.subject_id;

SELECT s.subject_name
FROM (SELECT m.subject_id, avg(m.mark) as avg_mark
      FROM marks m
        JOIN kse_practice_db.subjects sbj ON sbj.subject_id = m.subject_id
      GROUP BY m.subject_id
      HAVING avg_mark < (SELECT avg(m.mark) FROM marks m)) s_id
         JOIN subjects s ON s_id.subject_id = s.subject_id;


-- 4. Find Students with Above Average Marks in a Specific Subject
-- This query finds students who have scored above the average mark in a specific subject (e.g., subject_id = 1).

SELECT m.student_id, avg(m.mark) as avg_mark
FROM marks m
WHERE m.subject_id = 1
GROUP BY m.student_id, m.subject_id
HAVING avg_mark >= (select avg(m.mark)
                    from marks m
                    where m.subject_id = 1)
ORDER BY avg_mark DESC;


SELECT student_id, AVG(mark) AS average_mark
FROM marks
WHERE subject_id = 1
  AND student_id IN (SELECT student_id
                     FROM marks
                     WHERE subject_id = 1
                     GROUP BY student_id
                     HAVING AVG(mark) > (SELECT AVG(mark)
                                         FROM marks
                                         WHERE subject_id = 1))
GROUP BY student_id;


-- 2. List Subjects with the Highest Average Mark
-- This query lists subjects that have the highest average mark across all subjects.

-- 3. Identify Groups with No Failing Marks
-- This query identifies study groups where no student has received a mark below 50 in any subject.

-- 4. Students with Marks in Top 10% for Any Subject
-- This query selects students who have marks in the top 10% for any subject.

-- 5. Average Marks of Students Who Also Take a Specific Subject
-- This query calculates the average marks of students who are also enrolled in a specific subject (e.g., subject_id = 2).

