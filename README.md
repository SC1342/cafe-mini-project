# cafe-mini-project
The client is a pop up cafe selling various products requiring a software application in order to manage their products, couriers and incoming orders.

This python application will allow the client to display, add, update and delete their products, couriers and incoming orders. The data is saved in CSV files.
Testing (in particular unit testing) and data validation was employed to guarantee the client requirements

With more time, there is future room to expand this project to be linked to a database as our client expands their business as well as adding additional functionality to add stock levels to their products and assert that their is enough product stock for incoming orders, as well as checking the availability of couriers etc. 
One would guarantee these new client requirements via more testing, in particular integration testing (with the database) as well as data validation checks such as the aforementioned with regards to stock levels.


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#client-specifications">Client Specifications</a>
    </li>
    <li>
      <a href="#design-specifications">Design Specifications</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
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

Various data validation checks as well as some unit testing was used ensuring the client's requirements were met and guaranteed. If the client is mistaken when entering key data such as the name of a courier or the phone number of their customer which is likely to occur due to human limitations, then the application will inform the client and prompt them. This was done in the use of try-except blocks as well as with the use of other means of boolean logic. Some unit tests were carried out on functions in the products, couriers, and orders menu.  



### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```

### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/your_username_/Project-Name.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Add Changelog
- [x] Add back to top links
- [ ] Add Additional Templates w/ Examples
- [ ] Add "components" document to easily copy & paste sections of the readme
- [ ] Multi-language Support
    - [ ] Chinese
    - [ ] Spanish

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Patrick

Numan Mahmood
