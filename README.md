# Booking ticket
This concert ticket system allows users to book, delete, and purchase tickets for concerts. It also supports various discount strategies, including no discount, percentage discount, and fixed discount. The system utilizes a combination of object-oriented programming principles and design patterns to achieve its functionality.

# Installation and Usage
To install and use the code, follow these steps:

- Prerequisites: Ensure you have Python 3.6 or higher installed on your system.

- Cloning the Repository: Clone the repository containing the code using the following command:

Bash
git clone <repository_url>
Running the Program: Navigate to the cloned repository directory and execute the following command:
Bash
Event Selection: Upon running the program, you will be prompted to enter the type of event you want to attend, such as "Concert," "Football," "Basketball," "Museum," or "Movie."

- Discount Strategy Selection: Next, you will be asked to choose a discount strategy from the available options: "NoDiscount," "PercentageDiscount," or "FixedDiscount."

Ticket Operations: The system will guide you through the process of booking, deleting, or purchasing tickets based on your selections.

1. Features
The concert ticket system offers the following features:

- Ticket Booking: Users can reserve tickets for upcoming concerts.

- Ticket Deletion: Users can cancel their reserved tickets if needed.

- Ticket Purchase: Users can finalize their ticket bookings and make payments.

- Discount Strategies: The system supports various discount strategies to reduce ticket prices.

- Observer Pattern: Changes to the ticket system, such as bookings, deletions, and purchases, are notified to registered observers.

# Implementation
The concert ticket system is implemented using object-oriented programming principles and employs several design patterns to achieve its functionality:

- Observer Pattern: This pattern allows objects to subscribe as observers of a subject and receive notifications when the subject's state changes. In this case, the ticket system acts as the subject, and observers can be any entities interested in ticket-related events.

- Decorator Pattern: This pattern enables dynamic modification of an object's behavior by wrapping it in another object. The decorator pattern is used to apply discount strategies to the ticket system, altering its ticket pricing behavior.

- Factory Pattern: This pattern provides a mechanism for creating objects of different classes based on provided criteria. The factory pattern is implemented to create ticket system objects specific to the selected event type.

- Strategy Pattern: This pattern encapsulates different algorithms for a specific task, allowing for interchangeable implementation strategies. The strategy pattern is employed to apply different discount calculation algorithms based on the chosen discount strategy.

# Singleton Pattern
The Singleton pattern ensures that there is only one instance of the TicketFactory class throughout the application. This pattern provides a global point of control over the creation of ticket-related objects, preventing unnecessary duplication of factory instances. The Singleton pattern simplifies the management of object creation and ensures a centralized mechanism for creating tickets and discount strategies.

# Adapter Pattern
The Adapter pattern plays a crucial role in achieving uniformity across different event types. The ConcertShowAdapter class acts as an adapter, allowing various concrete event booking systems to conform to a common interface defined by the BookingSystem abstraction. This abstraction ensures that regardless of the event type, clients can interact with the booking systems uniformly. The Adapter pattern thus enhances consistency and simplifies the integration of new event types.

# How to Use the Ticket Booking System
Event Selection:

- Run the program and input the type of event you wish to attend (Concert, Football, Basketball, Museum, Movie).
Discount Strategy Selection:

- Choose a discount strategy (NoDiscount, PercentageDiscount, FixedDiscount) based on your preferences.
Booking, Deletion, and Purchase:

- Follow the on-screen prompts to book, delete, or purchase tickets for the selected event.
View Purchased Tickets:

- Option 4 allows you to view detailed information about purchased tickets, including the name, date, show time, number of tickets, and total price.
Exit:

Select option 5 to exit the program.

- Contributions
Contributions to the project are welcomed and encouraged. Please feel free to create pull requests with your improvements and suggestions.


# Conclusion
The Ticket Booking System showcases the effective implementation of design patterns to create a modular, flexible, and scalable application. The Observer pattern facilitates efficient event handling, the Decorator pattern dynamically extends functionality, and the Adapter pattern ensures uniform treatment of diverse event types. The Factory pattern centralizes object creation, the Singleton pattern provides a global point of control, and the Strategy pattern allows for easy switching between different discount strategies. Together, these design patterns contribute to a robust, maintainable, and adaptable ticket booking system, providing an excellent foundation for future enhancements and expansions.


