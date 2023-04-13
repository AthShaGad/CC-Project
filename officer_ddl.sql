create table if not exists officer (officer_id int NOT NULL AUTO_INCREMENT , officer_name varchar(10) , officer_join_time date , primary key(officer_id));

insert into officer (officer_name , officer_join_time) values ("Gaurav_Mahajan" , "2022-11-12");
insert into officer (officer_name , officer_join_time) values ("Saieesh_Rao" , "2022-11-13");
insert into officer (officer_name , officer_join_time) values ("Dinesh Vijay" , "2022-11-25");


create table if not exists complaint(officer_id int , aadhar varchar(12) , C_date date , complaint TEXT , primary key(officer_id , aadhar) ,foreign key(aadhar) references citizen(aadhar) , foreign key(officer_id) references officer(officer_id));
insert into complaint values(1 , "120" , "2022-11-13" , "Rude Behavior");