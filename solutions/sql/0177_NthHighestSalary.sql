/* https://leetcode.com/problems/nth-highest-salary/description/
177. Nth Highest Salary
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
 

Write a solution to find the nth highest distinct salary from the Employee table. If there are less than n distinct salaries, return null.

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
n = 2
Output: 
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| 200                    |
+------------------------+
Example 2:

Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
+----+--------+
n = 2
Output: 
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| null                   |
+------------------------+
*/

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
    WITH distinct_salaries AS (
        SELECT DISTINCT salary FROM Employee
    ),
    ranked_salaries AS (
        SELECT salary, RANK() OVER (ORDER BY salary DESC) AS salary_rank
        FROM distinct_salaries
    )
    SELECT 
        CASE
            WHEN MAX(salary_rank) >= N THEN salary
            ELSE NULL
        END AS SecondHighestSalary
    FROM ranked_salaries
    WHERE salary_rank = N
  );
END
