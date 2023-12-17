
# QA Automation Answers

# <a name="setup"></a>Setup Instructions


### Prerequisites

1. Install Python3.10
2. Install pyenv(https://github.com/pyenv/pyenv#installation)
3. Install Postman(https://www.postman.com/)
4. Install jmeter(https://jmeter.apache.org/)

### Locally

The following instructions and commands need to be executed in your computer.

1. In your terminal install python 3.10 with pyenv
   - Run: `pyenv install <python version>`
2. In your terminal where you want to create a new virtual environment.
   - Run: `pyenv virtualenv <name of venv>`
3. In your terminal activate your virtual environment
   - Run: `pyenv activate <name of venv>`
4. `cd` to where you want to clone this repository
   - Run: `git clone <repo>`

## <a name="usage"></a>How to run the tests.

## Part 1

###Selenium

1. Install Selenium -> `pip install selenium`

####Scenario 1

1. cd part_1/selenium
2. python `Scenario1.py`
3. Check test result in the terminal.

####Scenario 2

1. cd part_1/selenium
2. python `Scenario2.py``
3. Check test result in the terminal.

###Postman

1. Open postman app
2. import the file `part_1/postman/Scenario_3_4.postman_collection.json``
3. Run the request for scenario 3 (`Login`) and scenario 4 (`Upload File`)

###Jmeter

1. Open a terminal and run the command `jmeter`` to start the jmeter app
2. Open de test plan file `part_1/jmeter/HTTP Request.jmx`
3. click Play button  for scenario 3 (`Login`) and scenario 4 (`Upload File`)


## Part 2

1) Explain the difference, in databases, between ‘Having’ and ‘where’ when it comes to a query. Develop one example for each one of this two cases and point out the difference.

    Differences:
    WHERE used to filter individual rows before grouping results.

        SELECT *
        FROM Student
        WHERE Code = A001 ;

    HAVING used to filter groups of results based on aggregation conditions.

        SELECT ID_Customer, SUM(Amount) AS TotalAmount
        FROM Orders
        GROUP BY ID_Customer
        HAVING SUM(Amount) > 100;


2) Write a query for create a data table ‘Student’ with the following attributes in it: ‘Name, ‘Code, ‘Class’, ‘Age’, ‘Favorite Subject, ‘GPA’ (5.0 scale).

    CREATE TABLE Student (
        Name VARCHAR(50),
        Code VARCHAR(10),
        Class VARCHAR(50),
        Age INT,
        Favorite_Subject VARCHAR(50),
        GPA DECIMAL(3, 2)
    );

3) Insert at least 40 records in the last table with close to real data.

    `INSERT INTO Student (Name, Code, Class, Age, Favorite_Subject, GPA) VALUES
        ('María Pérez', 'A001', 'Historia del Arte', 20, 'Renacimiento', 3.9),
        ('Juan González', 'A002', 'Matemáticas', 21, 'Geometría Analítica', 4.1),
        ('Ana Martínez', 'A003', 'Biología Celular', 22, 'Genética', 4.3),
        ('Carlos Rodríguez', 'A004', 'Literatura Universal', 20, 'Teatro Griego', 3.8),
        ('Sofía García', 'A005', 'Física Moderna', 23, 'Mecánica Cuántica', 4.5),
        ('Daniel Sánchez', 'A006', 'Economía', 21, 'Microeconomía', 3.7),
        ('Laura López', 'A007', 'Química Inorgánica', 22, 'Química Analítica', 4.2),
        ('Javier Martín', 'A008', 'Psicología', 20, 'Psicología Cognitiva', 3.9),
        ('Paula Ramírez', 'A009', 'Derecho Internacional', 24, 'Derecho Penal', 4.0),
        ('Miguel Fernández', 'A010', 'Ingeniería de Software', 23, 'Desarrollo Web', 4.4),
        ('Elena Gómez', 'A011', 'Biología Marina', 21, 'Ecología Acuática', 4.1),
        ('Alejandro Pérez', 'A012', 'Antropología', 22, 'Antropología Forense', 3.8),
        ('Carmen Torres', 'A013', 'Arquitectura', 20, 'Diseño Urbano', 4.3),
        ('Pedro Ruiz', 'A014', 'Sociología', 24, 'Movimientos Sociales', 3.6),
        ('Isabella González', 'A015', 'Arte Contemporáneo', 22, 'Instalaciones Artísticas', 4.6),
        ('Diego Martínez', 'A016', 'Estadística', 21, 'Análisis de Datos', 3.9),
        ('Valentina Sánchez', 'A017', 'Neurociencia', 23, 'Neurobiología Molecular', 4.1),
        ('Emilio Gómez', 'A018', 'Filosofía', 20, 'Ética', 4.0),
        ('Luisa Ramírez', 'A019', 'Derecho Civil', 24, 'Contratos', 4.4),
        ('Andrés Fernández', 'A020', 'Ingeniería Eléctrica', 21, 'Electrónica de Potencia', 4.2),
        ('Camila López', 'A021', 'Medicina', 22, 'Anatomía Humana', 4.5),
        ('Gustavo Martín', 'A022', 'Historia', 20, 'Edad Media', 3.8),
        ('Lucía Pérez', 'A023', 'Geología', 23, 'Geología Estructural', 4.3),
        ('Felipe Rodríguez', 'A024', 'Literatura Comparada', 21, 'Novela del Siglo XX', 4.1),
        ('Victoria García', 'A025', 'Física Nuclear', 22, 'Física de Partículas', 3.9),
        ('Renata Sánchez', 'A026', 'Economía Internacional', 20, 'Comercio Internacional', 4.2),
        ('Marcos Ramírez', 'A027', 'Química Orgánica', 24, 'Síntesis Orgánica', 4.4),
        ('Carolina Fernández', 'A028', 'Psicología Social', 21, 'Psicología Organizacional', 3.7),
        ('Roberto Gómez', 'A029', 'Derecho Penal', 22, 'Criminología', 4.3),
        ('Lucas Pérez', 'A030', 'Marketing', 20, 'Estrategias de Mercado', 4.0),
        ('Julia Martínez', 'A031', 'Biología Molecular', 23, 'Genómica', 4.6),
        ('Ignacio González', 'A032', 'Antropología Cultural', 21, 'Evolución Humana', 3.8),
        ('Alicia Ramírez', 'A033', 'Arquitectura Sostenible', 24, 'Diseño Ecológico', 4.2),
        ('Hugo Fernández', 'A034', 'Sociología Urbana', 22, 'Planificación Urbana', 3.9),
        ('Marina López', 'A035', 'Arte Moderno', 21, 'Expresionismo Abstracto', 4.5),
        ('Bruno Martín', 'A036', 'Estadística Avanzada', 23, 'Análisis Multivariado', 4.0),
        ('Valeria Pérez', 'A037', 'Neurociencia Cognitiva', 20, 'Memoria y Cognición', 4.4),
        ('Martín González', 'A038', 'Filosofía Política', 21, 'Teoría de la Justicia', 4.3),
        ('Ana García', 'A039', 'Derecho Internacional', 23, 'Derechos Humanos', 3.7),
        ('Diego Ramírez', 'A040', 'Ingeniería Biomédica', 22, 'Bioinstrumentación', 4.1);

4) Write a query to get the average of the GPA from all the students which name starts with ‘A’.

    SELECT AVG(GPA) AS Promedio_GPA
    FROM Student
    WHERE Name LIKE 'A%';

5) Write a query to get the list of students that are in the same class, have a GPA higher than 3.5/5.0 and order them by Age and Name. 

    SELECT *
    FROM Student
    WHERE Class = 'Name_of_the_class'
    AND GPA > 3.5
    ORDER BY Age, Name;

6) Write a query to get the list of all the students with ‘Name, ‘Code, ‘Class’, ‘Age’, ‘Favorite Subject, ‘GPA’.

    SELECT Name, Code, Class, Age, Favorite_Subject, GPA
    FROM Student;

7)	Take the following 25 question quiz about SQL, please include a screenshot about the results and time it took to take the test.
http://www.w3schools.com/quiztest/quiztest.asp?qtest=SQL

![diagram](./part_2/SQL%20test%20result.png)


## Part 3

1) What is the difference between a unit test, an acceptance test, an integration test and an end-to-end test?

    Each type of testing has its specific purpose in the software development life cycle and focuses on different aspects and levels of the system.
    In order to answer the question, let's first talk about the qualities of each one and finally their differences.

        Unit tests:
            They focus on validating the individual behavior of components or units of code.
            They are small tests and run in isolation, usually written by developers.
            Its goal is to ensure that each part of the code (a function, method, or class) works correctly as designed.
            They are carried out using testing frameworks such as JUnit, NUnit, Jest, among others, and are executed frequently during development.

        Integration tests:
            They evaluate how individual components combine and function together as a larger system.
            They verify the interaction between different parts of the system and how they integrate to form a functional whole.
            They can be manual or automated and are performed after unit testing to ensure that the units work together correctly.
            They identify problems that may arise due to the interaction between modules and how they communicate with each other.
       
        Acceptance tests:
            They validate whether the system meets the requirements and expectations of the client or end user.
            They are generally performed to evaluate the behavior of the system from the perspective of the end user.
            They can be automated or manual, and are often based on system usage scenarios.
            They are designed to ensure that the delivered software meets the customer's needs and expectations.
            
        End-to-end testing:
            They evaluate the entire flow of a system from start to finish.
            They verify the operation of the entire system, including the interaction of all components and their behavior in a production-like environment.
            They often simulate the actual user flow, from data input to output and interactions between various systems or modules.
            They can be complex and require well-designed test scenarios to cover all functionalities.
        
    In summary
    Unit tests focus on individual parts of the code.
    Integration testing focuses on how these parts fit together
    Acceptance testing focuses on validating user requirements
    while end-to-end testing evaluates the entire system in a production-like environment
    All these tests are important to ensure the quality and correct functioning of the software.


2) Could you explain Cohn's automation pyramid?

    The central idea of ​​the pyramid is that the most basic and fastest tests (unit tests) form the solid foundation of automated tests
    while integration tests, UI tests and system tests are less numerous but complement and validate the functionality of the system from different perspectives.
    This model provides guidance on the appropriate distribution of efforts and resources in automated testing.
    highlighting the importance of unit testing and encouraging a balance between different levels of testing to improve software quality.

3) Could you explain the difference between a black box testing and a white box testing?

    The main difference between black box testing and white box testing lies in the level of knowledge that the tester has about the system or software to be tested.
    In black box testing, functionality is tested without considering the internal logic.
    while in white box testing the structure and internal logic of the code are evaluated.
    Both techniques are complementary and are used together to ensure exhaustive coverage in software validation.

4) What is the purpose of an exploratory test and when is it useful to run them?

    An exploratory test is a testing technique in which the tester, instead of following a detailed and predefined test plan, dynamically interacts with the software, investigating, discovering and evaluating its operation in a spontaneous and creative way.
    The main purpose of exploratory testing is to discover undocumented or unexpected defects and problems in the software, as well as to better understand its operation in a limited time.

    Exploratory testing is useful in several situations.
    such as at the beginning of the development cycle when there is little documentation available
    in time-limited situations for formal testing.
    in critical areas where additional testing is needed, or simply to explore and better understand the software.
    Additionally, they can be a valuable tool in agile teams or iterative development methods, where adaptability and flexibility in the testing process are valued.

5) Mention at least 5 test design techniques and explain them briefly

    A)Equivalence Tests:

        Explanation: This technique involves dividing the data set into equivalence classes and then selecting representative test cases from each class.
        
        Usage: A minimum set of test cases are chosen that cover different scenarios within each equivalence class. For example, if a function expects numbers between 1 and 100, test cases will be selected for values ​​inside, on the edge, and outside that range.
    
    B)Boundary Testing:

        Explanation: It focuses on testing the limits or edges between different equivalence classes.

        Usage: Test cases are selected that are on the limits, including limit values ​​and just outside these limits. For example, if you have an input field that accepts values ​​between 1 and 10, bounds testing focuses on testing with 1, 10, and values ​​like 0 and 11.

    C)Decision Table (Decision Table Testing):

        Explanation: Used to test specific combinations of input conditions and determine corresponding actions.
        
        Usage: A table is created that lists all possible combinations of input conditions and their associated actions. Each of these combinations are then tested.

    D)State Testing (State Transition Testing):

        Explanation: This technique is used to test the behavior of a system in different states and the transitions between these states.
        
        Use: The different states of the system are modeled, along with the allowed transitions between them. Testing focuses on testing these transitions and the behavior of the system in each state.

    E)Black Box Based Testing (Black Box Testing):

        Explanation: It focuses on testing the functionality of the software without knowing its internal structure or implementation logic.
        
        Usage: Test cases are designed based on specifications, requirements, and the expected functionality of the software. The inputs and outputs of the system are tested without considering the internal code.

6) What is the purpose of the following types of tests?
	•	Functional test: 
	•	Performance test: 
	•	Security test:
	•	Usability test: 
	•	API test: 
	•	Unit Test:

    • Functional test:

            Purpose: Verify that the software meets the specified functional requirements.
            
            Approach: Evaluate the functions, features and behaviors of the software from the perspective of the end user.

    • Performance test:

            Purpose: To evaluate how the software performs in terms of speed, capacity, scalability and stability under different loads and situations.

            Approach: Measure and analyze software performance in terms of response time, resource usage, processing time, etc.
    
    • Security test:

            Purpose: Identify vulnerabilities, risks and security issues in software to protect it against potential threats.
            
            Approach: Evaluate the system's resistance to attacks, security failures, data theft, among others.

    • Usability test:

            Purpose: Evaluate ease of use, efficiency, and user satisfaction when interacting with the software.
            
            Focus: Analyze the user interface, navigation, accessibility and overall user experience.

    • API Test:

            Purpose: Verify the functional behavior, reliability and integration between different software components through their interfaces.
            
            Focus: Test input/output methods, error handling, authentication, security, and API interoperability.

    • Unit test:

            Purpose: Verify that individual units of code (functions, methods, classes) work correctly in isolation.
            
            Approach: Evaluate the functionality of the smallest parts of the software through specific tests performed by the developers.





