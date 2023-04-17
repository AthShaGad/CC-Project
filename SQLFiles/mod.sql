

select * from ll  minus
select * from ll inner join dl on ll.aadhar=dl.aadhar;


select firstname  from citizen natural join (select  aadhar from ll except select aadhar from dl) ;



-- aadhars virtual table
create  or replace view aadhars as
select  aadhar from ll
except
select aadhar from dl;


DELIMITER //
CREATE PROCEDURE class_mod()
BEGIN
	select firstname,lastname,citizen.aadhar from citizen natural join aadhars;
END //

DELIMITER ;