# Rock_Cleaner
# This function cleans and transforms the data from the Mohs Dataset 

def rock_cleaner(df): 
    df = df.loc[(df.atomicweight_Average > 1.0)] # Removes all atomic weights that cannot possibly exist
    df = df.loc[(df.allelectrons_Total > 1.0) & (df.allelectrons_Total < 725)] # Removes both non-existent values from the low end, and the upper 1% of data that may be outliers
    df = df.loc[(df.density_Total > 0.1) & (df.density_Total < 200)] # Removes those values with spurious and low densities, including 0, and removes the few with excessively high density, likely outliers
    df['atomicnumber_Average'] = df.atomicweight_Average * df.zaratio_Average # Adds a column for the atomic number, calculated from the Z/A ratio and atomic weight
    df[['allelectrons_Total_T', 'allelectrons_Average_T', 'atomicweight_Average_T', 'atomicnumber_Average_T', 'density_Total_T']] = df[['allelectrons_Total', 'allelectrons_Average', 'atomicweight_Average', 'atomicnumber_Average', 'density_Total']].apply(lambda x: x**(1/3))
        # This transforms the data that are cubically correlated with the radii, applying a cubed root, which also brings the distributions to a more normal appearance
    df.drop(['density_Average','allelectrons_Total', 'allelectrons_Average', 'atomicweight_Average', 'density_Total', 'atomicnumber_Average'], axis=1, inplace=True) 
        # This drops the linear columns from the transformed data as well as the Density_Average, which contained 40 or so columns of all zeros when all other data were present
    return df