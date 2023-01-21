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