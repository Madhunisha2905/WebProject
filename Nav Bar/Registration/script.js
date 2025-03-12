// Sample Products
const products = [
    { id: 1, name: "Laptop", price: 799, img: "laptop.jpg" },
    { id: 2, name: "Smartphone", price: 499, img: "phone.jpg" },
    { id: 3, name: "Camera", price: 299, img: "camera.jpg" }
];

let cart = JSON.parse(localStorage.getItem("cart")) || [];

// Display Products
const productList = document.getElementById("product-list");
function loadProducts() {
    productList.innerHTML = "";
    products.forEach(product => {
        const item = document.createElement("div");
        item.classList.add("product");
        item.innerHTML = `
            <h3>${product.name}</h3>
            <p>Price: $${product.price}</p>
            <button onclick="addToCart(${product.id})">Add to Cart</button>
        `;
        productList.appendChild(item);
    });
}
loadProducts();

// Add to Cart
function addToCart(id) {
    const product = products.find(p => p.id === id);
    cart.push(product);
    localStorage.setItem("cart", JSON.stringify(cart));
    updateCartCount();
}

// Update Cart Count
function updateCartCount() {
    document.getElementById("cart-count").innerText = cart.length;
}
updateCartCount();

// View Cart
function viewCart() {
    alert("Cart Items:\n" + cart.map(p => p.name).join(", "));
}

// Hero Slider
let currentIndex = 0;
const slides = document.querySelectorAll(".slide");

function showSlide(index) {
    slides.forEach((slide, i) => {
        slide.style.transform = `translateX(${-100 * index}%)`;
    });
}

setInterval(() => {
    currentIndex = (currentIndex + 1) % slides.length;
    showSlide(currentIndex);
}, 3000);
