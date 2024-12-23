-- Define Enum Types
CREATE TYPE day AS ENUM ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday');

-- Teacher Table
CREATE TABLE teacher (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL
);

-- Specialization Table
CREATE TABLE specialization (
    id SERIAL PRIMARY KEY,
    specialization VARCHAR(255),
    teacher_id INTEGER,
    FOREIGN KEY (teacher_id) REFERENCES teacher(id) ON DELETE CASCADE
);

-- Class Table
CREATE TABLE class (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL NOT NULL,
    teacher_id INTEGER,  -- Reference to the teacher
    FOREIGN KEY (teacher_id) REFERENCES teacher(id) ON DELETE CASCADE
);

-- Time Table
CREATE TABLE time_table (
    id SERIAL PRIMARY KEY,
    class_id INTEGER NOT NULL,  -- Reference to the class
    day day NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    FOREIGN KEY (class_id) REFERENCES class(id) ON DELETE CASCADE
);

-- Student Table
CREATE TABLE student (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    birthday DATE
);

-- Enrollment Table
CREATE TABLE enrollment (
    student_id INTEGER NOT NULL,
    class_id INTEGER NOT NULL,
    enrollment_date DATE NOT NULL,
    PRIMARY KEY (student_id, class_id),
    FOREIGN KEY (student_id) REFERENCES student(id) ON DELETE CASCADE,
    FOREIGN KEY (class_id) REFERENCES class(id) ON DELETE CASCADE
);

-- Assignment Table
CREATE TABLE assignment (
    teacher_id INTEGER NOT NULL,
    class_id INTEGER NOT NULL,
    assignment_date DATE NOT NULL,
    PRIMARY KEY (teacher_id, class_id),
    FOREIGN KEY (teacher_id) REFERENCES teacher(id) ON DELETE CASCADE,
    FOREIGN KEY (class_id) REFERENCES class(id) ON DELETE CASCADE
);

-- Payment Table
CREATE TABLE payment (
    id SERIAL PRIMARY KEY,
    student_id INTEGER NOT NULL,
    class_id INTEGER NOT NULL,
    amount DECIMAL NOT NULL,
    payment_date DATE NOT NULL,
    status VARCHAR(50),
    FOREIGN KEY (student_id, class_id) REFERENCES enrollment(student_id, class_id) ON DELETE CASCADE
);
