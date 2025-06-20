-- Initialize the products table with sample data
CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10,2) NOT NULL,
    category VARCHAR(100),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Insert sample products for testing
INSERT INTO products (name, description, price, category) VALUES
('MacBook Pro 16"', 'Apple MacBook Pro with M2 Pro chip, 16GB RAM, 512GB SSD', 2499.99, 'Laptops'),
('iPhone 15 Pro', 'Apple iPhone 15 Pro with A17 Pro chip, 128GB storage', 999.99, 'Smartphones'),
('Sony WH-1000XM5', 'Wireless noise-canceling headphones with 30-hour battery life', 399.99, 'Audio'),
('Nintendo Switch OLED', 'Nintendo Switch with 7-inch OLED screen and enhanced audio', 349.99, 'Gaming'),
('Samsung 65" QLED TV', '4K QLED Smart TV with Quantum HDR and Alexa Built-in', 1299.99, 'TVs'),
('iPad Air', 'Apple iPad Air with M1 chip, 10.9-inch display, 64GB storage', 599.99, 'Tablets'),
('AirPods Pro', 'Active noise cancellation, Transparency mode, Spatial audio', 249.99, 'Audio'),
('PlayStation 5', 'Sony PlayStation 5 Digital Edition with DualSense controller', 499.99, 'Gaming'),
('Dell XPS 13', '13.4-inch InfinityEdge display, Intel Core i7, 16GB RAM', 1199.99, 'Laptops'),
('Google Pixel 8', 'Google Pixel 8 with Tensor G3 chip, 128GB storage', 699.99, 'Smartphones'),
('Bose QuietComfort 45', 'Wireless noise-canceling headphones with 24-hour battery', 329.99, 'Audio'),
('LG 55" OLED TV', '4K OLED Smart TV with AI ThinQ and webOS', 1499.99, 'TVs'),
('Microsoft Surface Pro 9', '13-inch PixelSense display, Intel Core i5, 8GB RAM', 999.99, 'Tablets'),
('Xbox Series X', 'Microsoft Xbox Series X with 1TB SSD and 4K gaming', 499.99, 'Gaming'),
('HP Spectre x360', '13.5-inch 3K2K OLED display, Intel Core i7, 16GB RAM', 1399.99, 'Laptops');

-- Create index on id for faster lookups
CREATE INDEX IF NOT EXISTS idx_products_id ON products(id);

-- Create index on category for potential future queries
CREATE INDEX IF NOT EXISTS idx_products_category ON products(category); 