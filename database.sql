CREATE TYPE specialization AS ENUM ('Tahfidh', 'Ahkam');
CREATE TYPE day AS ENUM('monday','tuesday','wednesday','thursday','friday','satuday','sunday');
create table teacher(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    specialization specialization[]
);
create table time_table(
    id SERIAL PRIMARY KEY,
    'day' day,
    start_time TIMESTAMP,
    end_time TIMESTAMP,
    FOREIGN KEY (class_id) REFERENCES class(id)
);

CREATE TABLE class (
    class_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL NOT NULL,
    Foreign Key (id)  REFERENCES teacher (id),
    Foreign Key (id)  REFERENCES time_table (id)
);
CREATE TABLE student (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    birthday Date,
    price DECIMAL NOT NULL,
    FOREIGN Key (id)  REFERENCES TimeTable (time_id)
);
CREATE TABLE enrolement (
    'date' Date  NOT NULL,
    PRIMARY KEY (student_id, class_id),
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (class_id) REFERENCES class(id)
CREATE TABLE assignement (
    'date' Date  NOT NULL,
    PRIMARY KEY (teacher_id, class_id),
    FOREIGN KEY (teacher_id) REFERENCES teacher(id),
    FOREIGN KEY (course_id) REFERENCES courses(id)
);
CREATE TABLE payment (
    PRIMARY KEY (enrolement_is, student_id),
    enrollment_id INT NOT NULL,          -- Foreign key referencing the enrollment
    amount DECIMAL NOT NULL,             -- Amount of the payment
    payment_date DATE NOT NULL,          -- Date of the payment
    status VARCHAR(50),                  -- Status of the payment (e.g., completed, pending)
    FOREIGN KEY (enrollment_id) REFERENCES enrollment(student_id, class_id),  -- Composite foreign key
    FOREIGN KEY (student_id) REFERENCES students(id)  -- Direct reference to students
);

    
    
