# cafe-mini-project

This python application will allow the client to display, add, update and delete their products, couriers and incoming orders.


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#client-specifications">Client Specifications</a>
    </li>
    <li>
      <a href="#design-specifications">Design Specifications</a>
    </li>
    <li>
      <a href="#plans-for-future-implmentation">Plans for future implementation</a>
    </li>
    <li>
      <a href="#acknowledgments">Acknowledgments</a>
    </li>
  </ol>
</details>



<!-- CLIENT SPECIFICATIONS -->
## Client Specifications
The client is a pop up cafe selling various products requiring a software application in order to:
* View their products list
* Add a new product to their products list
* Update details about an existing product
* Delete an existing product

* View their couriers list
* Add a new courier to their couriers list
* Update details about an existing courier
* Delete an existing courier

* View their orders list
* Add a new order to their orders list
* Update details about an existing order
* Delete an existing order
 
In addition to this, the client required me to persist/save the data and any changes made everytime they exited the application as well as loading all previous data when starting the application.

<!-- Design Specifications -->
## Design Specifications

A functional orientated approach was taken. Functions were designed to carry out each client specification in order to avoid repeating code. Due to the client changing their specifications every week the use of functions preserved readability of the code making it easier to refactor in order to meet the updated requirements.

A main-menu function was used allowing the client to navigate through to the products, couriers, or orders menu which were themselves functions allowing the client to decide what action they wanted to carry out within each of those 3 menus. These actions of viewing, adding, updating, and deleting products, orders, and couriers were themselves functions. This logical use of functions in line with the client requirements allowed for clean code and easier readability which will be beneficial for other collaborators wanting to add software updates to the application in the future.

The data for products, couriers, and orders is loaded from CSV files everytime the application starts. When the client decides to exit the application, all of the data including any changes made to the data are saved in CSV files. This ensures data persistance in the application.

Various data validation checks as well as some unit testing was used ensuring the client's requirements were met and guaranteed. If the client is mistaken when entering key data such as the name of a courier or the phone number of their customer which is likely to occur due to human limitations, then the application will prompt the user. This was done using try-except blocks as well as with the use of other means of boolean logic. Some unit tests were carried out on functions in the products, couriers, and orders menu.

<!-- PLANS FOR FUTURE IMPLEMENTATION -->
## Plans for future implementation

With more time, there is future room to expand this project to be linked to a database as our client expands their business as well as adding additional functionality to add stock levels to their products and assert that their is enough product stock for incoming orders alongside asserting the availability of couriers etc.

Moreover, more testing such as unit testing would be employed on all of the functions of the application in order to guarantee the client requirements. In particular integration testing would be employed after having updated to a database.

Finally, I would consider refactoring and taking an object-orientated approach. This may make the process of refactoring the code to implement the use of a database much more feasible.

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Patrick Cando

Numan Mahmood
