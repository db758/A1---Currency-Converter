"""
Unit test for module a1

When run as a script, this module invokes several procedures that 
test the various functions in the module a1.

Debasmita Bhattacharya db758 and Amelia Myers arm293
15 September 2017
"""

import cornell
import a1

def testA():
    """ Test procedure for the functions before_space and after_space """
    
    #Test case for string with only one space
    result1 = a1.before_space("0.838095 Euros")
    cornell.assert_equals = ("0.838095", result1)
    
    #Test case for string with more than one space i.e. four spaces
    result2 = a1.before_space("0.838095    Euros")
    cornell.assert_equals = ("0.838095", result2)
    
    #Test case for string starting with a space i.e. two spaces
    result3 = a1.before_space("  0.838095 Euros")
    cornell.assert_equals = ("0.838095", result3)
    
    #Test case for string ending with a space
    result4 = a1.before_space("0.838095 Euros ")
    cornell.assert_equals = ("0.838095", result4)
    
    #Test case for string with no space but ending with a space
    result28 = a1.before_space("0.838095Euros ")
    cornell.assert_equals = ("0.838095Euros", result28)
    
    #Test case for string with no space but starting with a space
    result29 = a1.before_space(" 0.838095Euros")
    cornell.assert_equals = ("", result29)
    
    #Test case for string that is only a space
    result30 = a1.before_space(" ")
    cornell.assert_equals = ("", result30)
    
    #Test case for string with only one space
    result5 = a1.after_space("0.838095 Euros")
    cornell.assert_equals = ("Euros", result5)
    
    #Test case for string with more than one space i.e. four spaces
    result6 = a1.after_space("0.838095    Euros")
    cornell.assert_equals = ("Euros", result6)
    
    #Test case for string starting with a space i.e. two spaces
    result7 = a1.after_space("  0.838095 Euros")
    cornell.assert_equals = ("Euros", result7)
    
    #Test case for string ending with a space
    result8 = a1.after_space("0.838095 Euros ")
    cornell.assert_equals = ("Euros", result8)
    
    #Test case for string with no space but ending with a space
    result31 = a1.after_space("0.838095Euros ")
    cornell.assert_equals = ("", result31)
    
    #Test case for string with no space but starting with a space
    result32 = a1.after_space(" 0.838095Euros")
    cornell.assert_equals = ("0.838095Euros", result32)
    
    #Test case for string that is only a space
    result33 = a1.after_space(" ")
    cornell.assert_equals = ("", result33)

def testB():
    """Test procedure for functions first_inside_quotes, get_lhs(json), get_rhs(json), and has_error(json)"""
    #Test case for general string with only one set of double quotes
    result9 = a1.first_inside_quotes('A "B C" D')
    cornell.assert_equals = ('B C', result9)
    
    #Test case for nothing inside the double quotes
    result10 = a1.first_inside_quotes('A "" C')
    cornell.assert_equals = ('', result10)
    
    #Test case for two sets of double quotes in the string
    result11 = a1.first_inside_quotes('A "B" "C" D')
    cornell.assert_equals = ('B', result11)
    
    #Test case for whole string inside double quotes
    result34 = a1.first_inside_quotes('"B"')
    cornell.assert_equals = ('B', result34)
    
    #Test case for given a general lhs currency query
    result12 = a1.get_lhs('{"success" : true, "lhs" : "2 United States Dollars", "rhs" : "1.825936 Euros", "error":""}')
    cornell.assert_equals = ('2 United States Dollars', result12)
    
    #Test Case for an invalid lhs currency query
    result13 = a1.get_lhs('{"success" : false, "lhs" : "2 AAA", "rhs" : "3 BBB", "error" : "Currency amount is invalid." }')
    cornell.assert_equals = ('', result13)
    
    #Test case for given a general rhs currency query
    result14 = a1.get_rhs('{"success" : true, "lhs" : "2 United States Dollars", "rhs" : "1.825936 Euros", "error":""}')
    cornell.assert_equals = ('1.825936 Euros', result14)
    
    #Test Case for an invalid rhs currency query
    result15 = a1.get_rhs('{"success" : false, "lhs" : "2 AAA", "rhs" : "3 BBB", "error" : "Currency amount is invalid." }')
    cornell.assert_equals = ('', result15)
    
    #Test case for a valid currency query
    result16 = a1.has_error('{"success" : true, "lhs" : "2 United States Dollars", "rhs" : "1.825936 Euros", "error":""}')
    cornell.assert_equals = (False, result16)
    
    #Test case for an invalid currency query
    result17 = a1.has_error('{"success" : false, "lhs" : "", "rhs" : "", "error":"Source currency code is invalid."}')
    cornell.assert_equals = (True, result17)
    

def testC():
    """Test procedure for the function currency_response"""
    #Test case for valid currency_from
    result18 = a1.currency_response('USD', 'HKD', 1.0)
    cornell.assert_equals = ('{ "success" : true, "lhs" : "1 United States Dollar", "rhs" : "7.82541 Hong Kong Dollars", "error" : "" }', result18)
    
    #Test case for invalid currency_from
    result19 = a1.currency_response('AAA', 'HKD', 1.0)
    cornell.assert_equals = ('{ "success" : false, "lhs" : "", "rhs" : "", "error" : "Source currency code is invalid." }', result19)
    
    #Test case for invalid currency_from
    result20 = a1.currency_response('usd', 'HKD', 1.0)
    cornell.assert_equals = ('{ "success" : false, "lhs" : "", "rhs" : "", "error" : "Source currency code is invalid." }', result20)
    
    #Test case for invalid currency_to
    result21 = a1.currency_response('USD', 'hkd', 1.0)
    cornell.assert_equals = ('{ "success" : false, "lhs" : "", "rhs" : "", "error" : "Exchange currency code is invalid." }', result21)
    
    #Test case for invalid currency_to
    result22 = a1.currency_response('USD', 'BBB', 1.0)
    cornell.assert_equals = ('{ "success" : false, "lhs" : "", "rhs" : "", "error" : "Exchange currency code is invalid." }', result22)
    
    #Test case for invalid amount_from
    result23 = a1.currency_response('USD', 'HKD', 10.0e100000)
    cornell.assert_equals = ('{ "success" : true, "lhs" : "INF United States Dollars", "rhs" : "INF Hong Kong Dollars", "error" : "" }', result23)
    

def testD():
    """Test procedure for functions iscurrency and exchange"""
    #Test case for valid iscurrency
    result24 = a1.iscurrency('USD')
    cornell.assert_equals = (True, result24)
    
    #test case for invalid iscurrency
    result25 = a1.iscurrency('AAA')
    cornell.assert_equals = (False, result25)
    
    #Test case for invalid iscurrency
    result26 = a1.iscurrency('usd')
    cornell.assert_equals = (False, result26)

    #Test case for valid exchange
    result27 = a1.exchange('USD','HKD',1.0)
    cornell.assert_floats_equal(7.82541, result27)


testA()
testB()
testC()
testD()
print("Module a1 passed all tests")