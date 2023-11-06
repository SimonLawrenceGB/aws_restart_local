# Databases Fact Finding

## Python Fact Finding Exercise

![alt text](https://www.researchgate.net/profile/Khaled-Nagaty/publication/237062986/figure/fig10/AS:614291111673856@1523469822085/shows-the-iconic-logo-of-the-Python-programming-language-Python-Software-Foundation.png)

**1.What are a list and tuple in Python, and what are some examples?**

> List is a collection which is ordered and changeable. Allows duplicate members. Tuple is a collection which is ordered and unchangeable.

**2.What is a namespace in Python?**

> Namespaces in Python. A namespace is a collection of currently defined symbolic names along with information about the object that each name references

**3.What is the difference between a local variable and a global variable?**

> A global variable is one that is “declared” outside of the functions in a program and can, therefore, be accessed by any of the functions. A local variable is declared inside a specific function and can only be accessed by the function in which it is declared.

**4.What is an IDE, and what are some common IDEs that could be used with Python?**

> An integrated development environment (IDE) refers to a software application that offers computer programmers with extensive software development abilities

**5.What are modules in Python, and what are some examples?**

> In Python, Modules are simply files with the “. py” extension containing Python code that can be imported inside another Python Program.

**6.What is the difference between an array and a list?**

> Lists and arrays both are mutable and store ordered items. List can store elements of different types, but arrays can store elements only of the same type.

**7.What are operators, and what are some examples?**

> Operators are special symbols that perform operations on variables and values. For example,

| Operator | Operation                 | Example            |
| -------- | ------------------------- | ------------------ |
| +        | Addition                  | 5 + 2 = 7          |
| -        | Subtraction               | 4 - 2 = 2          |
| \*       | Multiplication            | 2 \* 3 = 6         |
| /        | Division                  | 4 / 2 = 2          |
| =        | Assignment Operator       | a = 7              |
| +=       | Addition Assignment       | a += 1 # a = a + 1 |
| -=       | Subtraction Assignment    | a -= 3 # a = a - 3 |
| \*=      | Multiplication Assignment | a \_= 4 # a = a_4  |

## Databases Fact Finding Exercise

**1.What is the difference between a relational and a non-relational database?**

> Relational databases store data in rows and columns like a spreadsheet while non-relational databases store data don't, using a storage model (one of four) that is best suited for the type of data it's storing.

**2.What are indexes?**

> Index is a pointer to data in a table. An index in a database is very similar to an index in the back of a book.

**3.What are primary key sand secondary keys?**

> A primary key is the field in a database that is the primary key used to uniquely identify a record in a database. A secondary key is an additional key, or alternate key, which can be use in addition to the primary key to locate specific data.

**4.What are inner join sand outer joins?**

> INNER JOIN returns the common and the matching records between the tables. OUTER JOIN returns all the records from the database tables.

**5.What is the difference between DROP TABLE and TRUNCATE TABLE?**

> the DROP command is used to remove the whole database or table indexes, data, and more. Whereas the TRUNCATE command is used to remove all the rows from the table.

**6.What are the different data types in SQL?**

- Numeric data types such as: INT, TINYINT, BIGINT, FLOAT, REAL, etc.
- Date and Time data types such as: DATE, TIME, DATETIME, etc.
- Character and String data types such as: CHAR, VARCHAR, TEXT, etc.
- Unicode character string data types such as: NCHAR, NVARCHAR, NTEXT etc.
- Binary data types such as: BINARY, VARBINARY, etc.
- Miscellaneous data types - CLOB, BLOB, XML, CURSOR, TABLE, etc.

**7.What are the WHERE and HAVING clauses used for?**

> filter the records from the table based on the specified condition. HAVING Clause is used to filter record from the groups based on the specified condition.

## AWS Cloud Foundations Part 1 fact-finding exercise

![alt text](https://upload.wikimedia.org/wikipedia/commons/1/1d/AmazonWebservices_Logo.svg)

**1.What are IaaS, PaaS, and SaaS?**

- IaaS (Infrastructure as a Service): Virtualized infrastructure resources.
- PaaS (Platform as a Service): Application development platform.
- SaaS (Software as a Service): Fully functional software applications.

**2.What are the advantages of cloud computing?**
The advantages of cloud computing are:

- Cost savings
- Scalability
- Accessibility
- Reliability
- Security
- Automated maintenance
- Disaster recovery
- Collaboration
- Eco-friendly
- Innovation
- Global reach
- Reduced IT overhead

**3.What is an AWS region?**

> An AWS Region is a geographic area with multiple data centers that offers redundancy, fault tolerance, and low-latency connections for hosting AWS services and resources.

**4.What is an Availability Zone?**

> An Availability Zone (AZ) is an isolated data center within an AWS Region, providing redundancy and fault tolerance for AWS services and resources.

**5.What are all the AWS regions?**

- US East (North Virginia)
- US East (Ohio)
- US West (North California)
- US West (Oregon)
- Canada (Central)
- South America (Sao Paulo)
- EU (Ireland)
- EU (London)
- EU (Frankfurt)
- EU (Paris)
- EU (Stockholm)
- Asia Pacific (Mumbai)
- Asia Pacific (Seoul)
- Asia Pacific (Singapore)
- Asia Pacific (Sydney)
- Asia Pacific (Tokyo)
- China (Beijing)
- China (Ningxia)
- Middle East (Bahrain)
- Africa (Cape Town)

**6.What are the categories in which AWS services are grouped?**

> AWS services are grouped into categories like Compute, Storage, Databases, Networking, and more, based on their primary functions and use cases.

**7.What is the difference between object storage and block storage?**

> Object storage is for unstructured data (e.g., images, videos) with associated metadata, scalable, and accessed via HTTP.

> Block storage is for structured data (e.g., databases), offers better performance, and may need a file system.

**8.What are two AWS cloud compute services and what do they do?**

> Amazon EC2: Provides scalable virtual servers for running applications and hosting web services.

> AWS Lambda: Offers serverless, event-driven computing for automating tasks and microservices without server management.

**9.What are the two AWS storage services and what do they do?**

> Amazon S3: Stores objects like documents and media, highly scalable and durable.

> Amazon EBS: Provides high-performance block storage for EC2 instances, suitable for databases and applications.

![alt text](https://allcode.com/wp-content/uploads/2021/02/Group-169-3.png)

## AWS Cloud Foundations Part 2 fact-finding exercise

**1.What is the AWS shared responsibility model?**

> Shared Responsibility Model: AWS and customers share security responsibilities; AWS secures the infrastructure, while customers secure their applications and data.

**2.What is an AWS Identity and Access Management (IAM) role?**

> IAM Role: IAM roles are AWS identities with permission policies for granting access to AWS resources. They are not associated with specific users and are often used by services and applications.

**3.What is an IAM policy?**

> IAM Policy: An IAM policy is a document that defines permissions for AWS resources. It specifies what actions are allowed or denied on which resources.

**4.What is Amazon Machine Image?**

> Amazon Machine Image (AMI): An AMI is a pre-configured template used to create virtual machine instances in Amazon EC2.

**5.What are the different Amazon EC2 instance types?**

> Amazon EC2 Instance Types: EC2 offers various instance types, such as T2 (burstable), M5 (general-purpose), and P3 (GPU optimized), each suited for different workloads and performance needs.

**6.What is a virtual private cloud (VPC)?**

> Virtual Private Cloud (VPC): VPC is a logically isolated section of the AWS cloud where you can launch AWS resources. It provides control over the virtual network environment.

**7.What is the difference between a public and private subnet?**

> Public vs. Private Subnet: Public subnets have a route to the internet and can access it, while private subnets do not have a direct route to the internet.

## AWS Well-Architected Framework fact-finding exercise

![alt text](https://www.aws.ps/wp-content/uploads/2019/12/aws-five-pillars.png)

**1.What are the pillars of the AWS Well Architected Framework?**

AWS Well Architected Framework is Built around five pillars:

- operational excellence
- security
- reliability
- performance efficiency
- cost optimization

> AWS Well-Architected provides a consistent approach for customers and partners to evaluate architectures and implement scalable designs.

**2.What are the design principles for operational excellence in the cloud?**

> Make frequent, small, reversible changes. Refine operations procedures frequently. Anticipate failure. Learn from all operational failures.

**3.What are the design principles that strengthen system security?**

There are seven design principles for security in the cloud:

- Implement a strong identity foundation.
- Enable traceability.
- Apply security at all layers.
- Automate security best practices.
- Protect data in transit and at rest.
- Keep people away from data.
- Prepare for security events.

**4.What are the design principles that increase reliability?**

- There are five design principles for reliability in the cloud:
- Automatically recover from failure
- Test recovery procedures
- Scale horizontally to increase aggregate workload availability
- Stop guessing capacity
- Manage change in automation

**5.What are the factors that influence performance efficiency in the cloud?**

> optimizing cloud performance requires a holistic approach that addresses various factors such as network latency, scalability, resource allocation, data storage, application design, and continuous monitoring.

> By implementing optimization techniques in these areas, businesses can ensure efficient utilization of cloud resources, enhance user experience, and drive better overall performance.

> As cloud computing continues to evolve, staying updated with the latest optimization techniques and best practices is crucial to unlock the full potential of cloud technology.

**6.What are the different focus areas for cost-effective optimization in the cloud?**

- Practice Cloud Financial Management
- Expenditure and usage awareness
- Cost effective resources
- Manage demand and supply resources
- Optimize over time

**7.What are the design principles that support sustainability in the cloud?**

- Understand your impact
- Establish sustainability goals
- Maximize utilization
- Anticipate and adopt new, more efficient hardware and software offerings
- Use managed services
- Reduce the downstream impact of your cloud workloads

### **by Simon, Ata, Arthur**
