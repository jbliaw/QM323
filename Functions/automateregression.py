class AutomateRegression: 
    
    def automateregression(df): 
        # Rename columns so they're easier to grab
        df = df.rename(columns={"Price high": "pricehigh", 
                   "Price low": "pricelow", 
                   "atribute 2 high": "attribute2high",
                   "attribute 3 high": "attribute3high", 
                   "attribute 4 high": "attribute4high"}, errors='raise')
        
        # Create a list of customers to iterate through
        listofcustomers = []
        for (columns, columndata) in df.iteritems():
            if columns.startswith("Customer"):
                listofcustomers.append(columns)
            else: continue
            
        # Create an empty dataframe (theresults) with proper column names
        theresults = pd.DataFrame(columns = ['Intercept', 'pricehigh', 'pricelow', 'attribute2high', 'attribute3high', 'attribute4high'])
        
        # Iterating thru each customer and running regressions
        for eachcustomer in listofcustomers:
            customer = eachcustomer
            # Run regressions
            mod = smf.ols(formula = '{} ~ pricehigh + pricelow + attribute2high + attribute3high + attribute4high'.format(customer), data = df)
            res = mod.fit()
            results_summary = res.summary() # Regression results
            results_as_html = results_summary.tables[1].as_html() # Converting results summary into dataframe
            newdf = pd.read_html(results_as_html, header=0, index_col=0)[0] # Converting results summary into dataframe
            transposed = newdf.T # Transposing to new dataframe
            theresults = theresults.append(transposed.iloc[0]) # Appending transposed dataframe to theresults
        
        # Resetting index for nice formatting
        theresults = theresults.reset_index(drop=True)
        theresults.index = theresults.index + 1
        
        return theresults
