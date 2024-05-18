-- File generated with SQLiteStudio v3.4.4 on �� ��� 14 17:18:26 2024
--
-- Text encoding used: System
--

BEGIN TRANSACTION;

-- Table: fields_record
CREATE TABLE IF NOT EXISTS fields_record (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    email VARCHAR(254) NOT NULL,
    homepage VARCHAR(200) NULL,
    text TEXT NOT NULL,
    created_at DATETIME NOT NULL,
    parent_comment_id BIGINT NULL,
    FOREIGN KEY (parent_comment_id) REFERENCES fields_record (id)
);

INSERT INTO fields_record (id, username, email, homepage, text, created_at, parent_comment_id) VALUES
(7, 'Bob', 'Email@emai.com', '', 'Leucippus was a Greek philosopher of the 5th century BCE. He is credited with founding atomism, with his student Democritus. Leucippus divided the world into two entities: atoms, indivisible particles that make up all things, and the void, the nothingness between the atoms. Leucippus''s ideas were influential in ancient and Renaissance philosophy. They were a precursor to modern atomic theory, but the two are only superficially similar. Leucippus''s atoms come in infinitely many forms, all in constant motion, creating a deterministic world created by the collisions of atoms. The soul is viewed as an arrangement of spherical atoms, cycled through the body by respiration and creating thought and sensory input. Little is known of his life, with a few scholars doubting that he existed, attributing his ideas purely to Democritus. Two works are attributed to Leucippus, The Great World System and On Mind, but all of his writing has been lost except for one sentence.', '2024-05-11 05:40:15.117330', 8),
(8, 'Bill', 'Bill@gmail.com', '', 'In the news...', '2024-05-11 05:57:37.470170', 10),
(9, 'Poly', 'Winter@gmail.com', 'http://127.0.0.1:8000/', 'Did you know ...', '2024-05-11 06:09:19.856885', 7),
(10, 'Robert', 'RobStark@gmail.com', '', 'On this day...', '2024-05-11 06:40:11.007155', NULL),
(11, 'Andre', 'Andre@gmail.com', '', 'Today''s featured picture...', '2024-05-11 06:46:16.203066', 10),
(16, 'Kate', 'Kate@gmai.com', '', 'Many Exceptions...', '2024-05-11 11:26:41.848955', 11),
(17, 'Den', 'Den@gmail.com', '', 'Eagle is the common name...', '2024-05-11 14:53:53.036965', 16),
(18, 'Ivan', 'Ivan@gmail.com', '', 'The lion (Panthera leo)...', '2024-05-11 14:54:53.193351', NULL),
(19, 'admin', 'porozovivan090@gmail.com', 'http://127.0.0.1:8000/', 'asdasdasd', '2024-05-14 06:08:43.386189', NULL),
(20, 'admin', 'porozovivan090@gmail.com', 'http://127.0.0.1:8000/', 'This is a synchronous WebSocket consumer...', '2024-05-14 06:09:17.158949', NULL),
(21, 'Igor', 'igor@gmail.com', '', 'this is a <a href="https://example.com"...', '2024-05-14 06:32:46.095512', 18),
(22, '1', '1@gmail.com', '', '1', '2024-05-14 09:10:12.929068', 19),
(23, 'admin', 'Email@emai.com', '', 'q', '2024-05-14 09:10:32.975297', NULL);

-- Index: fields_record_parent_comment_id_2c3bd719
CREATE INDEX IF NOT EXISTS fields_record_parent_comment_id_2c3bd719 ON fields_record (parent_comment_id);

COMMIT;

