-- DELIMITER $$
-- CREATE FUNCTION pin_code(cd varchar)
-- RETURNS INT
-- begin
-- -- declare cnt int;
-- return (select count(*) from citizen where state_code = cd);
-- end $$
-- DELIMITER ;

-- DELIMITER $$
-- CREATE FUNCTION count_citizens(cnt int)
-- RETURNS varchar(500)
-- DETERMINISTIC
-- BEGIN
-- DECLARE msg varchar(500);
-- set msg = "test";
-- if (cnt>0) then
--     SET msg = "you had a lot of citizens.";
-- else
--     SET msg = "you had no citizens.";
-- end if;
-- return msg;
-- END; $$
-- DELIMITER ;

DELIMITER $$
CREATE FUNCTION total_count()
RETURNS INT
begin
-- declare cnt int;
return (select count(*) from citizen );
end $$
DELIMITER ;


DELIMITER $$
CREATE FUNCTION state_code(cd varchar(255))
RETURNS INT
begin
-- declare cnt int;
return (select count(*) from address where state_code = cd);
end
$$
DELIMITER ;
