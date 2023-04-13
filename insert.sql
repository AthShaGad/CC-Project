create table if not exists driving_test(dl_status char(1) ,aadhar varchar(10),primary key(aadhar),foreign key(aadhar) references citizen (aadhar));
insert into driving_test(dl_status,aadhar) values ("0","100");

insert into driving_test(dl_status,aadhar) values ("0","850");

-- aadhar =250
--aadhar =300