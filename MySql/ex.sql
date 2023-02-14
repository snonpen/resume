DELIMITER $$

CREATE PROCEDURE get_employee_salary_statistics (IN department_id INT)
BEGIN
  DECLARE avg_salary DECIMAL(10, 2);
  DECLARE min_salary DECIMAL(10, 2);
  DECLARE max_salary DECIMAL(10, 2);

  SELECT AVG(salary) INTO avg_salary
  FROM employees
  WHERE department_id = department_id;

  SELECT MIN(salary) INTO min_salary
  FROM employees
  WHERE department_id = department_id;

  SELECT MAX(salary) INTO max_salary
  FROM employees
  WHERE department_id = department_id;

  SELECT AVG(salary) AS average_salary, MIN(salary) AS minimum_salary,
         MAX(salary) AS maximum_salary
  FROM employees
  WHERE department_id = department_id;
END $$

DELIMITER ;



