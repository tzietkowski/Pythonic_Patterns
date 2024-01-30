from dataclasses import dataclass, field
from abc import abstractmethod, ABC

@dataclass
class Item:
    name: str
    price: int


class ShippingStrategy(ABC):
    
    @abstractmethod
    def calculate(self, items_cost: int) -> int:
        pass


class ShippingStandard(ShippingStrategy):
    
    def calculate(self, items_cost: int) -> int:
        if items_cost <= 50:
            return 5
        elif items_cost > 50:
            return 0 


class ShippingExpress(ShippingStrategy):
    
    def calculate(self, items_cost: int) -> int:
        if items_cost <= 50:
            return 10
        elif items_cost > 50:
            return 5


class ShippingOvernight(ShippingStrategy):
    
    def calculate(self, _: int) -> int:
        return 50


@dataclass
class ShoppingCart:
    items: list[Item] = field(default_factory=list)
    
    def add_item(self, item: Item) -> None:
        self.items.append(item)
    
    def calculate_total_cost(self, shipping_strategy: ShippingStrategy) -> int:
        items_cost  = sum(item.price for item in self.items)
        shipping_cost = shipping_strategy.calculate(items_cost)
        return items_cost + shipping_cost    

def main() -> None:
    shopping_cart = ShoppingCart()
    shopping_cart.add_item(Item(name="laptop", price=1500))
    shopping_cart.add_item(Item(name="mouse", price=30))
    shopping_cart.add_item(Item(name="keyboard", price=40))
    print(shopping_cart.calculate_total_cost(ShippingStandard()))
    print(shopping_cart.calculate_total_cost(ShippingExpress()))
    print(shopping_cart.calculate_total_cost(ShippingOvernight()))


if __name__ == "__main__":
    main()
    
