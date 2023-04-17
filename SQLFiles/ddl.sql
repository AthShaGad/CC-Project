create table if not exists citizen(
    firstname varchar(30),
    lastname varchar(30),
    aadhar varchar(12),
    gender char(1),
    dob DATE ,
    phone_no varchar(12),
    PRIMARY KEY (aadhar)
    ); 

create table if not exists complaint(
    officer_id int, 
    aadhar varchar(12), 
    C_date date, 
    compaint TEXT, 
    primary key(officer_id , aadhar),
    foreign key(aadhar) references citizen(aadhar) 
    ON DELETE CASCADE ON UPDATE CASCADE, 
    foreign key(officer_id) references officer(officer_id)
    ON DELETE CASCADE ON UPDATE CASCADE
    );

insert into complaint values(1 , "250" , "2022-11-13" , "Testing Complaint");

create table if not exists officer(
    officer_id int NOT NULL AUTO_INCREMENT,
    officer_name varchar(10), 
    officer_join_time date, 
    primary key(officer_id));

insert into officer (officer_name , officer_join_time) values ("Saptarshi" , "2022-11-12");
insert into officer (officer_name , officer_join_time) values ("Souymoroop" , "2022-11-13");

create table if not exists address(
    aadhar varchar(10),
    street varchar(50),
    city varchar(30),
    state_code varchar(30),
    primary key(aadhar),
    foreign key(aadhar) references citizen(aadhar) 
    ON DELETE CASCADE ON UPDATE CASCADE
    );

create table if not exists ll(
    ll_id int NOT NULL AUTO_INCREMENT, 
    ll_status char(1), 
    ll_date date,
    aadhar varchar(10), 
    primary key(ll_id),
    foreign key(aadhar) references citizen(aadhar)
    ON DELETE CASCADE ON UPDATE CASCADE
    );

create table if not exists dl(
    dl_id int NOT NULL AUTO_INCREMENT, 
    dl_status char(1), 
    dl_date date  ,
    aadhar varchar(10), 
    primary key(dl_id), 
    foreign key (aadhar) references  citizen (aadhar)
    ON DELETE CASCADE ON UPDATE CASCADE
    );
