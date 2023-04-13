select citizen.aadhar , firstname , city , phone_no
from citizen , address 
where citizen.aadhar = address.aadhar ;
//project

select dl_status , dl.aadhar , complaint.complaint
from dl,complaint
where dl.aadhar = complaint.aadhar ;

select * from citizen 
    where exists(
        select * from complaint where gender ="F" 
        and
        address.aadhar = citizen.aadhar
        );


select * from citizen 
    where exists(
        select * from complaint where officer_id = 1  
        and
        complaint.aadhar = citizen.aadhar
);


select * from address where aadhar IN(select aadhar from dl);

select * from citizen where aadhar IN(select aadhar from ll where ll_status = 0);



select firstname,lastname ,citizen.aadhar,gender,dob,phone_no,street,city,state_code from citizen
left outer join address on address.aadhar=citizen.aadhar;


select firstname,lastname,dl.aadhar,dob
from citizen inner join dl on dl.aadhar=citizen.aadhar;