def calculate_ticket_price():
    return 50.0 

from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, event_data):
        pass

class Subject(ABC):
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, event_data):
        for observer in self._observers:
            observer.update(event_data)

class BookingSystem(Subject, ABC):
    @abstractmethod
    def bookTicket(self, name, date, showTime, tickets):
        pass

    @abstractmethod
    def deleteTicket(self, name, date):
        pass

    @abstractmethod
    def buyTicket(self, name, date, showTime, tickets):
        pass

class ConcertTicket(BookingSystem):
    def bookTicket(self, name, date, showTime, tickets):
        print(f"Reserved {tickets} tickets for {name} on {date} at {showTime}, let's quickly buy a ticket to the concert")

    def deleteTicket(self, name, date):
        print("Deletion not supported by the concert")

    def buyTicket(self, name, date, showTime, tickets):
        print(f"Congratulations, {name}! Your {tickets} tickets for the show on {date} at {showTime} are booked.")

class FootballGameTicket(BookingSystem):
    def bookTicket(self, name, date, showTime, tickets):
        print(f"Reserved {tickets} tickets for {name} for the football game on {date} at {showTime}.")

    def deleteTicket(self, name, date):
        print(f"Deleted the ticket for {name} for the football game on {date}.")

    def buyTicket(self, name, date, showTime, tickets):
        print(f"Congratulations, {name}! Your {tickets} tickets for the football game on {date} at {showTime} are booked.")

class BasketballGameTicket(BookingSystem):
    def bookTicket(self, name, date, showTime, tickets):
        print(f"Reserved {tickets} tickets for {name} for the basketball game on {date} at {showTime}.")

    def deleteTicket(self, name, date):
        print(f"Deleted the ticket for {name} for the basketball game on {date}.")

    def buyTicket(self, name, date, showTime, tickets):
        print(f"Congratulations, {name}! Your {tickets} tickets for the basketball game on {date} at {showTime} are booked.")

class MuseumTicket(BookingSystem):
    def bookTicket(self, name, date, showTime, tickets):
        print(f"You reserved {tickets} tickets for {name} for the museum show on {date} at {showTime}")

    def deleteTicket(self, name, date):
        print(f"You deleted the ticket for {name} for the museum show on {date}")

    def buyTicket(self, name, date, showTime, tickets):
        print(f"Congratulations, {name}! Your {tickets} tickets for the museum show on {date} at {showTime} are booked")

class MovieTicket(BookingSystem):
    def bookTicket(self, name, date, showTime, tickets):
        print(f"You reserved {tickets} tickets for {name} for the movie on {date} at {showTime}")

    def deleteTicket(self, name, date):
        print(f"You deleted the ticket for {name} for the movie on {date}")

    def buyTicket(self, name, date, showTime, tickets):
        print(f"Congratulations, {name}! Your {tickets} tickets for the movie on {date} at {showTime} are booked")


class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, price):
        pass

class NoDiscount(DiscountStrategy):
    def apply_discount(self, price):
        return price

class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage):
        self.percentage = percentage / 100

    def apply_discount(self, price):
        return price - (price * self.percentage)

class FixedDiscount(DiscountStrategy):
    def __init__(self, amount):
        self.amount = amount

    def apply_discount(self, price):
        return price - self.amount

class DiscountDecorator(BookingSystem):
    def __init__(self, booking_system, discount_strategy):
        self._booking_system = booking_system
        self._discount_strategy = discount_strategy

    def bookTicket(self, name, date, showTime, tickets):
        self._booking_system.bookTicket(name, date, showTime, tickets)
        discounted_price = self._discount_strategy.apply_discount(calculate_ticket_price())
        print(f"Цена со скидкой: ${discounted_price:.2f}")

    def deleteTicket(self, name, date):
        self._booking_system.deleteTicket(name, date)

    def buyTicket(self, name, date, showTime, tickets):
        self._booking_system.buyTicket(name, date, showTime, tickets)
        discounted_price = self._discount_strategy.apply_discount(calculate_ticket_price())
        print(f"Поздравляем, {name}! Ваши билеты ({tickets} штук) на шоу {date} в {showTime} забронированы.")
        print(f"Итоговая цена: ${discounted_price:.2f}")

class ConcertTicketWithDiscount(DiscountDecorator):
    def __init__(self, discount_strategy):
        super().__init__(ConcertTicket(), discount_strategy)

class ConcertShowAdapter(BookingSystem):
    def __init__(self, ticket_system, discount_strategy):
        super().__init__()
        self.ticket_system = ticket_system
        self.discount_strategy = discount_strategy
        self.purchasedTickets = []

    def bookTicket(self, name, date, showTime, tickets):
        self.ticket_system.bookTicket(name, date, showTime, tickets)
        self.purchasedTickets.append((name, date, showTime, tickets))
        event_data = {"action": "booking", "data": (name, date, showTime, tickets)}
        self.notify_observers(event_data)
        print(f"Booking completed for {name} on {date} at {showTime} for {tickets} tickets.")

    def deleteTicket(self, name, date):
        self.ticket_system.deleteTicket(name, date)
        event_data = {"action": "deletion", "data": (name, date)}
        self.notify_observers(event_data)

    def buyTicket(self, name, date, showTime, tickets):
        ticket_price = calculate_ticket_price()  # Replace this with your actual logic
        discounted_price = self.discount_strategy.apply_discount(ticket_price)

        self.ticket_system.buyTicket(name, date, showTime, tickets)
        self.purchasedTickets.append((name, date, showTime, tickets, discounted_price))
        event_data = {"action": "purchase", "data": (name, date, showTime, tickets, discounted_price)}
        self.notify_observers(event_data)
        print(f"Congratulations, {name}! Your {tickets} tickets for the show on {date} at {showTime} are booked.")
        print(f"Total Price: ${discounted_price:.2f}")

    def viewPurchasedTickets(self):
        if self.purchasedTickets:
            print("Purchased Tickets:")
            for ticket in self.purchasedTickets:
                print(f"Name: {ticket[0]}, Date: {ticket[1]}, Show Time: {ticket[2]}, Tickets: {ticket[3]}, Total Price: ${ticket[4]:.2f}")
        else:
            print("No purchased tickets.")

class TicketFactory:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TicketFactory, cls).__new__(cls)
        return cls._instance

    @staticmethod
    def chooseEvent(type, discount_strategy):
        if type == "Concert":
            return ConcertShowAdapter(ConcertTicket(), discount_strategy)
        elif type == "Football":
            return ConcertShowAdapter(FootballGameTicket(), discount_strategy)
        elif type == "Museum":
            return ConcertShowAdapter(MuseumTicket(), discount_strategy)
        elif type == "Basketball":
            return ConcertShowAdapter(BasketballGameTicket(), discount_strategy)
        elif type == "Movie":
            return ConcertShowAdapter(MovieTicket(), discount_strategy)
        else:
            raise ValueError("Incorrect selection or we do not have such an event. Rerun the program.")

    @staticmethod
    def chooseDiscountStrategy(type):
        if type == "NoDiscount":
            return NoDiscount()
        elif type == "PercentageDiscount":
            percentage = float(input("Enter the discount percentage: "))
            return PercentageDiscount(percentage)
        elif type == "FixedDiscount":
            amount = float(input("Enter the fixed discount amount: "))
            return FixedDiscount(amount)
        else:
            raise ValueError("Incorrect selection for discount strategy.")

class Configuration:
    showTimes = ["2pm", "4pm", "6pm", "8pm", "10pm", "12pm"]

class TicketObserver(Observer):
    def update(self, event_data):
        action = event_data["action"]
        data = event_data["data"]
        if action == "booking":
            print(f"Observer: Booking completed for {data[0]} on {data[1]} at {data[2]} for {data[3]} tickets.")
        elif action == "deletion":
            print(f"Observer: Ticket for {data[0]} on {data[1]} has been deleted.")
        elif action == "purchase":
            print(f"Observer: Congratulations, {data[0]}! Your {data[3]} tickets for the show on {data[1]} at {data[2]} are booked.")
            print(f"Observer: Total Price: ${data[4]:.2f}")

if __name__ == '__main__':
    type = input("Enter the event you want to go to (Concert, Football, Basketball, Museum, Movie): ")
    discount_type = input("Choose a discount strategy (NoDiscount, PercentageDiscount, FixedDiscount): ")

    try:
        discount_strategy = TicketFactory.chooseDiscountStrategy(discount_type)

        # Wrap the base ticket system with the decorator
        ticketSystem = DiscountDecorator(TicketFactory.chooseEvent(type, discount_strategy), discount_strategy)

        # Alternatively, you can use a specific decorated ticket class
        # ticketSystem = ConcertTicketWithDiscount(discount_strategy)
    except ValueError as e:
        print(f"Error: {e}")
    else:
        adapter = ConcertShowAdapter(ticketSystem, discount_strategy)

        # Create and register the observer
        observer = TicketObserver()
        adapter.add_observer(observer)

        while True:
            print("\n1. Book a ticket \n2. Delete a ticket \n3. Buy a ticket \n4. View Purchased Tickets\n5. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                name = input("Enter your name: ")
                showDate = input("Enter the date (YYYY-MM-DD): ")
                print("Available show times:", Configuration.showTimes)
                showTime = input("Choose the show time: ")
                tickets = int(input("Enter the number of tickets: "))
                adapter.bookTicket(name, showDate, showTime, tickets)

            elif choice == '2':
                name = input("Enter your name: ")
                showDate = input("Enter the date to delete (YYYY-MM-DD): ")
                adapter.deleteTicket(name, showDate)

            elif choice == '3':
                name = input("Enter your name: ")
                showDate = input("Enter the date (YYYY-MM-DD): ")
                print("Available show times:", Configuration.showTimes)
                showTime = input("Choose the show time: ")
                tickets = int(input("Enter the number of tickets: "))
                adapter.buyTicket(name, showDate, showTime, tickets)

            elif choice == '4':
                adapter.viewPurchasedTickets()

            elif choice == '5':
                print("Exiting...")
                break

            else:
                print("Invalid choice. Please try again.")
