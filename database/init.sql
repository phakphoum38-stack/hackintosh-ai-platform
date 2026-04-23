CREATE TABLE tenants (
    id SERIAL PRIMARY KEY,
    name TEXT
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    tenant_id INT,
    email TEXT
);

CREATE TABLE jobs (
    id SERIAL PRIMARY KEY,
    tenant_id INT,
    status TEXT
);
