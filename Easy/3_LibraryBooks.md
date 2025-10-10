**Problem Statement:**

Imagine you're working for a library and you're tasked with generating a report on the borrowing habits of patrons. 
You have two tables in your database: Books and Borrowers.
Write an SQL to display the name of each borrower along 
with a comma-separated list of the books they have borrowed in alphabetical order, display the output in ascending order of Borrower Name.

**Expected Output:**

| BorrowerName | BorrowedBooks                           |
|--------------|-----------------------------------------|
| Alice        | Pride and Prejudice,The Great Gatsby    |
| Bob          | Romeo and Juliet,To Kill a Mockingbird  |
| Charlie      | 1984,The Notebook                       |
| David        | The Catcher in the Rye,The Hunger Games |
| Eve          | Pride and Prejudice                     |
| Frank        | Foundation,Romeo and Juliet             |
| Grace        | The Notebook                            |
| Harry        | To Kill a Mockingbird                   |
| Ivy          | 1984                                    |

```
select 
bo.BorrowerName, 
GROUP_CONCAT(b.BookName ORDER BY b.BookName)
FROM Books b
JOIN Borrowers bo
ON b.BookID = bo.BookID
GROUP BY bo.BorrowerName
```
