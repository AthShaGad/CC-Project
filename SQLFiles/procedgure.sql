--
DELIMITER //
CREATE PROCEDURE GetCitizen1(IN gender varchar(1))
BEGIN
	SELECT * from citizen where citizen.gender = gender ;
END //

DELIMITER ;


call GetCitizen1("F");
call GetCitizen1("M");
--     UNION
--     select * from citizen where gender = "F";