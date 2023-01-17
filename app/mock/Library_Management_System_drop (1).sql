-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2023-01-14 21:36:56.624

-- foreign keys
ALTER TABLE library.address
    DROP CONSTRAINT adres_osoba;

ALTER TABLE library.book_author
    DROP CONSTRAINT autor_autor_ksiazka;

ALTER TABLE library.payment
    DROP CONSTRAINT czlonek_oplata;

ALTER TABLE library.member
    DROP CONSTRAINT czlonek_osoba;

ALTER TABLE library.book_author
    DROP CONSTRAINT ksiazka_autor_ksiazka;

ALTER TABLE library.book_genre
    DROP CONSTRAINT ksiazka_gatunek_gatunek;

ALTER TABLE library.book_genre
    DROP CONSTRAINT ksiazka_gatunek_ksiazka;

ALTER TABLE library.payment
    DROP CONSTRAINT oplata_pracownik;

ALTER TABLE library.librarian
    DROP CONSTRAINT pracownik_osoba;

ALTER TABLE library.librarian
    DROP CONSTRAINT pracownik_pracownik;

ALTER TABLE library.loan
    DROP CONSTRAINT wypozyczenia_czlonek;

ALTER TABLE library.loan
    DROP CONSTRAINT wypozyczenie_ksiazka;

ALTER TABLE library.loan
    DROP CONSTRAINT wypozyczenie_pracownik;

-- tables
DROP TABLE library.address;

DROP TABLE library.author;

DROP TABLE library.book;

DROP TABLE library.book_author;

DROP TABLE library.book_genre;

DROP TABLE library.genre;

DROP TABLE library.librarian;

DROP TABLE library.loan;

DROP TABLE library.member;

DROP TABLE library.payment;

DROP TABLE library.person;

-- End of file.

