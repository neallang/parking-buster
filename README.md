[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/qgEWmaMc)
# Parking Buster

Welcome to Parking Buster, the reporting app for bad parking! This project was created in CS 3240 during the Spring 2024 semester. Throughout the process, I was the DevOps manager, meaning I focused more on back end development and integrating each technology to work with our project. This website has some cool features, such as Google Authentication, Amazon S3 file storage (no longer supported), different users / interfaces / functionalities, JavaScript, internal notifications, and more! Read more to understand how the website works and feel free to give it a try! It is currently deployed via PythonAnywhere. [Live Site](https://neallang.pythonanywhere.com/).

## Users

### Common User
A common user must log in with Google in order to enter the website by pressing the 'Login with Google' button. Once logged in, a common user is able to make a new report (or log out). When making a report, a common user must enter a 'Report Subject' and 'Description' about their incident. They also can enter the 'Color', 'License Plate', 'Location', 'Make/Model', or upload a file (no longer supported). Once they submit their report, they will now be able to view their submitted reports on the home page. These reports are organized chronologically within three categories:  'New', 'In Progress', and 'Resolved'. A user can view any of their past reports and see if a site admin has changed the status of their report and/or added admin notes regarding the case. A user has the ability to delete any of their reports and can submit as many reports as they desire.

### Anonymous User
An anonymous user does not have to log in with Google. They can click the 'Report Anonymously' button to make a report. The same conditions and features apply for submitting a report as a common user. Once they submit their report, they will not be able to view its status or any notes a site admin has added. They can submit as many reports as they desire as well.

### Site Admin
A site admin must log in with Google in order to enter the website by pressing the 'Login with Google' button. Once logged in, a site admin is able to view all submitted reports on the home page (or log out). These reports are organized chronologically within three categories:  'New', 'In Progress', and 'Resolved'. A site admin can view any report and update the status of it, as well as add any notes regarding the case. Once updated, the user who submitted the report (if applicable) will be able to see these changes. A site admin cannot delete any reports.

### Django Admin
A Django admin is able to promote a common user into a site admin. They are able to delete reports, common user accounts, and site admin accounts. A Django admin is able to enter the website, and must log in with Google in order to enter the website by pressing the 'Login with Google' button. Once logged in, a Django admin has the same abilities as a common user. They cannot promote themselves to a site admin.
