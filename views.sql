create view person_add as 
select citizen.aadhar , firstname , city , phone_no
from citizen , address 
where citizen.aadhar = address.aadhar ;

select * from person_add ;