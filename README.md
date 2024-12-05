
# IBM Stock & News Notification System

This Python-based system fetches real-time stock data and the latest news related to IBM (International Business Machines) and sends SMS notifications based on the stock price change. It integrates multiple APIs to get the necessary information and uses Twilio to send SMS updates.

## Features

- **Real-Time Stock Data**: Fetches daily stock price data for IBM using the [Alpha Vantage API](https://www.alphavantage.co/).
- **News Retrieval**: Fetches the latest news articles related to IBM using the [NewsAPI](https://newsapi.org/).
- **Stock Price Analysis**: Analyzes the stock price changes, calculating the percentage change between two consecutive days.
- **SMS Notifications**: Sends SMS notifications through [Twilio](https://www.twilio.com/) if the stock price increases, decreases, or stays the same, along with the latest news related to the stock.
- **Time Zone Handling**: Adjusts for the US Eastern Time Zone for accurate timestamps and notifications.

## Requirements

- Python 3.x
- `requests` library for API calls
- `twilio` library for sending SMS
- `pytz` library for timezone support
- `.env` file to store API keys and Twilio credentials (e.g., `STOCK_KEY`, `NEWS_KEY`, `ACCOUNT_SID`, `AUTH_TOKEN`, `TWILIO_PN`, `SAMPLE_NUMBER`)

## Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/ibm-stock-notification-system.git
   cd ibm-stock-notification-system
   ```

2. **Install the necessary libraries**:
   ```bash
   pip install requests twilio pytz
   ```

3. **Create a `.env` file** in the root directory and store your API keys and Twilio credentials. Example:

   ```ini
   STOCK_KEY=your_stock_api_key
   NEWS_KEY=your_news_api_key
   ACCOUNT_SID=your_twilio_account_sid
   AUTH_TOKEN=your_twilio_auth_token
   TWILIO_PN=your_twilio_phone_number
   SAMPLE_NUMBER=your_phone_number
   ```

4. **Run the script**:
   You can run the script using the following command:
   ```bash
   python stock_news_notification.py
   ```

## Script Workflow

1. **Stock Price Retrieval**:
   The system fetches IBM's stock price data for the most recent two days from Alpha Vantage using the `TIME_SERIES_DAILY` endpoint.

2. **News Retrieval**:
   The system fetches the latest news articles related to IBM from NewsAPI, filtering the results by the date.

3. **Price Analysis**:
   The system compares the stock prices of two consecutive days and calculates the percentage change.

4. **SMS Notifications**:
   Based on the stock price movement:
   - If the price increased: Sends a notification with the percentage increase and the latest news.
   - If the price decreased: Sends a notification with the percentage decrease and the latest news.
   - If there was no price change: Sends a notification indicating no change.
   
   All notifications are sent via Twilio to the phone number provided in the `.env` file.

## Example Output

When the stock price increases:
```
Date: December 02, 2024

IBM (International Business Machines) stock price increased from 123.45 to 125.67 📈
Percentage increase: 1.80%

Source: News API
Latest News: IBM announces new AI advancements.
```

When the stock price decreases:
```
Date: December 02, 2024

IBM (International Business Machines) stock price decreased from 125.67 to 123.45 📉
Percentage decrease: -1.80%

Source: News API
Latest News: IBM faces challenges in quarterly earnings.
```

When there is no price change:
```
No price changes as of December 02, 2024
```

## Environment Variables

Make sure to include the following environment variables in the `.env` file:

- `STOCK_KEY`: Your Alpha Vantage API key.
- `NEWS_KEY`: Your NewsAPI key.
- `ACCOUNT_SID`: Your Twilio account SID.
- `AUTH_TOKEN`: Your Twilio authentication token.
- `TWILIO_PN`: Your Twilio phone number.
- `SAMPLE_NUMBER`: The phone number to receive SMS notifications.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
