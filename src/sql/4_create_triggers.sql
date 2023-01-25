create or replace function delayed_book_return_trigger_func() 
returns trigger
as
$$
begin
    if new.return_date > old.due_date then
        insert into library.payment 
        (id_member, id_librarian, type, to_pay, issue_date)
        values
        (old.id_member, 1, 'delayed return of book', ((new.return_date - old.due_date) * 0.1), current_date);
    end if;

    return new;
end;
$$
language plpgsql;

drop trigger if exists delayed_book_return_trigger on library.loan; 
create trigger delayed_book_return_trigger 
after update on library.loan
for each row
execute function delayed_book_return_trigger_func(); 




create or replace function impose_membership_payment_trigger_func()
returns trigger
as
$$
begin 
    insert into library.payment
        (id_member, id_librarian, type, to_pay, issue_date)
        values
        (new.id, 1, 'membership fee', 100, current_date);
    return new;
end;
$$
language plpgsql;

drop trigger if exists impose_membership_payment_trigger on library.member; 
create trigger impose_membership_payment_trigger 
after insert on library.member
for each row
execute function impose_membership_payment_trigger_func(); 

