create table library.address (
    id_person int  not null,
    city varchar(255)  not null,
    postal_code varchar(255)  not null,
    street varchar(255)  not null,
    house_number int  not null,
    apartment_number int  null,
    constraint address_pk primary key (id_person)
);

create table library.author (
    id serial  not null,
    first_name varchar(255)  not null,
    last_name varchar(255)  null,
    nationality varchar(255)  null,
    constraint author_pk primary key (id)
);

create table library.book (
    id serial  not null,
    isbn varchar(13)  null,
    title varchar(255)  not null,
    language varchar(255)  not null,
    publication_date date  not null,
    physical_location varchar(255)  not null,
    price int  not null,
    constraint id primary key (id)
);

create table library.book_author (
    id_author int  not null,
    id_book int  not null,
    constraint book_author_pk primary key (id_author,id_book)
);

create table library.book_genre (
    id_book int  not null,
    id_genre int  not null,
    constraint book_genre_pk primary key (id_book,id_genre)
);

create table library.genre (
    id serial  not null,
    name varchar(255)  not null,
    constraint genre_pk primary key (id)
);

create table library.librarian (
    id serial  not null,
    id_person int  not null,
    id_supervisor int  null,
    salary int  not null,
    job_position varchar(255)  not null,
    constraint librarian_pk primary key (id)
);

create table library.loan (
    id bigserial  not null,
    id_book int  not null,
    id_member int  not null,
    id_librarian int  not null,
    loan_date date  not null,
    due_date date  not null,
    return_date date  null,
    constraint loan_pk primary key (id)
);

create table library.member (
    id serial  not null,
    id_person int  not null,
    join_date date  not null,
    expiration_date date  not null,
    constraint member_pk primary key (id)
);

create table library.payment (
    id serial  not null,
    id_member int  not null,
    id_librarian int  not null,
    type varchar(255)  not null,
    to_pay int  not null,
    issue_date date  not null,
    payment_date date  null,
    constraint payment_pk primary key (id)
);

create table library.person (
    id serial  not null,
    first_name varchar(255)  not null,
    last_name varchar(255)  not null,
    pesel bigint  not null check (pesel > 9999999999 and pesel < 100000000000 ),
    birth_date date  not null,
    email varchar(255)  not null,
    constraint pesel unique (pesel) not deferrable  initially immediate,
    constraint person_pk primary key (id)
);

alter table library.address add constraint address__person
    foreign key (id_person)
    references library.person (id)  
    not deferrable 
    initially immediate
;

alter table library.book_author add constraint book_author__author
    foreign key (id_author)
    references library.author (id)  
    not deferrable 
    initially immediate
;

alter table library.book_author add constraint book_author__book
    foreign key (id_book)
    references library.book (id)  
    not deferrable 
    initially immediate
;

alter table library.book_genre add constraint book_genre__book
    foreign key (id_book)
    references library.book (id)  
    not deferrable 
    initially immediate
;

alter table library.book_genre add constraint book_genre__genre
    foreign key (id_genre)
    references library.genre (id)  
    not deferrable 
    initially immediate
;

alter table library.librarian add constraint librarian__librarian
    foreign key (id_supervisor)
    references library.librarian (id)  
    not deferrable 
    initially immediate
;

alter table library.librarian add constraint librarian__person
    foreign key (id_person)
    references library.person (id)  
    not deferrable 
    initially immediate
;

alter table library.loan add constraint loan__book
    foreign key (id_book)
    references library.book (id)  
    not deferrable 
    initially immediate
;

alter table library.loan add constraint loan__librarian
    foreign key (id_librarian)
    references library.librarian (id)  
    not deferrable 
    initially immediate
;

alter table library.loan add constraint loan__member
    foreign key (id_member)
    references library.member (id)  
    not deferrable 
    initially immediate
;

alter table library.member add constraint member__person
    foreign key (id_person)
    references library.person (id)  
    not deferrable 
    initially immediate
;

alter table library.payment add constraint payment__librarian
    foreign key (id_librarian)
    references library.librarian (id)  
    not deferrable 
    initially immediate
;

alter table library.payment add constraint payment__member
    foreign key (id_member)
    references library.member (id)  
    not deferrable 
    initially immediate
;


