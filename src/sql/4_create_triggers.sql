create or replace function create_payment_for_delayed_return() 
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
language plpgsql
;

;
drop trigger if exists fine_for_delayed_return on library.loan; 
create trigger fine_for_delayed_return
after update on library.loan
for each row
execute function create_payment_for_delayed_return(); 