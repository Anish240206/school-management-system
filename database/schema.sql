-- School Management System
-- Relational schema for the modern web application
-- MySQL 8.0+

CREATE DATABASE IF NOT EXISTS school_management
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE school_management;

CREATE TABLE users (
    user_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    role ENUM('ADMIN', 'TEACHER') NOT NULL DEFAULT 'TEACHER',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

CREATE TABLE teachers (
    teacher_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    teacher_code VARCHAR(20) NOT NULL UNIQUE,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50),
    subject VARCHAR(100) NOT NULL,
    salary DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
    address VARCHAR(255),
    phone VARCHAR(20),
    user_id BIGINT UNSIGNED UNIQUE,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_teachers_user
        FOREIGN KEY (user_id) REFERENCES users(user_id)
        ON DELETE SET NULL ON UPDATE CASCADE,

    CONSTRAINT chk_teacher_salary CHECK (salary >= 0)
) ENGINE=InnoDB;

CREATE TABLE classes (
    class_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    grade TINYINT UNSIGNED NOT NULL,
    section VARCHAR(5) NOT NULL,
    academic_year VARCHAR(9) NOT NULL,
    room_number VARCHAR(20),
    class_teacher_id BIGINT UNSIGNED,

    CONSTRAINT uq_class UNIQUE (grade, section, academic_year),

    CONSTRAINT fk_classes_teacher
        FOREIGN KEY (class_teacher_id) REFERENCES teachers(teacher_id)
        ON DELETE SET NULL ON UPDATE CASCADE,

    CONSTRAINT chk_class_grade CHECK (grade BETWEEN 1 AND 12)
) ENGINE=InnoDB;

CREATE TABLE students (
    student_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    roll_number VARCHAR(20) NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50),
    date_of_birth DATE,
    address VARCHAR(255),
    phone VARCHAR(20),
    class_id BIGINT UNSIGNED NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT uq_student_roll UNIQUE (class_id, roll_number),

    CONSTRAINT fk_students_class
        FOREIGN KEY (class_id) REFERENCES classes(class_id)
        ON DELETE RESTRICT ON UPDATE CASCADE,

    INDEX idx_students_name (last_name, first_name),
    INDEX idx_students_class (class_id)
) ENGINE=InnoDB;

CREATE TABLE student_attendance (
    attendance_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    student_id BIGINT UNSIGNED NOT NULL,
    attendance_date DATE NOT NULL,
    status ENUM('PRESENT', 'ABSENT', 'LATE', 'EXCUSED') NOT NULL DEFAULT 'PRESENT',

    CONSTRAINT uq_student_attendance UNIQUE (student_id, attendance_date),

    CONSTRAINT fk_student_attendance_student
        FOREIGN KEY (student_id) REFERENCES students(student_id)
        ON DELETE CASCADE ON UPDATE CASCADE,

    INDEX idx_student_attendance_date (attendance_date)
) ENGINE=InnoDB;

CREATE TABLE teacher_attendance (
    attendance_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    teacher_id BIGINT UNSIGNED NOT NULL,
    attendance_date DATE NOT NULL,
    status ENUM('PRESENT', 'ABSENT', 'LATE', 'EXCUSED') NOT NULL DEFAULT 'PRESENT',

    CONSTRAINT uq_teacher_attendance UNIQUE (teacher_id, attendance_date),

    CONSTRAINT fk_teacher_attendance_teacher
        FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id)
        ON DELETE CASCADE ON UPDATE CASCADE,

    INDEX idx_teacher_attendance_date (attendance_date)
) ENGINE=InnoDB;

CREATE TABLE fee_structure (
    fee_structure_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    class_id BIGINT UNSIGNED NOT NULL,
    school_fee DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
    bus_fee DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
    excursion_fee DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
    tech_fee DECIMAL(10, 2) NOT NULL DEFAULT 0.00,

    CONSTRAINT uq_fee_structure
        UNIQUE (class_id),

    CONSTRAINT fk_fee_structure_class
        FOREIGN KEY (class_id)
        REFERENCES classes(class_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    CONSTRAINT chk_school_fee
        CHECK (school_fee >= 0),

    CONSTRAINT chk_bus_fee
        CHECK (bus_fee >= 0),

    CONSTRAINT chk_excursion_fee
        CHECK (excursion_fee >= 0),

    CONSTRAINT chk_tech_fee
        CHECK (tech_fee >= 0)
) ENGINE=InnoDB;

CREATE TABLE books (
    book_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    isbn VARCHAR(20) UNIQUE,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(150) NOT NULL,
    publisher VARCHAR(150),
    genre VARCHAR(100),
    total_copies INT UNSIGNED NOT NULL DEFAULT 1,
    available_copies INT UNSIGNED NOT NULL DEFAULT 1,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT chk_book_copies CHECK (available_copies <= total_copies),

    INDEX idx_books_title (title),
    INDEX idx_books_author (author)
) ENGINE=InnoDB;

CREATE TABLE library_transactions (
    transaction_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    book_id BIGINT UNSIGNED NOT NULL,
    student_id BIGINT UNSIGNED NOT NULL,
    issued_date DATE NOT NULL,
    due_date DATE NOT NULL,
    returned_date DATE,
    status ENUM('ISSUED', 'RETURNED', 'OVERDUE') NOT NULL DEFAULT 'ISSUED',

    -- Default late fee: INR 1 per late day per book.
    -- The backend calculates the final penalty when the book is returned.
    late_fee_per_day DECIMAL(10, 2) NOT NULL DEFAULT 1.00,
    penalty_amount DECIMAL(10, 2) NOT NULL DEFAULT 0.00,

    CONSTRAINT fk_library_transaction_book
        FOREIGN KEY (book_id) REFERENCES books(book_id)
        ON DELETE RESTRICT ON UPDATE CASCADE,

    CONSTRAINT fk_library_transaction_student
        FOREIGN KEY (student_id) REFERENCES students(student_id)
        ON DELETE RESTRICT ON UPDATE CASCADE,

    CONSTRAINT chk_library_dates CHECK (due_date >= issued_date),
    CONSTRAINT chk_library_penalty CHECK (late_fee_per_day >= 0 AND penalty_amount >= 0),

    INDEX idx_library_student (student_id),
    INDEX idx_library_book (book_id),
    INDEX idx_library_status (status)
) ENGINE=InnoDB;

CREATE TABLE fee_payments (
    payment_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    student_id BIGINT UNSIGNED NOT NULL,
    payment_type ENUM(
        'SCHOOL_FEE',
        'BUS_FEE',
        'EXCURSION_FEE',
        'TECH_FEE',
        'LIBRARY_PENALTY'
    ) NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_date DATE NOT NULL,
    payment_method ENUM('CASH', 'CARD', 'UPI', 'BANK_TRANSFER', 'OTHER') NOT NULL,
    academic_year VARCHAR(9),
    library_transaction_id BIGINT UNSIGNED,
    status ENUM('PAID', 'REFUNDED', 'CANCELLED') NOT NULL DEFAULT 'PAID',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_fee_payment_student
        FOREIGN KEY (student_id) REFERENCES students(student_id)
        ON DELETE RESTRICT ON UPDATE CASCADE,

    CONSTRAINT fk_fee_payment_library_transaction
        FOREIGN KEY (library_transaction_id)
        REFERENCES library_transactions(transaction_id)
        ON DELETE SET NULL ON UPDATE CASCADE,

    CONSTRAINT chk_payment_amount CHECK (amount > 0),

    INDEX idx_fee_payments_student (student_id),
    INDEX idx_fee_payments_date (payment_date),
    INDEX idx_fee_payments_type (payment_type)
) ENGINE=InnoDB;
