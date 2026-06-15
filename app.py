import streamlit as st

# ==========================================
# PAGE CONFIGURATION & CUSTOM CSS
# ==========================================
st.set_page_config(
    page_title="MiniStore - Home",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for UI cards and a floating support button in the bottom right corner
st.markdown("""
    <style>
    /* Main container styling */
    .main {
        background-color: #f9f9fb;
    }
    /* Product Card Styling */
    .product-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 20px;
        border: 1px solid #eee;
        transition: transform 0.2s;
    }
    .product-card:hover {
        transform: translateY(-5px);
    }
    /* Typography */
    .product-title {
        font-size: 1.15rem;
        font-weight: 600;
        color: #1e293b;
        margin-bottom: 8px;
    }
    .product-price {
        font-size: 1.25rem;
        font-weight: 700;
        color: #2563eb;
        margin-bottom: 8px;
    }
    .product-desc {
        font-size: 0.9rem;
        color: #64748b;
        height: 60px;
        overflow: hidden;
        text-overflow: ellipsis;
        margin-bottom: 15px;
    }
    .category-badge {
        display: inline-block;
        background-color: #f1f5f9;
        color: #475569;
        font-size: 0.75rem;
        padding: 4px 8px;
        border-radius: 20px;
        margin-bottom: 10px;
        font-weight: 500;
    }
    
    /* FLOATING SUPPORT BUTTON STYLING */
    .floating-support-btn {
        position: fixed;
        bottom: 30px;
        right: 30px;
        background-color: #2563eb;
        color: white !important;
        padding: 15px 22px;
        border-radius: 50px;
        box-shadow: 0 6px 12px rgba(37, 99, 235, 0.3);
        text-decoration: none;
        font-weight: bold;
        z-index: 999;
        font-size: 1rem;
        display: flex;
        align-items: center;
        gap: 8px;
        transition: background-color 0.2s, transform 0.2s;
    }
    .floating-support-btn:hover {
        background-color: #1d4ed8;
        transform: scale(1.05);
    }
    </style>
""", unsafe_allow_html=True)

# Add Floating Support Button pointing to the Multipage app route
# Note: Streamlit's URL matching pattern converts "1_Support_Chatbot.py" into "Support_Chatbot"
st.markdown(
    '<a href="/Support_Chatbot" target="_self" class="floating-support-btn">💬 Live Support Chat</a>', 
    unsafe_allow_html=True
)

# ==========================================
# INITIALIZE SESSION STATE (Shopping Cart)
# ==========================================
if 'cart' not in st.session_state:
    st.session_state.cart = {}

def add_to_cart(product_id, name, price):
    if product_id in st.session_state.cart:
        st.session_state.cart[product_id]['quantity'] += 1
    else:
        st.session_state.cart[product_id] = {'name': name, 'price': price, 'quantity': 1}
    st.toast(f"Added {name} to cart! 🛒")

def clear_cart():
    st.session_state.cart = {}
    st.toast("Cart cleared!")

# ==========================================
# SAMPLE PRODUCT DATA
# ==========================================
products = [
    {"id": "p1", "name": "Minimalist Leather Watch", "price": 129.00, "description": "Sleek, scratch-resistant analog watch with a genuine Italian leather band.", "category": "Accessories", "image": "🕒"},
    {"id": "p2", "name": "Wireless Noise-Canceling Headphones", "price": 249.50, "description": "Immersive sound with 30-hour battery life and ultra-soft memory foam earcups.", "category": "Electronics", "image": "🎧"},
    {"id": "p3", "name": "Ergonomic Mechanical Keyboard", "price": 89.99, "description": "Hot-swappable tactile switches with customizable RGB backlighting for creators.", "category": "Electronics", "image": "⌨️"},
    {"id": "p4", "name": "Matte Stainless Steel Water Bottle", "price": 34.00, "description": "Double-wall vacuum insulated bottle that keeps drinks cold for up to 24 hours.", "category": "Lifestyle", "image": "🧉"},
    {"id": "p5", "name": "Recycled Canvas Daypack", "price": 75.00, "description": "Water-resistant, eco-friendly backpack featuring a dedicated 15-inch laptop sleeve.", "category": "Accessories", "image": "🎒"},
    {"id": "p6", "name": "Smart Ambient Desk Lamp", "price": 45.00, "description": "App-controlled LED lamp with adjustable color temperatures and sleep timers.", "category": "Lifestyle", "image": "💡"}
]

# ==========================================
# SIDEBAR: FILTERS & CART SUMMARY
# ==========================================
with st.sidebar:
    st.title("🛒 MiniStore Desk")
    st.write("Navigate & manage your order details below.")
    st.write("---")
    
    st.subheader("Filter Categories")
    categories = ["All Products", "Electronics", "Accessories", "Lifestyle"]
    selected_category = st.selectbox("Choose a category:", categories)
    
    st.write("---")
    st.subheader("Your Shopping Cart")
    
    if not st.session_state.cart:
        st.info("Your cart is currently empty.")
    else:
        total_cost = 0.0
        for pid, item in list(st.session_state.cart.items()):
            item_total = item['price'] * item['quantity']
            total_cost += item_total
            st.markdown(f"**{item['name']}**")
            st.markdown(f"Qty: {item['quantity']} × ${item['price']:.2f} = **${item_total:.2f}**")
            st.write("")
            
        st.write("---")
        st.markdown(f"### Total: `${total_cost:.2f}`")
        
        col_cart1, col_cart2 = st.columns(2)
        with col_cart1:
            if st.button("Checkout", type="primary", use_container_width=True):
                st.success("🎉 Thank you for your mock order!")
                st.session_state.cart = {}
        with col_cart2:
            st.button("Clear Cart", on_click=clear_cart, use_container_width=True)

# ==========================================
# MAIN PAGE CONTENT
# ==========================================
st.title("🛍️ MiniStore")
st.markdown("### Simple. Elegant. Premium.")
st.write(
    "Welcome to MiniStore, a curated marketplace for premium everyday essentials. "
    "Browse our handpicked collection of lifestyle goods and electronics designed to elevate your routine."
)
st.write("---")

if selected_category == "All Products":
    filtered_products = products
else:
    filtered_products = [p for p in products if p["category"] == selected_category]

st.subheader(f"Featured {selected_category if selected_category != 'All Products' else 'Items'}")

if filtered_products:
    for i in range(0, len(filtered_products), 3):
        cols = st.columns(3)
        for j in range(3):
            if i + j < len(filtered_products):
                product = filtered_products[i + j]
                with cols[j]:
                    st.markdown(
                        f"""
                        <div class="product-card">
                            <div style="font-size: 3rem; margin-bottom: 10px;">{product['image']}</div>
                            <span class="category-badge">{product['category']}</span>
                            <div class="product-title">{product['name']}</div>
                            <div class="product-price">${product['price']:.2f}</div>
                            <div class="product-desc">{product['description']}</div>
                        </div>
                        """, 
                        unsafe_allow_html=True
                    )
                    st.button(
                        f"Add to Cart", 
                        key=product['id'], 
                        on_click=add_to_cart, 
                        args=(product['id'], product['name'], product['price']),
                        use_container_width=True
                    )
else:
    st.warning("No products found in this category.")

st.write("---")
st.caption("© 2026 MiniStore Inc. Built entirely using Streamlit.")