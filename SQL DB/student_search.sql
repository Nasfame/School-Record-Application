select std.name from student as std join section as s on s.id = std.section_id  join teacher as t on s.teacher_id = t.id where t.name ='Parth';