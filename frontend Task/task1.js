function calculateTotal(cart) {
    let total = 0;

    cart.forEach(item => {
        console.log(`Processing item: ${item.name}, Price: ${item.price}, Quantity: ${item.quantity}`);
        if (typeof item.price === 'number' && typeof item.quantity === 'number') {
            total += item.price * item.quantity;
        } else {
            console.warn(`Invalid item detected: ${JSON.stringify(item)}`);
        }
    });

    console.log(`Final total calculated: ₹${total}`);
    return total.toFixed(2);
}

const shoppingCart = [
    { name: "Laptop", price: 50000, quantity: 1 },
    { name: "Headphones", price: 2000, quantity: 2 },
    { name: "Mouse", price: 1500, quantity: 1 }
];

console.log("Total Price: ₹" + calculateTotal(shoppingCart));
