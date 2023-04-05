use db;

CREATE TABLE INFO(
    _ID int not null AUTO_INCREMENT,
    _NAME varchar(100) NOT NULL,
    _EMAIL varchar(100) NOT NULL,
    _PHONENUMBER varchar(100) NOT NULL,
    _MESSAGE varchar(100) NOT NULL,
    PRIMARY KEY (_ID)
);