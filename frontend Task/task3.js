function findMostFrequentProduct(orders) {
    const productCount = {};

    // Count the frequency of each product
    orders.forEach(order => {
        order.products.forEach(product => {
            productCount[product] = (productCount[product] || 0) + 1;
        });
    });

    // Find the product with the highest count
    let mostFrequentProduct = null;
    let maxCount = 0;

    for (const product in productCount) {
        if (productCount[product] > maxCount) {
            mostFrequentProduct = product;
            maxCount = productCount[product];
        }
    }

    return mostFrequentProduct;
}

// Example usage
const orders = [
    { id: 1, products: ["Laptop", "Mouse"] },
    { id: 2, products: ["Mouse", "Keyboard"] },
    { id: 3, products: ["Laptop", "Mouse", "Headphones"] },
    { id: 4, products: ["Mouse", "Monitor"] }
];

console.log("Most frequently purchased product:", findMostFrequentProduct(orders));
