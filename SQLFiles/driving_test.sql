DELIMITER $$
create trigger driving_test
before INSERT
on dl for each row
begin
declare error_msg varchar(255);
DECLARE k char(1) ;
set k = (select dl_status from driving_test where aadhar=new.aadhar);
set error_msg=("Person has failed driving test");
if k=0 then
    SIGNAL SQLSTATE '42000'

SET MESSAGE_TEXT=error_msg;
end if;
end $$
DELIMITER ;