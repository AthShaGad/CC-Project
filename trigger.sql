DELIMITER $$ 
create trigger check_adult 
before INSERT 
on citizen for each row 
begin
declare error_msg varchar(255);
declare age int;
set error_msg=("You're a minor");
set age=DATE_FORMAT(FROM_DAYS(DATEDIFF(NOW(),new.dob)), '%Y') + 0;
if age<18 then
SIGNAL SQLSTATE '45000'
SET MESSAGE_TEXT = error_msg;
end if;
end $$
DELIMITER ;
