"""Categories Module for Grocio — Smart Grocery Booking System.

Defines the 7 core grocery categories, category cards rendering,
category selection, and seamless navigation to the Shop page.
"""

import os
import streamlit as st

CATEGORIES_DATA = [
    {
        "name": "Vegetables",
        "icon": "🥦",
        "tagline": "Farm-fresh daily harvest",
        "description": "Crisp green vegetables, fresh leafy greens, and cooking essentials straight from local farms.",
        "popular_items": "Tomatoes, Potatoes, Onions, Spinach, Carrots",
        "image": 'https://loremflickr.com/600/400/tomatoes,vegetable?lock=101',
    },
    {
        "name": "Fruits",
        "icon": "🍎",
        "tagline": "Juicy, seasonal & sweet",
        "description": "Naturally ripened apples, sweet bananas, golden mangoes, and antioxidant-rich berries.",
        "popular_items": "Apples, Bananas, Alphonso Mangoes, Oranges",
        "image": 'https://loremflickr.com/600/400/mango,fruit?lock=111',
    },
    {
        "name": "Dairy",
        "icon": "🥛",
        "tagline": "Pure farm goodness",
        "description": "Pasteurized fresh milk, thick curd, creamy malai paneer, butter, and cheese slices.",
        "popular_items": "Full Cream Milk, Dahi, Butter, Malai Paneer",
        "image": 'https://loremflickr.com/600/400/milk,bottle?lock=114',
    },
    {
        "name": "Bakery",
        "icon": "🍞",
        "tagline": "Oven-fresh delights",
        "description": "Whole wheat bread, soft burger buns, flaky croissants, and artisanal butter cookies.",
        "popular_items": "Brown Bread, Burger Buns, Choco Cookies",
        "image": 'https://loremflickr.com/600/400/whole,wheat,bread?lock=119',
    },
    {
        "name": "Snacks",
        "icon": "🍟",
        "tagline": "Crunchy munchies & treats",
        "description": "Crispy salted potato chips, digestive biscuits, rich dark chocolate, and spicy namkeens.",
        "popular_items": "Potato Chips, Dark Chocolate, Aloo Bhujia",
        "image": 'https://loremflickr.com/600/400/potato,chips?lock=123',
    },
    {
        "name": "Beverages",
        "icon": "☕",
        "tagline": "Refreshing sips & brews",
        "description": "Premium Assam leaf tea, South Indian roast filter coffee, pure orange juice, and mineral water.",
        "popular_items": "Assam Tea, Filter Coffee, Orange Juice",
        "image": 'https://loremflickr.com/600/400/black,tea,cup?lock=128',
    },
    {
        "name": "Staples",
        "icon": "🍚",
        "tagline": "Kitchen pantry essentials",
        "description": "Aged aromatic Basmati rice, chakki fresh wheat atta, crystal sugar, iodized salt, and cooking oils.",
        "popular_items": "Basmati Rice, Sharbati Atta, Sunflower Oil",
        "image": 'https://loremflickr.com/600/400/basmati,rice?lock=131',
    },
]


def get_all_categories() -> list:
    """Return all category definitions."""
    return CATEGORIES_DATA


def get_category_names() -> list:
    """Return list of all category names."""
    return [c["name"] for c in CATEGORIES_DATA]


def render_categories_page() -> None:
    """Render the dedicated Categories catalogue page."""
    st.title("Grocery Categories")
    st.caption("Explore all 7 grocery departments to find fresh essentials for your home.")

    # 3-column grid for categories
    cols = st.columns(3)
    for idx, cat in enumerate(CATEGORIES_DATA):
        col = cols[idx % 3]
        with col:
            with st.container(border=True):
                # Category image or icon
                if cat["image"].startswith(("http://", "https://")) or os.path.exists(cat["image"]):
                    st.image(cat["image"], width="stretch")
                
                st.subheader(f"{cat['icon']} {cat['name']}")
                st.caption(f"**{cat['tagline']}**")
                st.write(cat["description"])
                st.write(f"**Includes:** {cat['popular_items']}")
                
                btn_key = f"cat_browse_btn_{cat['name'].lower()}"
                if st.button(f"Browse {cat['name']}", key=btn_key, type="primary", use_container_width=True):
                    st.session_state.selected_category = cat["name"]
                    st.session_state.search_query = ""
                    st.session_state.current_page = "Shop"
                    st.rerun()

    st.write("")
    with st.container(border=True):
        st.write("💡 **Quick tip:** Looking for something specific across all categories? Use our global catalog search.")
        if st.button("Explore All Products", key="cat_explore_all_btn"):
            st.session_state.selected_category = "All"
            st.session_state.search_query = ""
            st.session_state.current_page = "Shop"
            st.rerun()


def render_featured_categories_preview() -> None:
    """Render featured category cards for the Homepage."""
    st.header("Featured Categories")
    st.caption("Quickly jump into your favorite grocery aisles.")

    # Show all 7 categories in clean columns (4 in row 1, 3 in row 2)
    row1 = st.columns(4)
    for i in range(4):
        cat = CATEGORIES_DATA[i]
        with row1[i]:
            with st.container(border=True):
                if cat["image"].startswith(("http://", "https://")) or os.path.exists(cat["image"]):
                    st.image(cat["image"], width="stretch")
                st.subheader(f"{cat['icon']} {cat['name']}")
                st.caption(cat["tagline"])
                if st.button(f"Shop {cat['name']}", key=f"home_cat_btn_{cat['name'].lower()}", use_container_width=True):
                    st.session_state.selected_category = cat["name"]
                    st.session_state.search_query = ""
                    st.session_state.current_page = "Shop"
                    st.rerun()

    st.write("")
    row2 = st.columns(3)
    for i in range(3):
        cat = CATEGORIES_DATA[4 + i]
        with row2[i]:
            with st.container(border=True):
                if cat["image"].startswith(("http://", "https://")) or os.path.exists(cat["image"]):
                    st.image(cat["image"], width="stretch")
                st.subheader(f"{cat['icon']} {cat['name']}")
                st.caption(cat["tagline"])
                if st.button(f"Shop {cat['name']}", key=f"home_cat_btn_{cat['name'].lower()}", use_container_width=True):
                    st.session_state.selected_category = cat["name"]
                    st.session_state.search_query = ""
                    st.session_state.current_page = "Shop"
                    st.rerun()
