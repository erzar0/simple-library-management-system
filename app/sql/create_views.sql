create or replace view library.member_all_data as 
select mem.id as id 
        ,first_name
        ,last_name
        ,pesel
        ,birth_date
        ,email
        ,join_date
        ,expiration_date
        ,city
        ,postal_code
        ,street
        ,house_number
        ,apartment_number
         from library.member mem
inner join library.person per on per.id = mem.id_person
inner join library.address addr on addr.id_person = per.id;

create or replace view library.librarian_all_data as 
select libr.id as id 
        ,first_name
        ,last_name
        ,pesel
        ,birth_date
        ,email
        ,salary
        ,job_position
        ,id_supervisor
        ,city
        ,postal_code
        ,street
        ,house_number
        ,apartment_number
         from library.librarian libr 
inner join library.person per on per.id = libr.id_person
inner join library.address addr on addr.id_person = per.id;

create or replace view library.authors_of_book as
select bk.id as id_book, a.id as id_author, a.first_name, a.last_name, a.nationality from library.book bk
inner join library.book_author ba on ba.id_book = bk.id
inner join library.author a on a.id = ba.id_author;

create or replace view library.genres_of_book as
select bk.id as id_book, g.id as id_genre, g.name from library.book bk
inner join library.book_genre bg on bg.id_book = bk.id
inner join library.genre g on g.id = bg.id_genre;


