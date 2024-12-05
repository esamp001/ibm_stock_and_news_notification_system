
# IBM Stock News and Notification System

This script fetches IBM stock prices and relevant news articles, calculates the percentage change in stock prices, and sends text notifications based on the changes. The notifications include significant price changes or lack thereof, as well as recent news updates. It uses the Alpha Vantage API for stock data, the News API for news articles, and Twilio for SMS notifications.

## Prerequisites

### Required Libraries
Install the following Python libraries:
- `requests`
- `pytz`
- `twilio`

Use pip to install them:
```bash
pip install requests pytz twilio
```

### Environment Variables
Set the following environment variables for secure access to API keys and credentials:
- `STOCK_KEY`: Your Alpha Vantage API key.
- `NEWS_KEY`: Your News API key.
- `ACCOUNT_SID`: Your Twilio Account SID.
- `AUTH_TOKEN`: Your Twilio Auth Token.
- `TWILIO_PN`: Your Twilio phone number.
- `SAMPLE_NUMBER`: The recipient's phone number.

You can use a `.env` file and load it with the `dotenv` package, or configure them directly in your environment.

### APIs Used
- **Alpha Vantage API**: Fetches daily stock prices for IBM.
- **News API**: Retrieves the latest news articles related to IBM stock.
- **Twilio API**: Sends SMS notifications about stock changes and related news.

## Features

1. **Stock Price Analysis**:
   - Compares the latest two days of stock data to determine the percentage change.
   - Identifies if the stock price has increased, decreased, or remained constant.

2. **News Retrieval**:
   - Fetches the latest IBM-related news articles.
   - Formats and includes relevant news content in notifications.

3. **SMS Notifications**:
   - Sends detailed notifications via SMS based on stock price changes:
     - **Increase**: Notifies with the percentage increase and a positive news update.
     - **Decrease**: Notifies with the percentage decrease and a warning or critical news update.
     - **No Change**: Notifies when there are no significant price changes.

## Configuration

### Time Zone
The script uses the `US/Eastern` timezone for date and time calculations. Modify the timezone as needed:
```python
US_timezone = pytz.timezone("US/Eastern")
```

### Test Dates and Stock Data
Test data and variables such as `test` and `test_news` can be replaced with dynamic or real-time data.

## How to Use

1. **Set Environment Variables**:
   Ensure all required environment variables are set correctly.

2. **Run the Script**:
   Execute the script to fetch stock prices, news articles, and send notifications:
   ```bash
   python script_name.py
   ```

3. **Interpreting the Output**:
   - The script prints stock data and date information to the console.
   - SMS messages are sent based on stock price analysis and news availability.

## Example Output

### SMS Notification for Price Increase:
```
Date: December 2, 2024

IBM (International Business Machines) stock price increase from 140.50 to 145.00 📈
Percentage increase: 3.21%

Source: Bloomberg

 IBM Stock Shows Resurgence Amid Market Rally.
 Shares climb to new heights as the market reacts positively.
 Investors remain optimistic.
```

### SMS Notification for Price Decrease:
```
Date: December 2, 2024

IBM (International Business Machines) stock price decrease from 145.00 to 140.50 📉
Percentage decrease: 3.21%

Source: Reuters

 IBM Faces Challenges Amid Economic Shifts.
 The tech giant struggles to maintain growth momentum.
 Experts weigh in on future strategies.
```

### SMS Notification for No Changes:
```
No price changes as of December 2, 2024
```

## Additional Notes
- Handle sensitive data securely using environment variables.
- The News API limits the number of free requests per day. Ensure adequate quota for production use.
- The script includes error handling for SMS delivery failures.

## License
This script is open for personal use and adaptation. Please adhere to the API usage policies of Alpha Vantage, News API, and Twilio.

## Author
[esamp001](https://github.com/esamp001)
