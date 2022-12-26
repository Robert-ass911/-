CREATE TABLE Excursions(
    Excursion_id INTEGER NOT NULL PRIMARY KEY,
    Time_of_the_event VARCHAR(40)  NOT NULL,
    Chart VARCHAR(50),
    cost VARCHAR(50)
);

CREATE TABLE Exhibits(
    Exhibit_id INTEGER NOT NULL PRIMARY KEY,
    Name VARCHAR(50) NOT NULL,
    Quantity VARCHAR(50) NOT NULL,
    Date_of_receipt VARCHAR(50) NOT NULL,
    Condition VARCHAR(50) NOT NULL,
    author VARCHAR(50) NOT NULL,
    material INTEGER NOT NULL,
    FOREIGN KEY (material) REFERENCES material(id)
);

CREATE TABLE Schedule(
    Schedule_id INTEGER NOT NULL PRIMARY KEY,
    Work schedule VARCHAR(50) NOT NULL,
    time_of_the_event VARCHAR(50) NOT NULL,
    Pavilion VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE Job_Title(
    Job_Title_id INTEGER NOT NULL PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE Services(
    Service_id INTEGER NOT NULL PRIMARY KEY,
    name VARCHAR(50),
    Price VARCHAR(50)
);

CREATE TABLE staff(
    Personnel_id INTEGER PRIMARY KEY,
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

INSERT INTO post(id, name) VALUES (1, 'Admin'), (2, "Director");
INSERT INTO users(id, login, password, post) VALUES (1, 'admin', 'admin', 1);