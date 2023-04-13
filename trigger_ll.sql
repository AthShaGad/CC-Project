DELIMITER $$ 
create trigger check_valid_ll 
before UPDATE 
on ll for each row 
begin
declare error_msg varchar(255);
declare my_date date;

SET my_date = (select ll_date from ll where aadhar = new.aadhar);
set error_msg=("Not eligible for license");

IF(TIMESTAMPDIFF(MONTH , my_date , NOW()) < 1) then 
SIGNAL SQLSTATE '42000'
SET MESSAGE_TEXT = error_msg;
end if;
end $$
DELIMITER ;