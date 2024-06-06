#Shipping cost calculator

##INput Package weight and shipping rate
weight=float(input("Enter the package weight in kilograms: "))
rate=float(input(input("Enter the shipping rate per kilogram")))

##Calculate the shipping cost
shipping_cost=weight*rate

##Display the result
print(f"Shipping Cost: {shipping_cost} USD")
