# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 10:29:50 2023

@author: ShendR
"""

# cFileName = "C:\\ShendR\\Python\\BES gui\\files\\BES_settings.cnf"

class PureConfigFileRead:
    def __init__(self, cFileName):
        print("Constructing pure config reader")
        self.fileName = cFileName

    def readUCharValue(self, error, stdValue, stdSub, stdSub2='', stdSub3=''):
        with open(self.fileName, 'r') as setup:
            result = 0

            keyWord = stdValue
            sub = stdSub
            sub2 = stdSub2
            sub3 = stdSub3

            found = -1
            found2 = -1
            found3 = -1
            found4 = -1

            error = 0

            if setup:
                if sub == "":
                    setup.seek(0)
                    for line in setup:
                        found = line.find(keyWord)
                        if found != -1:
                            list_values = line.split(' ')
                            value = list_values[0]
                            result = int(value)
                            return result
                        else:
                            pass
                    if found == -1:
                        error = 2
                else:
                    if sub2 == "":
                        setup.seek(0)
                        for line in setup:
                            found = line.find(keyWord)
                            if found != -1:
                                while True:
                                    line = next(setup)
                                    found3 = line.find(sub)
                                    if found3 != -1:
                                        list_values = line.split(' ')
                                        value = list_values[1]
                                        result = int(value)
                                        return result
                                if found3 == -1:
                                    error = 3
                        if found == -1:
                            error = 2
                    else:
                        if sub3 == "":
                            setup.seek(0)
                            for line in setup:
                                found = line.find(keyWord)
                                if found != -1:
                                    while True:
                                        line = next(setup)
                                        found3 = line.find(sub)
                                        if found3 != -1:
                                            while True:
                                                line = next(setup)
                                                found2 = line.find(sub2)
                                                if found2 != -1:
                                                    list_values = line.split(' ')
                                                    value = list_values[2]
                                                    result = int(value)
                                                    return result
                                            if found2 == -1:
                                                error = 4
                                    if found3 == -1:
                                        error = 3
                            if found == -1:
                                error = 2
                        else:
                            setup.seek(0)
                            for line in setup:
                                found = line.find(keyWord)
                                if found != -1:
                                    while True:
                                        line = next(setup)
                                        found3 = line.find(sub)
                                        if found3 != -1:
                                            while True:
                                                line = next(setup)
                                                found2 = line.find(sub2)
                                                if found2 != -1:
                                                    while True:
                                                        line = next(setup)
                                                        found4 = line.find(sub3)
                                                        if found4 != -1:
                                                            list_values = line.split(' ')
                                                            value = list_values[3]
                                                            result = int(value)
                                                            return result
                                                    if found4 == -1:
                                                        error = 5
                                            if found2 == -1:
                                                error = 4
                                    if found3 == -1:
                                        error = 3
                            if found == -1:
                                error = 2
            else:
                error = 1
        return result
    
    
    
    def readUShortValue(self, error, stdValue, stdSub, stdSub2='', stdSub3=''):
        with open(self.fileName, 'r') as setup:
            result = 0

            keyWord = stdValue
            sub = stdSub
            sub2 = stdSub2
            sub3 = stdSub3

            found = -1
            found2 = -1
            found3 = -1
            found4 = -1

            error = 0

            if setup:
                if sub == "":
                    setup.seek(0)

                    for line in setup:
                        found = line.find(keyWord)

                        if found != -1:
                            list_values = line.split(' ')
                            value = list_values[0]
                            result = int(value)
                            return result
                        else:
                            pass

                    if found == -1:
                        error = 2

                else:
                    if sub2 == "":
                        setup.seek(0)

                        for line in setup:
                            found = line.find(keyWord)

                            if found != -1:
                                while True:
                                    line = next(setup)
                                    found3 = line.find(sub)

                                    if found3 != -1:
                                        list_values = line.split(' ')
                                        value = list_values[1]
                                        result = int(value)
                                        return result

                                if found3 == -1:
                                    error = 3

                        if found == -1:
                            error = 2

                    else:
                        if sub3 == "":
                            setup.seek(0)

                            for line in setup:
                                found = line.find(keyWord)

                                if found != -1:
                                    while True:
                                        line = next(setup)
                                        found3 = line.find(sub)

                                        if found3 != -1:
                                            while True:
                                                line = next(setup)
                                                found2 = line.find(sub2)

                                                if found2 != -1:
                                                    list_values = line.split(' ')
                                                    value = list_values[2]
                                                    result = int(value)
                                                    return result

                                            if found2 == -1:
                                                error = 4

                                    if found3 == -1:
                                        error = 3

                            if found == -1:
                                error = 2

                        else:
                            setup.seek(0)

                            for line in setup:
                                found = line.find(keyWord)

                                if found != -1:
                                    while True:
                                        line = next(setup)
                                        found3 = line.find(sub)

                                        if found3 != -1:
                                            while True:
                                                line = next(setup)
                                                found2 = line.find(sub2)

                                                if found2 != -1:
                                                    while True:
                                                        line = next(setup)
                                                        found4 = line.find(sub3)

                                                        if found4 != -1:
                                                            list_values = line.split(' ')
                                                            value = list_values[3]
                                                            result = int(value)
                                                            return result

                                                    if found4 == -1:
                                                        error = 5

                                            if found2 == -1:
                                                error = 4

                                    if found3 == -1:
                                        error = 3

                            if found == -1:
                                error = 2

            else:
                error = 1

        return result



    def readUIntValue(self, error, stdValue, stdSub, stdSub2='', stdSub3=''):
        with open(self.fileName, 'r') as setup:
            result = 0

            keyWord = stdValue
            sub = stdSub
            sub2 = stdSub2
            sub3 = stdSub3

            found = -1
            found2 = -1
            found3 = -1
            found4 = -1

            error = 0

            if setup:
                if sub == "":
                    setup.seek(0)

                    for line in setup:
                        found = line.find(keyWord)

                        if found != -1:
                            list_values = line.split(' ')
                            value = list_values[0]
                            result = int(value)
                            return result
                        else:
                            pass

                    if found == -1:
                        error = 2

                else:
                    if sub2 == "":
                        setup.seek(0)

                        for line in setup:
                            found = line.find(keyWord)

                            if found != -1:
                                while True:
                                    line = next(setup)
                                    found3 = line.find(sub)

                                    if found3 != -1:
                                        list_values = line.split(' ')
                                        value = list_values[1]
                                        result = int(value)
                                        return result

                                if found3 == -1:
                                    error = 3

                        if found == -1:
                            error = 2

                    else:
                        if sub3 == "":
                            setup.seek(0)

                            for line in setup:
                                found = line.find(keyWord)

                                if found != -1:
                                    while True:
                                        line = next(setup)
                                        found3 = line.find(sub)

                                        if found3 != -1:
                                            while True:
                                                line = next(setup)
                                                found2 = line.find(sub2)

                                                if found2 != -1:
                                                    list_values = line.split(' ')
                                                    value = list_values[2]
                                                    result = int(value)
                                                    return result

                                            if found2 == -1:
                                                error = 4

                                    if found3 == -1:
                                        error = 3

                            if found == -1:
                                error = 2

                        else:
                            setup.seek(0)

                            for line in setup:
                                found = line.find(keyWord)

                                if found != -1:
                                    while True:
                                        line = next(setup)
                                        found3 = line.find(sub)

                                        if found3 != -1:
                                            while True:
                                                line = next(setup)
                                                found2 = line.find(sub2)

                                                if found2 != -1:
                                                    while True:
                                                        line = next(setup)
                                                        found4 = line.find(sub3)

                                                        if found4 != -1:
                                                            list_values = line.split(' ')
                                                            value = list_values[3]
                                                            result = int(value)
                                                            return result

                                                    if found4 == -1:
                                                        error = 5

                                            if found2 == -1:
                                                error = 4

                                    if found3 == -1:
                                        error = 3

                            if found == -1:
                                error = 2

            else:
                error = 1

        return result
    
    
    
    def readULongValue(self, error, stdValue, stdSub, stdSub2='', stdSub3=''):
        with open(self.fileName, 'r') as setup:
            result = 0

            keyWord = stdValue
            sub = stdSub
            sub2 = stdSub2
            sub3 = stdSub3

            found = -1
            found2 = -1
            found3 = -1
            found4 = -1

            error = 0

            if setup:
                if sub == "":
                    setup.seek(0)

                    for line in setup:
                        found = line.find(keyWord)

                        if found != -1:
                            list_values = line.split(' ')
                            value = list_values[0]
                            result = int(value)
                            return result
                        else:
                            pass

                    if found == -1:
                        error = 2

                else:
                    if sub2 == "":
                        setup.seek(0)

                        for line in setup:
                            found = line.find(keyWord)

                            if found != -1:
                                while True:
                                    line = next(setup)
                                    found3 = line.find(sub)

                                    if found3 != -1:
                                        list_values = line.split(' ')
                                        value = list_values[1]
                                        result = int(value)
                                        return result

                                if found3 == -1:
                                    error = 3

                        if found == -1:
                            error = 2

                    else:
                        if sub3 == "":
                            setup.seek(0)

                            for line in setup:
                                found = line.find(keyWord)

                                if found != -1:
                                    while True:
                                        line = next(setup)
                                        found3 = line.find(sub)

                                        if found3 != -1:
                                            while True:
                                                line = next(setup)
                                                found2 = line.find(sub2)

                                                if found2 != -1:
                                                    list_values = line.split(' ')
                                                    value = list_values[2]
                                                    result = int(value)
                                                    return result

                                            if found2 == -1:
                                                error = 4

                                    if found3 == -1:
                                        error = 3

                            if found == -1:
                                error = 2

                        else:
                            setup.seek(0)

                            for line in setup:
                                found = line.find(keyWord)

                                if found != -1:
                                    while True:
                                        line = next(setup)
                                        found3 = line.find(sub)

                                        if found3 != -1:
                                            while True:
                                                line = next(setup)
                                                found2 = line.find(sub2)

                                                if found2 != -1:
                                                    while True:
                                                        line = next(setup)
                                                        found4 = line.find(sub3)

                                                        if found4 != -1:
                                                            list_values = line.split(' ')
                                                            value = list_values[3]
                                                            result = int(value)
                                                            return result

                                                    if found4 == -1:
                                                        error = 5

                                            if found2 == -1:
                                                error = 4

                                    if found3 == -1:
                                        error = 3

                            if found == -1:
                                error = 2

            else:
                error = 1

        return result
    
    
    
    def readShortValue(self, error, stdValue, stdSub, stdSub2="", stdSub3=""):
        with open(self.fileName, 'r') as setup:
            result = 0
            keyWord = stdValue
            sub = stdSub
            sub2 = stdSub2
            sub3 = stdSub3
            found = -1
            found2 = -1
            found3 = -1
            found4 = -1

            error = 0

            lines = setup.readlines()

            if sub == "":
                for line in lines:
                    found = line.find(keyWord)

                    if found != -1:
                        list = line.split(' ')
                        value = list[0]
                        result = int(value)
                        return result
            else:
                if sub2 == "":
                    for line in lines:
                        found = line.find(keyWord)

                        if found != -1:
                            for line in lines:
                                found3 = line.find(sub)

                                if found3 != -1:
                                    list = line.split(' ')
                                    value = list[1]
                                    result = int(value)
                                    return result

                            if found3 == -1:
                                error = 3
                else:
                    if sub3 == "":
                        for line in lines:
                            found = line.find(keyWord)

                            if found != -1:
                                for line in lines:
                                    found3 = line.find(sub)

                                    if found3 != -1:
                                        for line in lines:
                                            found2 = line.find(sub2)

                                            if found2 != -1:
                                                list = line.split(' ')
                                                value = list[2]
                                                result = int(value)
                                                return result

                                        if found2 == -1:
                                            error = 4

                                if found3 == -1:
                                    error = 3
                    else:
                        for line in lines:
                            found = line.find(keyWord)

                            if found != -1:
                                for line in lines:
                                    found3 = line.find(sub)

                                    if found3 != -1:
                                        for line in lines:
                                            found2 = line.find(sub2)

                                            if found2 != -1:
                                                for line in lines:
                                                    found4 = line.find(sub3)

                                                    if found4 != -1:
                                                        list = line.split(' ')
                                                        value = list[3]
                                                        result = int(value)
                                                        return result

                                                if found4 == -1:
                                                    error = 5

                                        if found2 == -1:
                                            error = 4

                                if found3 == -1:
                                    error = 3

            error = 2

        return result
    
    
    
    def readIntValue(self, error, stdValue, stdSub, stdSub2="", stdSub3=""):
        with open(self.fileName, 'r') as setup:
            result = 0
            keyWord = stdValue
            sub = stdSub
            sub2 = stdSub2
            sub3 = stdSub3
            found = -1
            found2 = -1
            found3 = -1
            found4 = -1

            error = 0

            lines = setup.readlines()

            if sub == "":
                for line in lines:
                    found = line.find(keyWord)

                    if found != -1:
                        list = line.split(' ')
                        value = list[0]
                        result = int(value)
                        return result
            else:
                if sub2 == "":
                    for line in lines:
                        found = line.find(keyWord)

                        if found != -1:
                            for line in lines:
                                found3 = line.find(sub)

                                if found3 != -1:
                                    list = line.split(' ')
                                    value = list[1]
                                    result = int(value)
                                    return result

                            if found3 == -1:
                                error = 3
                else:
                    if sub3 == "":
                        for line in lines:
                            found = line.find(keyWord)

                            if found != -1:
                                for line in lines:
                                    found3 = line.find(sub)

                                    if found3 != -1:
                                        for line in lines:
                                            found2 = line.find(sub2)

                                            if found2 != -1:
                                                list = line.split(' ')
                                                value = list[2]
                                                result = int(value)
                                                return result

                                        if found2 == -1:
                                            error = 4

                                if found3 == -1:
                                    error = 3
                    else:
                        for line in lines:
                            found = line.find(keyWord)

                            if found != -1:
                                for line in lines:
                                    found3 = line.find(sub)

                                    if found3 != -1:
                                        for line in lines:
                                            found2 = line.find(sub2)

                                            if found2 != -1:
                                                for line in lines:
                                                    found4 = line.find(sub3)

                                                    if found4 != -1:
                                                        list = line.split(' ')
                                                        value = list[3]
                                                        result = int(value)
                                                        return result

                                                if found4 == -1:
                                                    error = 5

                                        if found2 == -1:
                                            error = 4

                                if found3 == -1:
                                    error = 3

            error = 2

        return result
    
    
    
    def readLongValue(self, error, stdValue, stdSub, stdSub2="", stdSub3=""):
        with open(self.fileName, 'r') as setup:
            result = 0
            keyWord = stdValue
            sub = stdSub
            sub2 = stdSub2
            sub3 = stdSub3
            found = -1
            found2 = -1
            found3 = -1
            found4 = -1

            error = 0

            lines = setup.readlines()

            if sub == "":
                for line in lines:
                    found = line.find(keyWord)

                    if found != -1:
                        list = line.split(' ')
                        value = list[0]
                        result = int(value)
                        return result
            else:
                if sub2 == "":
                    for line in lines:
                        found = line.find(keyWord)

                        if found != -1:
                            for line in lines:
                                found3 = line.find(sub)

                                if found3 != -1:
                                    list = line.split(' ')
                                    value = list[1]
                                    result = int(value)
                                    return result

                            if found3 == -1:
                                error = 3
                else:
                    if sub3 == "":
                        for line in lines:
                            found = line.find(keyWord)

                            if found != -1:
                                for line in lines:
                                    found3 = line.find(sub)

                                    if found3 != -1:
                                        for line in lines:
                                            found2 = line.find(sub2)

                                            if found2 != -1:
                                                list = line.split(' ')
                                                value = list[2]
                                                result = int(value)
                                                return result

                                        if found2 == -1:
                                            error = 4

                                if found3 == -1:
                                    error = 3
                    else:
                        for line in lines:
                            found = line.find(keyWord)

                            if found != -1:
                                for line in lines:
                                    found3 = line.find(sub)

                                    if found3 != -1:
                                        for line in lines:
                                            found2 = line.find(sub2)

                                            if found2 != -1:
                                                for line in lines:
                                                    found4 = line.find(sub3)

                                                    if found4 != -1:
                                                        list = line.split(' ')
                                                        value = list[3]
                                                        result = int(value)
                                                        return result

                                                if found4 == -1:
                                                    error = 5

                                        if found2 == -1:
                                            error = 4

                                if found3 == -1:
                                    error = 3

            error = 2

        return result
    
    
    
    def readDoubleValue(self, error, stdValue, stdSub, stdSub2="", stdSub3=""):
        with open(self.fileName, 'r') as setup:
            result = 0.0
            keyWord = stdValue
            sub = stdSub
            sub2 = stdSub2
            sub3 = stdSub3
            found = -1
            found2 = -1
            found3 = -1
            found4 = -1

            error = 0

            lines = setup.readlines()

            if sub == "":
                for line in lines:
                    found = line.find(keyWord)

                    if found != -1:
                        list = line.split(' ')
                        value = list[0]
                        result = float(value)
                        return result
            else:
                if sub2 == "":
                    for line in lines:
                        found = line.find(keyWord)

                        if found != -1:
                            for line in lines:
                                found3 = line.find(sub)

                                if found3 != -1:
                                    list = line.split(' ')
                                    value = list[1]
                                    result = float(value)
                                    return result

                            if found3 == -1:
                                error = 3
                else:
                    if sub3 == "":
                        for line in lines:
                            found = line.find(keyWord)

                            if found != -1:
                                for line in lines:
                                    found3 = line.find(sub)

                                    if found3 != -1:
                                        for line in lines:
                                            found2 = line.find(sub2)

                                            if found2 != -1:
                                                list = line.split(' ')
                                                value = list[2]
                                                result = float(value)
                                                return result

                                        if found2 == -1:
                                            error = 4

                                if found3 == -1:
                                    error = 3
                    else:
                        for line in lines:
                            found = line.find(keyWord)

                            if found != -1:
                                for line in lines:
                                    found3 = line.find(sub)

                                    if found3 != -1:
                                        for line in lines:
                                            found2 = line.find(sub2)

                                            if found2 != -1:
                                                for line in lines:
                                                    found4 = line.find(sub3)

                                                    if found4 != -1:
                                                        list = line.split(' ')
                                                        value = list[3]
                                                        result = float(value)
                                                        return result

                                                if found4 == -1:
                                                    error = 5

                                        if found2 == -1:
                                            error = 4

                                if found3 == -1:
                                    error = 3

            error = 2

        return result
    
    
    
    def readStringValue(self, error, stdValue, stdSub, stdSub2="", stdSub3=""):
        with open(self.fileName, 'r') as setup:
            result = ""
            keyWord = stdValue
            sub = stdSub
            sub2 = stdSub2
            sub3 = stdSub3
            found = -1
            found2 = -1
            found3 = -1
            found4 = -1

            error = 0

            lines = setup.readlines()

            if sub == "":
                for line in lines:
                    found = line.find(keyWord)

                    if found != -1:
                        list = line.split(' ')
                        value = list[0]
                        result = value
                        return result
            else:
                if sub2 == "":
                    for line in lines:
                        found = line.find(keyWord)

                        if found != -1:
                            for line in lines:
                                found3 = line.find(sub)

                                if found3 != -1:
                                    list = line.split(' ')
                                    value = list[1]
                                    result = value
                                    return result

                            if found3 == -1:
                                error = 3
                else:
                    if sub3 == "":
                        for line in lines:
                            found = line.find(keyWord)

                            if found != -1:
                                for line in lines:
                                    found3 = line.find(sub)

                                    if found3 != -1:
                                        for line in lines:
                                            found2 = line.find(sub2)

                                            if found2 != -1:
                                                list = line.split(' ')
                                                value = list[2]
                                                result = value
                                                return result

                                        if found2 == -1:
                                            error = 4

                                if found3 == -1:
                                    error = 3
                    else:
                        for line in lines:
                            found = line.find(keyWord)

                            if found != -1:
                                for line in lines:
                                    found3 = line.find(sub)

                                    if found3 != -1:
                                        for line in lines:
                                            found2 = line.find(sub2)

                                            if found2 != -1:
                                                for line in lines:
                                                    found4 = line.find(sub3)

                                                    if found4 != -1:
                                                        list = line.split(' ')
                                                        value = list[3]
                                                        result = value
                                                        return result

                                                if found4 == -1:
                                                    error = 5

                                        if found2 == -1:
                                            error = 4

                                if found3 == -1:
                                    error = 3

            error = 2

        return result
    
    
    
    