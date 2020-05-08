from sklearn.decomposition import PCA

def dim_reduction(dtm):
    explained var = []
    for components in range (1, 100, 5):
        pca = PCA(n_components=components)
        pca.fit(dtm.toarray())
        
