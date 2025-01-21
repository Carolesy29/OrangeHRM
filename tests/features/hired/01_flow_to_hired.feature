@login
Feature: Orange: Create candidate to hired.

  Scenario Outline: Create candidate.
    Given that the page is opened for a in <browser> device
    When submit user: <username> and password: <password> and click on the enter button
    And fill in First Name with <firstname>
    And fill in Middle Name with <middle_name>
    And fill in Last Name with <lastname>
    And select Vacancy with payroll administrator role
    And fill in Email with <email>
    And fill in Contact Number with <phone>
    And upload Resume with <path>
    And fill in Keywords with <keywords>
    And fill in Notes with <notes>
    And click on consent to keep data
    When click on Save
    When click on Shortlist button
    When click on save shortlist button
    When click on schedule interview
    When fill interview title with <title>
    When fill interview date with <date>
    When fill interview time with <time>
    When fill interviewer with <interviewer>
    When click on save interview
    When click on passed interview
    When click on save passed interview
    When click on offer job button
    When click on save offer job button
    When click on hired button
    When click on save hired button
    Then the candidate should be hired successfully

    Examples:
      | username | password | browser | firstname | lastname | middle_name | email          | phone    | path   | keywords               | notes     | browser | title        | date       | time  | interviewer |
      | Admin    | admin123 | random  | Esymar    | Vega     | Carolina    | test@email.com | 62345253 | cv.pdf | payroll, administrator | Confirmed | random  | QA Interview | 2025-06-19 | 12:00 | a           |

