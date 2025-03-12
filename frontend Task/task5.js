function isCouponValid(couponCode, expirationDate) {
    const expiry = new Date(expirationDate);
    if (isNaN(expiry.getTime())) {
        console.error("Invalid expiration date format.");
        return false;
    }

    const currentDate = new Date();

    if (currentDate > expiry) {
        alert("Coupon code is expired");
        return false;
    }

    return true;
}

// Example usage
console.log(isCouponValid("SAVE20", "2025-12-31")); // true (valid coupon)
console.log(isCouponValid("DISCOUNT10", "2023-01-01")); // false + popup (expired coupon)
console.log(isCouponValid("WELCOME15", "invalid-date")); // false (invalid date format)
