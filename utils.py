from sklearn.base import BaseEstimator, TransformerMixin


# Creating custom transformer for accessing genotype information
class GenotypeTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, al_col2, al_col3, al_col17):
        self.al_col2 = al_col2
        self.al_col3 = al_col3
        self.al_col17 = al_col17


    def fit(self, X, y=None):
        return self

    def get_genotype(self,X):
            allele_2 = X[self.al_col2]
            allele_3 = X[self.al_col3]
            allele_17 = X[self.al_col17]

            if allele_17 == "TT":
                return "*17/*17"
            elif allele_2 == "AA":
                return "*2/*2"
            elif allele_3 == "AA":
                return "*3/*3"

            # STAR 2
            if allele_2 == "AG":
                if allele_17 == "TC":
                    return "*2/*17"
                elif allele_3 == "AG":
                    return "*2/*3"
                else:
                    return "*1/*2"  # Default case for allele_2 == "AG"

            # STAR 3
            if allele_3 == "AG":
                if allele_17 == "TC":
                    return "*3/*17"
                else:
                    return "*1/*3"  # Default case for allele_3 == "AG"

            # 1/17
            if allele_17 == "TC" and allele_2 == "GG" and allele_3 == "GG":
                return "*1/*17"

            # Default
            return "*1/*1"

    def transform(self, X, y=None):
          X_ = X.copy()
          X_["genotype"] = X_.apply(self.get_genotype, axis=1)
          X_.drop(columns= [self.al_col2, self.al_col3, self.al_col17], inplace =True)
          return X_


