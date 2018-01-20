""" 
Module for currency exchange

This module provides several string parsing functions to implement a 
simple currency exchange routine using an online currency service. 
The primary function in this module is exchange.

Debasmita Bhattacharya db758 and Amelia Myers arm293
15 September 2017
"""

def before_space(s):
    """Returns: Substring of s; up to, but not including, the first space
    
    Parameter s: the string to slice
    Precondition: s has at least one space in it"""
    
    #Find and store the first part before the space
    start = s[0:]
    #Find the index of the space
    space_1 = s.index(' ')
    #Return the final number
    return start[:space_1]


def after_space(s): 

    """ Returns: Substring of s after the first space
    
    Parameter s: the string to slice
    Precondition: s has at least one space in it"""
    
    #Find the first space
    space_2 = s.index(' ')
    #Store the part after the space = Euros"
    middle_after = s[space_2+1:]
    #Return the final word
    return middle_after


def first_inside_quotes(s):

    """ Returns: The first substring of s between two (double) quote characters
    
    A quote character is one that is inside a string, not one that delimits it. We typically use single quotes (') to delimit a string if want to use a double quote character (") inside of it.
    
    Example: If s is 'A "B C" D', this function returns 'B C'
    Example: If s is 'A "B C" D "E F" G', this function still returns 'B C' because it only picks the first such substring.
    
    Parameter s: a string to search
    Precondition: s is a string with at least two (double) quote characters inside. """
    
    #Find the first double quote
    start_2 = s.index('"')
    #store the part after the first double quote
    middle = s[start_2+1:]
    #find the second double quote
    end = middle.index('"')
    #return the result
    return middle[:end]


def get_lhs(json):
    
    """Returns: The LHS value in the response to a currency query.
    
    Given a JSON response to a currency query, this returns the string inside double quotes (") immediately following the keyword "from". For example, if the JSON is
    
    '{"success":true, "lhs":"2 United States Dollars", "rhs":"1.825936 Euros", "error":""}'
    then this function returns '2 United States Dollars' (not '"2 United States Dollars"'). It returns the empty string if the JSON is the result of on invalid query.
    
    Parameter json: a json string to parse
    Precondition: json is the response to a currency query"""
    
    #Find "lhs" in the JSON 
    find_lhs = json.index('lhs')
    #Find currency query
    find_currencyquerylhs = json.index(':', find_lhs)
    #find first inside quotes for the currency query
    currency_query_lhs = first_inside_quotes(json[find_currencyquerylhs:])
    #Return the currency query
    return currency_query_lhs


def get_rhs(json):

    """ Returns: The RHS value in the response to a currency query.
    
    Given a JSON response to a currency query, this returns the string inside double quotes (") immediately following the keyword "rhs". For example, if the JSON is
    
      '{"success":true, "lhs":"2 United States Dollars", "rhs":"1.825936 Euros", "error":""}'
    then this function returns '1.825936 Euros' (not '"1.825936 Euros"'). It returns the empty string if the JSON is the result of on invalid query.
    
    Parameter json: a json string to parse
    Precondition: json is the response to a currency query"""
    
    #Find "rhs" in the JSON 
    find_rhs = json.index('rhs')
    #find currency query
    find_currencyqueryrhs = json.index(':', find_rhs)
    #find first inside quotes for the currency query
    currency_query_rhs = first_inside_quotes(json[find_currencyqueryrhs:])
    #Return the currency query
    return currency_query_rhs


def has_error(json):

    """ Returns: True if the query has an error; False otherwise.
    
    Given a JSON response to a currency query, this returns the opposite of the value following the keyword "success". For example, if the JSON is
    
      '{"success":false, "lhs":"", "rhs":"", "error":"Source currency code is invalid."}'
    then the query is not valid, so this function returns True (It does NOT return the message 'Source currency code is invalid').
    
    Parameter json: a json string to parse
    Precondition: json is the response to a currency query"""
    
    #Find "false" in the JSON
    find_false = 'false' in json
    return find_false
   

def currency_response(currency_from, currency_to, amount_from):
    """
    Returns: a JSON string that is a response to a currency query.
    
    A currency query converts amount_from money in currency currency_from 
    to the currency currency_to. The response should be a string of the form
    
        '{"success":true, "lhs":"<old-amt>", "rhs":"<new-amt>", "error":""}'
    
    where the values old-amount and new-amount contain the value and name for the 
    original and new currencies. If the query is invalid, both old-amount and 
    new-amount will be empty, while "success" will be followed by the value false.
    
    Parameter currency_from: the currency on hand (the LHS)
    Precondition: currency_from is a string
    
    Parameter currency_to: the currency to convert to (the RHS)
    Precondition: currency_to is a string
    
    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float
    """
    
    import cornell
    
    url_template = 'http://cs1110.cs.cornell.edu/2017fa/a1server.php?src=' + str(currency_from) + '&dst=' + str(currency_to) + '&amt=' + str(amount_from)
    json_string = str(cornell.urlread(url_template))
    return json_string 
   
    #use a general url to produce a json string 
    #taking variables that user inputs into URL and inserting it in the JSON string
    
    
def iscurrency(currency):
    """
    Returns: True if currency is a valid (3 letter code for a) currency. 
    It returns False otherwise.
    
    Parameter currency: the currency code to verify
    Precondition: currency is a string.
    """
    
    x = currency_response(currency, 'HKD', 1.0)
    y = has_error(x)
    return y != True 
 
   
def exchange(currency_from,currency_to,amount_from):
    """
    Returns: amount of currency received in the given exchange.

    In this exchange, the user is changing amount_from money in currency 
    currency_from to the currency currency_to. The value returned represents the 
    amount in currency currency_to.

    The value returned has type float.

    Parameter currency_from: the currency on hand (the LHS)
    Precondition: currency_from is a string for a valid currency code
    
    Parameter currency_to: the currency to convert to (the RHS)
    Precondition: currency_to is a string for a valid currency code
    
    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float
    """
    
    x2 = currency_response(currency_from,currency_to,amount_from)
    y2 = get_rhs(x2) 
    z2 = before_space(y2)
    return float(z2)

    
    