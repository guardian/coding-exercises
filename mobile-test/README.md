# Mobile Test: API Fetch & Navigation

## Overview:
Create a simple mobile app (in Swift for iOS or Kotlin for Android) that fetches data from an external API and displays it on a second screen when a button is clicked. The goal is to evaluate basic mobile development skills, including API calls, navigation, and UI handling.

---

## Tasks:

1. **Set Up the Project**:
    - Create a new mobile project (iOS or Android) with a single page containing a button.

2. **API Call**:
    - Make a GET request to the `https://dummyjson.com/products` API.
    - Parse the response, specifically fetching the title of the first product in the response.

3. **UI - Main Screen**:
    - The main screen should contain:
        - A title: "Product Viewer"
        - A button labeled: "Fetch Product"

4. **Navigation**:
    - When the button is clicked:
        - Fetch the data from the API.
        - Navigate to a second screen.

5. **UI - Second Screen**:
    - The second screen should display the title of the first product received from the API.

---

## Bonus Tasks:

1. **Loading Indicator**:
    - Show a loading indicator when the API call is in progress.

2. **Error Handling**:
    - Display an alert if the API call fails, with a retry option.

3. **UI Enhancements**:
    - Display more product details (such as price or description) on the second screen.
    - Improve the layout with additional styling and visual elements.

---

## Requirements:

- Use Swift (iOS) or Kotlin (Android).
- Fetch data from the API endpoint: `https://dummyjson.com/products`.
- Display the first product's title on a new screen after the button is pressed.
- Provide basic navigation between screens.