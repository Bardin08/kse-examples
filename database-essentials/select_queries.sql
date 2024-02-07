CREATE SCHEMA test;
USE test;

# Get students with GPA > 80
SELECT s.student_id, s.student_name, AVG(m.mark) AS avg_mark
FROM marks m
         JOIN students s ON m.student_id = s.student_id
GROUP BY s.student_id, s.student_name
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




