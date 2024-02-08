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

# Find the average grade for each subject.
SELECT sub.subject_name, AVG(m.mark) AS average_mark
FROM marks m
         JOIN subjects sub ON m.subject_id = sub.subject_id
GROUP BY sub.subject_name
ORDER BY average_mark DESC;

SELECT s.subject_name, AVG(m.mark) average_mark
FROM subjects s
         JOIN test.marks m ON s.subject_id = m.subject_id
GROUP BY m.subject_id
ORDER BY average_mark DESC;

# Determine the number of students in each group.
SELECT sg.group_name, COUNT(s.student_id) AS student_count
FROM study_groups sg
         JOIN students s ON sg.group_id = s.group_id
GROUP BY sg.group_name
ORDER BY student_count DESC;

SELECT sg.group_name, count(s.student_id) student_count
FROM students s
         JOIN test.study_groups sg on sg.group_id = s.group_id
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
         JOIN test.students s on s.student_id = m.student_id
GROUP BY s.student_id
ORDER BY avg_mark DESC
LIMIT 3;

# Print the students who got 'excellent' in all subjects (score 75 and above).
SELECT s.student_name
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
