-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2023-01-13 19:09:46.948

-- foreign keys
ALTER TABLE library.adres
    DROP CONSTRAINT adres_osoba;

ALTER TABLE library.autor_ksiazka
    DROP CONSTRAINT autor_autor_ksiazka;

ALTER TABLE library.oplata
    DROP CONSTRAINT czlonek_oplata;

ALTER TABLE library.czlonek
    DROP CONSTRAINT czlonek_osoba;

ALTER TABLE library.autor_ksiazka
    DROP CONSTRAINT ksiazka_autor_ksiazka;

ALTER TABLE library.ksiazka_gatunek
    DROP CONSTRAINT ksiazka_gatunek_gatunek;

ALTER TABLE library.ksiazka_gatunek
    DROP CONSTRAINT ksiazka_gatunek_ksiazka;

ALTER TABLE library.oplata
    DROP CONSTRAINT oplata_pracownik;

ALTER TABLE library.pracownik
    DROP CONSTRAINT pracownik_osoba;

ALTER TABLE library.pracownik
    DROP CONSTRAINT pracownik_pracownik;

ALTER TABLE library.wypozyczenie
    DROP CONSTRAINT wypozyczenia_czlonek;

ALTER TABLE library.wypozyczenie
    DROP CONSTRAINT wypozyczenie_ksiazka;

ALTER TABLE library.wypozyczenie
    DROP CONSTRAINT wypozyczenie_pracownik;

-- tables
DROP TABLE library.adres;

DROP TABLE library.autor;

DROP TABLE library.autor_ksiazka;

DROP TABLE library.czlonek;

DROP TABLE library.gatunek;

DROP TABLE library.ksiazka;

DROP TABLE library.ksiazka_gatunek;

DROP TABLE library.oplata;

DROP TABLE library.osoba;

DROP TABLE library.pracownik;

DROP TABLE library.wypozyczenie;

-- End of file.

