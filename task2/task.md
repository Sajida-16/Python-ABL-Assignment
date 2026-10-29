#Problem Statement
Develop a Python program to calculate a household electricity bill based on the number of units consumed using progressive billing slabs. The program should calculate energy charges, add a fixed charge and a surcharge, and display the final bill. It should also reject negative electricity consumption.
#Algorithm
1. Start the program.
2. Input the number of electricity units consumed.
3. If the units are negative, display Invalid Input and stop.
4. Calculate the energy charge using these slabs:
   - First 100 units: ₹2 per unit.
   - Next 100 units: ₹3 per unit.
   - Above 200 units: ₹5 per unit.
5. Calculate the surcharge as 5% of the energy charge.
6. Add a fixed charge of ₹50.
7. Calculate the total bill by adding energy charges, surcharge, and fixed charge.
8. Display the energy charge, surcharge, fixed charge, and total bill.
9. Stop.
    ```mermaid
    flowchart TD
    A([Start]) --> B[/Input units consumed/]
    B --> C{Units less than 0?}
    C -- Yes --> D[Display Invalid Input]
    D --> I([Stop])
    C -- No --> E{Units <= 100?}
    E -- Yes --> F[Energy charge = Units x 2]
    E -- No --> G{Units <= 200?}
    G -- Yes --> H[Energy charge = 200 + (Units - 100) x 3]
    G -- No --> J[Energy charge = 500 + (Units - 200) x 5]
    F --> K[Calculate 5 percent surcharge]
    H --> K
    J --> K
    K --> L[Add fixed charge of 50]
    L --> M[/Display total bill/]
    M --> I
```
# Sample Input
Enter electricity units consumed: 150


# Sample Output
Energy Charge: Rs. 350.0
Surcharge: Rs. 17.5
Fixed Charge: Rs. 50
Total Bill: Rs. 417.5


Calculation:
- First 100 units: 100 × ₹2 = ₹200
- Next 50 units: 50 × ₹3 = ₹150
- Energy charge: ₹350
- Surcharge: 5% of ₹350 = ₹17.50
- Fixed charge: ₹50
Final electricity bill = ₹417.50
