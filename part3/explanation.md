## Part 3: Low-Stock Alerts API

**Assumptions & Edge Cases**

• No recent sales → no alert  
• Zero sales velocity → no stockout estimate  
• Missing supplier → safe null handling  
• Multiple warehouses supported  

**Scalability Considerations**

• Precompute alerts via background jobs  
• Cache sales velocity metrics  
• Add pagination for large datasets
