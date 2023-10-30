# Database Activities on Friday 27th

> Today, we delved into database technology and transactions, gaining valuable insights into ACID principles.

> This knowledge was applied in a practical business analytics project for a local bookstore. The project encompassed crucial steps, including thorough preparation, structured meeting agendas, data requirement identification, and robust security measures.

> We focused on generating insightful reports, establishing clear timelines, and meticulously documenting project requirements using Markdown on GitHub. The technical implementation involved database design, configuring RDMS (MariaDB and MySQL) on a Linux platform, creating essential tables, and proficiently querying the database using SQL.

> This immersive experience significantly elevated our expertise in database management and application development.

**We then created a database on our systems using mariadb, using the commands as follows:**

> sudo apt update
> sudo apt install mariadb-server
> sudo mariadb --version
> sudo service mysql start
> sudo mariadb

**Lastly, we created a table in mariadb with the following syntax:**

> CREATE TABLE aws (id INTEGER PRIMARY KEY,
> first_name VARCHAR(20),
> last_name VARCHAR(20),
> address VARCHAR(50),
> phone_no VARCHAR(10),
> );

## What is A Database?

> A database is an organized collection of structured information, or data, typically stored electronically in a computer system.

> A database is usually controlled by a database management system (DBMS). Together, the data and the DBMS, along with the applications that are associated with them, are referred to as a database system, often shortened to just databases.

## What is a Relational Database?

> A relational database is a type of database that stores and provides access to data points that are related to one another.

> Relational databases are based on the relational model, an intuitive, straightforward way of representing data in tables. In a relational database, each row in the table is a record with a unique ID called the key.

> The columns of the table hold attributes of the data, and each record usually has a value for each attribute, making it easy to establish the relationships among data points.

## What are Non-relational Databases?

> Non-relational databases (often called NoSQL databases) are different from traditional relational databases in that they store their data in a non-tabular form.

> Instead, non-relational databases might be based on data structures like documents. A document can be highly detailed while containing a range of different types of information in different formats.

> This ability to digest and organize various types of information side by side makes non-relational databases much more flexible than relational databases.

## What are Database Management Systems?

> Database Management Systems (DBMS) are software systems used to store, retrieve, and run queries on data.

> A DBMS serves as an interface between an end-user and a database, allowing users to create, read, update, and delete data in the database.

:smile: :cd:
