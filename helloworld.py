
import random
import datetime

def helloworld(name=None, howlong=None, countdown=None):
    """
    return hello world, or hello {name}
    """

    # print greeting
    if not name:
        print("hello world")
    else:
        print("hello {}".format(name))

    # print days til Dog is hungry
    if howlong:
        dday = datetime.datetime(2019, 2, 12)
        diff = dday - datetime.datetime.now()
        print("{} days until the dog needs a treat".format(diff.days))

    # print number of treats
    if countdown:
        end = random.randint(0, 1000)
        print("the dog will need {} treats".format(end))

   



