-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2023-01-13 20:52:46.671

-- tables
-- Table: adres
CREATE TABLE library.adres (
    id_osoba int  NOT NULL,
    miasto varchar(255)  NOT NULL,
    kod_pocztowy varchar(255)  NOT NULL,
    ulica varchar(255)  NOT NULL,
    numer_domu int  NOT NULL,
    numer_lokalu int  NULL,
    CONSTRAINT adres_pk PRIMARY KEY (id_osoba)
);

-- Table: autor
CREATE TABLE library.autor (
    id serial  NOT NULL,
    imie varchar(255)  NOT NULL,
    nazwisko varchar(255)  NULL,
    narodowosc varchar(255)  NULL,
    CONSTRAINT autor_pk PRIMARY KEY (id)
);

-- Table: autor_ksiazka
CREATE TABLE library.autor_ksiazka (
    id_autor int  NOT NULL,
    id_ksiazka int  NOT NULL,
    CONSTRAINT autor_ksiazka_pk PRIMARY KEY (id_autor,id_ksiazka)
);

-- Table: czlonek
CREATE TABLE library.czlonek (
    id int  NOT NULL,
    id_osoba int  NOT NULL,
    data_doloczenia date  NOT NULL,
    data_waznosci_czlonkostwa date  NOT NULL,
    CONSTRAINT czlonek_pk PRIMARY KEY (id)
);

-- Table: gatunek
CREATE TABLE library.gatunek (
    id serial  NOT NULL,
    nazwa varchar(255)  NOT NULL,
    CONSTRAINT gatunek_pk PRIMARY KEY (id)
);

-- Table: ksiazka
CREATE TABLE library.ksiazka (
    id serial  NOT NULL,
    isbn varchar(13)  NULL,
    tytul varchar(255)  NOT NULL,
    jezyk varchar(255)  NOT NULL,
    data_wydania date  NOT NULL,
    lokalizacja_fizyczna varchar(255)  NOT NULL,
    cena_katalogowa int  NOT NULL,
    CONSTRAINT id PRIMARY KEY (id)
);

-- Table: ksiazka_gatunek
CREATE TABLE library.ksiazka_gatunek (
    id_ksiazka int  NOT NULL,
    id_gatunek int  NOT NULL,
    CONSTRAINT ksiazka_gatunek_pk PRIMARY KEY (id_ksiazka,id_gatunek)
);

-- Table: oplata
CREATE TABLE library.oplata (
    id serial  NOT NULL,
    id_czlonek int  NOT NULL,
    id_pracownik int  NOT NULL,
    rodzaj varchar(255)  NOT NULL,
    data_wystawienia date  NOT NULL,
    do_zaplaty int  NOT NULL,
    oplacona boolean  NOT NULL,
    CONSTRAINT oplata_pk PRIMARY KEY (id)
);

-- Table: osoba
CREATE TABLE library.osoba (
    id serial  NOT NULL,
    imie varchar(255)  NOT NULL,
    nazwisko varchar(255)  NOT NULL,
    pesel bigint  NOT NULL CHECK (pesel > 9999999999 and pesel < 100000000000 ),
    data_urodzenia date  NOT NULL,
    email varchar(255)  NOT NULL,
    CONSTRAINT pesel UNIQUE (pesel) NOT DEFERRABLE  INITIALLY IMMEDIATE,
    CONSTRAINT osoba_pk PRIMARY KEY (id)
);

-- Table: pracownik
CREATE TABLE library.pracownik (
    id serial  NOT NULL,
    id_osoba int  NOT NULL,
    id_przelozony int  NULL,
    pensja int  NOT NULL,
    stanowisko varchar(255)  NOT NULL,
    CONSTRAINT pracownik_pk PRIMARY KEY (id)
);

-- Table: wypozyczenie
CREATE TABLE library.wypozyczenie (
    id bigserial  NOT NULL,
    id_ksiazka int  NOT NULL,
    id_czlonek int  NOT NULL,
    id_pracownik int  NOT NULL,
    data_wypozyczenia date  NOT NULL,
    data_oddania date  NULL,
    termin_oddania date  NOT NULL,
    oddana boolean  NOT NULL,
    CONSTRAINT wypozyczenie_pk PRIMARY KEY (id)
);

-- foreign keys
-- Reference: adres_osoba (table: adres)
ALTER TABLE library.adres ADD CONSTRAINT adres_osoba
    FOREIGN KEY (id_osoba)
    REFERENCES library.osoba (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: autor_autor_ksiazka (table: autor_ksiazka)
ALTER TABLE library.autor_ksiazka ADD CONSTRAINT autor_autor_ksiazka
    FOREIGN KEY (id_autor)
    REFERENCES library.autor (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: czlonek_oplata (table: oplata)
ALTER TABLE library.oplata ADD CONSTRAINT czlonek_oplata
    FOREIGN KEY (id_czlonek)
    REFERENCES library.czlonek (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: czlonek_osoba (table: czlonek)
ALTER TABLE library.czlonek ADD CONSTRAINT czlonek_osoba
    FOREIGN KEY (id_osoba)
    REFERENCES library.osoba (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: ksiazka_autor_ksiazka (table: autor_ksiazka)
ALTER TABLE library.autor_ksiazka ADD CONSTRAINT ksiazka_autor_ksiazka
    FOREIGN KEY (id_ksiazka)
    REFERENCES library.ksiazka (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: ksiazka_gatunek_gatunek (table: ksiazka_gatunek)
ALTER TABLE library.ksiazka_gatunek ADD CONSTRAINT ksiazka_gatunek_gatunek
    FOREIGN KEY (id_gatunek)
    REFERENCES library.gatunek (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: ksiazka_gatunek_ksiazka (table: ksiazka_gatunek)
ALTER TABLE library.ksiazka_gatunek ADD CONSTRAINT ksiazka_gatunek_ksiazka
    FOREIGN KEY (id_ksiazka)
    REFERENCES library.ksiazka (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: oplata_pracownik (table: oplata)
ALTER TABLE library.oplata ADD CONSTRAINT oplata_pracownik
    FOREIGN KEY (id_pracownik)
    REFERENCES library.pracownik (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: pracownik_osoba (table: pracownik)
ALTER TABLE library.pracownik ADD CONSTRAINT pracownik_osoba
    FOREIGN KEY (id_osoba)
    REFERENCES library.osoba (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: pracownik_pracownik (table: pracownik)
ALTER TABLE library.pracownik ADD CONSTRAINT pracownik_pracownik
    FOREIGN KEY (id_przelozony)
    REFERENCES library.pracownik (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: wypozyczenia_czlonek (table: wypozyczenie)
ALTER TABLE library.wypozyczenie ADD CONSTRAINT wypozyczenia_czlonek
    FOREIGN KEY (id_czlonek)
    REFERENCES library.czlonek (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: wypozyczenie_ksiazka (table: wypozyczenie)
ALTER TABLE library.wypozyczenie ADD CONSTRAINT wypozyczenie_ksiazka
    FOREIGN KEY (id_ksiazka)
    REFERENCES library.ksiazka (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: wypozyczenie_pracownik (table: wypozyczenie)
ALTER TABLE library.wypozyczenie ADD CONSTRAINT wypozyczenie_pracownik
    FOREIGN KEY (id_pracownik)
    REFERENCES library.pracownik (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- End of file.

