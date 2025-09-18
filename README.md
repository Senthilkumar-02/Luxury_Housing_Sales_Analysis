🏠 Luxury Housing Sales Analysis – Bengaluru
This project presents an end-to-end data analysis and visualization of Bengaluru’s luxury housing market. Using real estate sales dataset of 100,000+ , it explores market trends, buyer preferences, and developer performance through interactive dashboards and insights.

Key Features

* Micro-Market Trends → Track booking volumes quarter by quarter across different Bengaluru micro-markets.

* Builder Performance → Identify top developers by revenue, booking success rate, and ticket size.

* Buyer Insights → Analyze buyer types (End-User, Investor, NRI) and how possession status influences decision-making.

* Configuration Demand → Discover which housing types (3BHK, 4BHK, etc.) are most in-demand.

* Sales Channels → Evaluate the effectiveness of different booking channels.

* Amenity Impact → Correlate amenity scores with booking conversion rates.

Tech Support

* Data Processing → SQL, Python (Pandas, NumPy)

* Visualization & BI → Power BI (DAX, interactive dashboards)

* Database → PostgreSQL / MySQL

Python – Data Preparation & Feature Engineering

Cleaned 100k+ raw records (removed duplicates, nulls, and inconsistencies). 
Filled missing numerical values using median or mean depending on the column (e.g., Unit_Size_Sqft → mean, Amenity_Score → mean, Ticket_Price_Cr → median). 
Normalized string columns: Micro_Market, Configuration, Ticket_Price_Cr. Standardized configuration labels: '3 BHK' → '3BHK', '4BHK+' → '4BHK+', etc. 
Handled missing comments: Buyer_Comments filled with 'No Comment'. 
Removed(1000) duplicate rows to ensure dataset consistency.

Price_per_Sqft = (Ticket_Price_Cr * 10000000) / Unit_Size_Sqft Quarter_Number = Extracted from Purchase_Quarter Booking_Flag = 1 if Status == 'Booked' else 0

📂 Output → A clean, analysis-ready dataset.

SQL – Load Clean Data into RDBMS

Power BI – Visualization & Insights

Connected dashboard to SQL database.

Built interactive visuals with filters (Builder, Market, Quarter, Price Range).

Created custom DAX measures:

Booking Conversion Rate (%)

Average Ticket Price per Builder

Market Share by Micro-Market

Revenue per Sqft

Professional Insights (from 100,000+ Records)

Builder Concentration

Top 5 builders control ~48% of revenue and 42% of bookings → intense competition at the top tier.

📈 Quarterly Growth

Consistent 12–15% sales spike in Q2, driven by festive demand and investor-led activity.

🎯 Booking Efficiency

Market-wide conversion averages 27%.

Premium builders with strong brand equity reach 35–40% conversion.

🌍 Geographic Insights

South Bengaluru leads luxury housing demand.

Tier-2 localities show ~20% YoY growth, emerging as future growth hubs.

Buyer Trends

3BHK is the most in-demand configuration.

Strong demand in the ₹1.5–2.5 Cr ticket size range.

Projects with eco-luxury features & smart amenities see 15–20% higher conversion.


Results

100,000+ records cleaned, standardized, and stored in a relational SQL database.

Developed an interactive Power BI dashboard with dynamic filters and drill-down insights.

Delivered builder, buyer, and market-level intelligence to support strategic real estate decisions.

Replicated a real-world BI pipeline — from data ingestion → transformation → visualization → business insights.
