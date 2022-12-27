CREATE TABLE Excursions(
    id INTEGER NOT NULL PRIMARY KEY,
    event VARCHAR(40)  NOT NULL,
    Chart VARCHAR(50),
    cost VARCHAR(50)
);

CREATE TABLE Exhibits(
    id INTEGER NOT NULL PRIMARY KEY,
    Name VARCHAR(50) NOT NULL,
    Quantity VARCHAR(50) NOT NULL,
    Date_of_receipt VARCHAR(50) NOT NULL,
    Condition VARCHAR(50) NOT NULL,
    author VARCHAR(50) NOT NULL,
    material INTEGER NOT NULL,
    FOREIGN KEY (material) REFERENCES material(id)
);

CREATE TABLE Schedule(
    id INTEGER NOT NULL PRIMARY KEY,
    Work schedule VARCHAR(50) NOT NULL,
    time_of_the_event VARCHAR(50) NOT NULL,
    Pavilion VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE Job_Title(
    id INTEGER NOT NULL PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE Services(
    id INTEGER NOT NULL PRIMARY KEY,
    name VARCHAR(50),
    Price VARCHAR(50)
);

CREATE TABLE staff(
    id INTEGER PRIMARY KEY,
    Full_name INTEGER NOT NULL,
    Post INTEGER,
    Salary INTEGER,
    Education INTEGER,
    Phone number INTEGER,
    FOREIGN KEY(Full_name_id) REFERENCES Full_name(id)
                  ON DELETE CASCADE ON UPDATE NO ACTION,
    FOREIGN KEY(Post_id) REFERENCES Post(id)
                  ON DELETE CASCADE ON UPDATE NO ACTION
);

INSERT INTO Job_Title(id, name)
VALUES (1, 'Main'), (2, "Secondary");

INSERT INTO Services(id, name, Price)
VALUES (1, 2, 500);

INSERT INTO Excursions(id, event, Chart, cost)
VALUES (1, 2, 3, 400);

INSERT INTO Schedule(id, Work schedule, time_of_the_event, Pavilion)
VALUES (1, 2, 16:00, 3);

INSERT INTO Exhibits(id, Name, Quantity, Date_of_receipt, Condition, author, material)
VALUES (1, 2, 3, 27.12.2001, 5, 6, 7);