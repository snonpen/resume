DELIMITER $$

CREATE PROCEDURE transfer_funds(IN sender INT, IN receiver INT, IN amount DECIMAL(10, 2))
BEGIN
  DECLARE sender_balance DECIMAL(10, 2);
  DECIMAL receiver_balance DECIMAL(10, 2);

  START TRANSACTION;
  
  SELECT balance INTO sender_balance
  FROM accounts
  WHERE account_number = sender
  FOR UPDATE;

  SELECT balance INTO receiver_balance
  FROM accounts
  WHERE account_number = receiver
  FOR UPDATE;

  IF sender_balance < amount THEN
    ROLLBACK;
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Insufficient funds';
  END IF;

  UPDATE accounts
  SET balance = balance - amount
  WHERE account_number = sender;

  UPDATE accounts
  SET balance = balance + amount
  WHERE account_number = receiver;

  COMMIT;
END $$

DELIMITER ;