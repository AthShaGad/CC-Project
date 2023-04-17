DELIMITER $$ 
create trigger check_valid_dl 
before INSERT 
on dl for each row 
begin
declare error_msg varchar(255);
DECLARE k char(1) ;
DECLARE r char(1);--
set r=(select dl_status from driving_test where aadhar=new.aadhar);
set k = (select ll_status from ll where aadhar=new.aadhar);
set error_msg=("No valid learner's license exists");
if k=0 OR r=0 then
    SIGNAL SQLSTATE '42000'

SET MESSAGE_TEXT=error_msg;
end if;
end $$
DELIMITER ;