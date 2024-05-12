CREATE SCHEMA IF NOT EXISTS ehc_prototype;

USE ehc_prototype;

CREATE TABLE IF NOT EXISTS Owner (
    owner_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    contact_information VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS Model (
    id INT AUTO_INCREMENT PRIMARY KEY,
    description VARCHAR(255),
    application_areas VARCHAR(255),
    params VARCHAR(255),
    metrics VARCHAR(255),
    confidence VARCHAR(255),
    owner_id INT,
    last_update_timestamp DATETIME,
    FOREIGN KEY (owner_id) REFERENCES Owner(owner_id)
);

CREATE TABLE IF NOT EXISTS Dataset (
    dataset_id INT AUTO_INCREMENT PRIMARY KEY,
    description VARCHAR(255),
    format VARCHAR(255),
    size DOUBLE
);

CREATE TABLE IF NOT EXISTS Metric (
    metric_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    value DOUBLE
);

CREATE TABLE IF NOT EXISTS ModelDataset (
    model_id INT,
    dataset_id INT,
    FOREIGN KEY (model_id) REFERENCES Model(id),
    FOREIGN KEY (dataset_id) REFERENCES Dataset(dataset_id),
    PRIMARY KEY (model_id, dataset_id)
);

CREATE TABLE IF NOT EXISTS ModelMetric (
    model_id INT,
    metric_id INT,
    FOREIGN KEY (model_id) REFERENCES Model(id),
    FOREIGN KEY (metric_id) REFERENCES Metric(metric_id),
    PRIMARY KEY (model_id, metric_id)
);
-- Inserting records into the Owner table
INSERT INTO Owner (name, contact_information) VALUES
('John Doe', 'john.doe@example.com'),
('Jane Smith', 'jane.smith@example.com');

-- Inserting records into the Model table
INSERT INTO Model (description, application_areas, params, metrics, confidence, owner_id, last_update_timestamp) VALUES
('Model 1', 'Image Recognition', 'param1=value1', 'metric1=value1', 'High', 1, NOW()),
('Model 2', 'Natural Language Processing', 'param2=value2', 'metric2=value2', 'Medium', 2, NOW());

-- Inserting records into the Dataset table
INSERT INTO Dataset (description, format, size) VALUES
('Dataset 1', 'CSV', 1024),
('Dataset 2', 'JSON', 2048);

-- Inserting records into the Metric table
INSERT INTO Metric (name, value) VALUES
('Accuracy', 0.95),
('Precision', 0.85);

-- Inserting records into the ModelDataset table
INSERT INTO ModelDataset (model_id, dataset_id) VALUES
(1, 1),
(2, 2);

-- Inserting records into the ModelMetric table
INSERT INTO ModelMetric (model_id, metric_id) VALUES
(1, 1),
(2, 2);

