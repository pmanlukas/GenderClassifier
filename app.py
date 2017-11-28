from sklearn import tree

classifierDT = tree.DecisionTreeClassifier()

#TODO: replace X and Y with a bigger data set

X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]



Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']

classifierDT = classifierDT.fit(X,Y)

def prediction(height, weight, shoesize, clf):
    #TODO: ask User for prediction value
    prediction = clf.predict([[height,weight, shoesize]])

    print(prediction)


height = int(input("Enter height: "))
weight = int(input("Enter weight: "))
shoesize = int(input("Enter shoe size: "))

prediction(height, weight, shoesize, classifierDT)
