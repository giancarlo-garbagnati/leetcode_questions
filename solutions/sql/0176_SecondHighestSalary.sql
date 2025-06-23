/* https://leetcode.com/problems/second-highest-salary/description/
176. Second Highest Salary
Medium

Table: Employee

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.
 

Write a solution to find the second highest distinct salary from the Employee table. If there is no second highest salary, return null (return None in Pandas).

The result format is in the following example.

 

Example 1:

Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
Output: 
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+
Example 2:

Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
+----+--------+
Output: 
+---------------------+
| SecondHighestSalary |
+---------------------+
| null                |
+---------------------+
*/

/* -- not my solution, but one of the more optimal solns for me to review
select max(salary) as SecondHighestSalary from Employee
where salary < (select max(salary) from Employee)
*/

/* -- My first solution
WITH distinct_salaries AS (
    SELECT DISTINCT salary FROM Employee
),
ranked_salaries AS (
    SELECT salary, RANK() OVER (ORDER BY salary DESC) AS salary_rank
    FROM distinct_salaries
)
SELECT 
    CASE
        WHEN MAX(salary_rank) > 1 THEN salary
        ELSE NULL
    END AS SecondHighestSalary
FROM ranked_salaries
WHERE salary_rank = 2;
*/

SELECT MAX(salary) AS SecondHighestSalary
FROM Employee
WHERE salary < (
    SELECT MAX(salary) FROM Employee
);

