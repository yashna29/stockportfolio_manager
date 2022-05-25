#Yahoo Finance Library - https://github.com/ranaroussi/yfinance - User: ranaroussi

#importing the Yahoo Finance Library into the program to gather necessary data
import yfinance as yf

# importing date and time libraries to display current date and time when displaying portfolio
import time
from datetime import date

# initializing global lists for tickers and number of shares for each
ticker_list = []
shares_list = []
current_market_price_list = []

# Creating portfolio for user
def create_portfolio (tmp_tckr_symbol, tmp_shares):
  ticker_list.append(tmp_tckr_symbol)
  shares_list.append(tmp_shares)

# Update portfolio for user
def update_portfolio (operation):
  # operation can have values 'ADD' or 'DELETE'
  global ticker_list, shares_list, current_market_price_list, investment_value_list
  # adding a new stock to the portfolio
  if (operation == "ADD"):    
    tmp_tckr_symbol = (input("Enter the stock ticker symbol you want to add: "))
    tmp_shares_held = int(input("Enter the number of shares you own for "  + tmp_tckr_symbol + ": " ))
    create_portfolio(tmp_tckr_symbol, tmp_shares_held)
  # deleting a stock from the portfolio
  elif (operation == "DELETE"):
    tmp_tckr_symbol = input("Enter the ticker symbol of the stock you want to delete: ")
    for i in range(len(ticker_list)):
      if (ticker_list[i].upper() == tmp_tckr_symbol.upper()):
        ticker_list.pop(i)
        shares_list.pop(i)
        current_market_price_list.pop(i)
        investment_value_list.pop(i)
        break

# Displaying portfolio for user 
def display_portfolio():
  curr_time = (time.strftime("%H:%M:%S"))
  today = date.today()
  print ("\nYour portfolio as of " + str(today) + " " + str(curr_time) + " :")
  print ("#\tTicker\t\t # of shares\t Current Market Price\t Value")
  print ("-----------------------------------------------------------------------")
  for i in range(len(ticker_list)):
    print (str(i+1) + "\t" + ticker_list[i] + "\t\t\t" + str(shares_list[i]) + "\t\t" + str(current_market_price_list[i]) + "\t\t" + str(investment_value_list[i]))
  print ("\nYour total portfolio value is $" + str(round(portfolio_value, 2)))

# Gathering the current market price for each ticker present in ticker_list
def get_market_price_for_tickers():
  global ticker_list, current_market_price_list
  current_market_price_list = []
  for tckr in ticker_list:
    print (tckr)
    ticker_data = yf.Ticker(tckr)
    print (ticker_data)
    print (ticker_data.info['regularMarketPrice'])
    current_market_price_list.append(round(ticker_data.info['regularMarketPrice'], 2))

# calculating total value of portfolio
def calculate_portfolio_value():
  global portfolio_value
  global investment_value_list
  investment_value_list = []
  # calculating investment value for each stock holding
  for i in range(len(shares_list)):
    investment_value_for_ticker = round(shares_list[i] * current_market_price_list[i],2)
    investment_value_list.append(investment_value_for_ticker)
  # calculating total portfolio value
  portfolio_value = 0
  for val in range(0, len(investment_value_list)):
    portfolio_value = portfolio_value + investment_value_list[val]

# sorting the portfolio
def sort_portfolio(field_name, sort_order):
  # field_name expects one of these values: 'T' for ticker , 'S' for number of shares, 'M' for current market price, 'V' for investment value
  # sort_order expects one of these values: 'ASC' for ascending, 'DESC' for descending 
  global ticker_list, shares_list, current_market_price_list, investment_value_list
  # sorting by ticker symbol in ascending order
  if (field_name == 'T' and sort_order == 'A'):
    zipped_lists = zip(ticker_list, shares_list, current_market_price_list, investment_value_list)
    sorted_pairs = sorted(zipped_lists)
    tuples = zip(*sorted_pairs)
    ticker_list, shares_list, current_market_price_list, investment_value_list = [ list(tuple) for tuple in  tuples]
  # sorting by ticker symbol in descending order
  elif (field_name == 'T' and sort_order == 'D'):
    zipped_lists = zip(ticker_list, shares_list, current_market_price_list, investment_value_list)
    sorted_pairs = sorted(zipped_lists, reverse=True)
    tuples = zip(*sorted_pairs)
    ticker_list, shares_list, current_market_price_list, investment_value_list = [ list(tuple) for tuple in  tuples]
  # sorting by number of shares in ascending order
  if (field_name == 'S' and sort_order == 'A'):
    zipped_lists = zip(shares_list, current_market_price_list, investment_value_list, ticker_list)
    sorted_pairs = sorted(zipped_lists)
    tuples = zip(*sorted_pairs)
    shares_list, current_market_price_list, investment_value_list, ticker_list = [ list(tuple) for tuple in  tuples]
  # sorting by number of shares in descending order
  elif (field_name == 'S' and sort_order == 'D'):
    zipped_lists = zip(shares_list, current_market_price_list, investment_value_list, ticker_list)
    sorted_pairs = sorted(zipped_lists, reverse = True)
    tuples = zip(*sorted_pairs)
    shares_list, current_market_price_list, investment_value_list, ticker_list = [ list(tuple) for tuple in  tuples]
  # sorting by current market price in ascending order
  if (field_name == 'M' and sort_order == 'A'):
    zipped_lists = zip(current_market_price_list, investment_value_list, ticker_list, shares_list)
    sorted_pairs = sorted(zipped_lists)
    tuples = zip(*sorted_pairs)
    current_market_price_list, investment_value_list, ticker_list, shares_list = [ list(tuple) for tuple in  tuples]
  # sorting by current market price in descending order
  elif (field_name == 'M' and sort_order == 'D'):
    zipped_lists = zip(current_market_price_list, investment_value_list, ticker_list, shares_list)
    sorted_pairs = sorted(zipped_lists, reverse = True)
    tuples = zip(*sorted_pairs)
    current_market_price_list, investment_value_list, ticker_list, shares_list = [ list(tuple) for tuple in  tuples]
  # sorting by investment value in ascending order
  if (field_name == 'V' and sort_order == 'A'):
    zipped_lists = zip(investment_value_list, ticker_list, shares_list, current_market_price_list)
    sorted_pairs = sorted(zipped_lists)
    tuples = zip(*sorted_pairs)
    investment_value_list, ticker_list, shares_list, current_market_price_list = [ list(tuple) for tuple in  tuples]
  # sorting by investment value in descending order
  elif (field_name == 'V' and sort_order == 'D'):
    zipped_lists = zip(investment_value_list, ticker_list, shares_list, current_market_price_list)
    sorted_pairs = sorted(zipped_lists, reverse = True)
    tuples = zip(*sorted_pairs)
    investment_value_list, ticker_list, shares_list, current_market_price_list = [ list(tuple) for tuple in  tuples]

# displaying menu options for user to choose
def display_menu_options_and_process_user_actions():
  while (True):
    str_menu_msg = "\nMenu:"
    str_underline_msg = "\n--------------------------------------------"
    str_refresh_msg = "\n  Refresh portfolio : Enter R"
    str_sort_msg = "\n  Sorting options:"
    str_ticker_sort_msg = "\n    Sort by ticker : Enter T"
    str_no_of_shares_msg = "\n    Sort by number of shares : Enter S"
    str_current_market_price_msg = "\n    Sort by current market price : Enter M"
    str_value_msg = "\n    Sort by investment value : Enter V"
    str_add_msg = "\n  Add Stock : Enter +"
    str_delete_msg = "\n  Delete Stock : Enter -"
    str_quit_msg = "\n  To quit this program, Enter Q"
    str_enter_preference_msg = ("\nEnter your input: ") 
    # gathering user response based on list of given options
    user_response = input(str_menu_msg + str_underline_msg + str_refresh_msg + str_sort_msg + str_ticker_sort_msg +  str_no_of_shares_msg  +
                        str_current_market_price_msg + str_value_msg + str_add_msg + str_delete_msg + str_quit_msg +  str_enter_preference_msg)
    # if user wants to refresh portfolio, the program will rerun to receive updated values
    if (user_response == "R"):
      get_market_price_for_tickers()
      calculate_portfolio_value()
      display_portfolio()
    # if user wants to add a stock ticker, the update_portfolio function will be called, with the parameter value of "ADD"
    elif (user_response == "+"):
      update_portfolio ("ADD")
      get_market_price_for_tickers()
      calculate_portfolio_value()
      display_portfolio()
    # if user wants to delete a stock ticker, the update_portfolio function will be called, with the parameter value of "DELETE"
    elif (user_response == "-"):
      update_portfolio ("DELETE")
      get_market_price_for_tickers()
      calculate_portfolio_value()
      display_portfolio()
    # f user wants to quit the program
    elif (user_response == "Q"):
      print ("\n\n\n\n\n")
      break
    # if any other option is selected ("T", "S", "M", or "V"), the user is asked if they would like to sort in ascending or descending order
    else:
      sort_order = input("Enter A for ascending or D for descending: ")
      get_market_price_for_tickers()
      calculate_portfolio_value()
      sort_portfolio(user_response, sort_order) 
      display_portfolio()

# welcome message
print ("\n*** Welcome to your Investment Portfolio Manager ***")

# asks user for # of securities
security_number = int(input("\nEnter the number of securities in your portfolio: "))

# input stock tickers for each security in portfolio
for i in range(security_number):
  tckr_symbol = (input("Enter the stock ticker symbol: "))
  shares_held = int(input("Enter the number of shares you own for "  + tckr_symbol + ": " ))
  create_portfolio(tckr_symbol, shares_held)

# calling functions to execute required processes
get_market_price_for_tickers()
calculate_portfolio_value()
display_portfolio()
# display menu options for user to perform refresh, sorting, add, delete and quit operations
display_menu_options_and_process_user_actions()