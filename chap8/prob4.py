print("Pickling lists.")
print("Unpickling lists.")
import _compat_pickle
variety = ["sweet", "hot", "dill"]
pickle_file = open("pickles1.dat", "w")
_compat_pickle.dump(variety, pickle_file)

pickle_file = open("pickles1.dat", "r")
variety = cPickle.load(pickle_file)
print(variety)
import shelve
pickles = shelve.open("pickles2.dat")
pickles["variety"] = ["sweet", "hot", "dill"]
pickles.sync()
for key in pickles.keys()
    print(key, "-", pickles[key])
1/0
