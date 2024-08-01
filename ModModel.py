import mysql.connector


def getinfo(min_lat, max_lat, min_lon, max_lon):
    cnx = mysql.connector.connect(user='', password='',
                                  host='127.0.0.1',
                                  database='flights')

    print('getinfo start')
    cursor = cnx.cursor()

    query = ("SELECT city, country, latitude, longitude FROM airports "
             "WHERE latitude BETWEEN %s AND %s AND longitude BETWEEN %s AND %s")

    cursor.execute(query, (float(min_lat), float(max_lat), float(min_lon), float(max_lon)))

    lst = []
    for (city, country, latitude, longitude) in cursor:
        lst.append((city, country, latitude, longitude))
        
    cursor.close()
    cnx.close()
    return lst
def getroutes(first_city, second_city):
    print('getroutes start')
    try:
        cnx = mysql.connector.connect(user='' password='',
                                      host='127.0.0.1',
                                      database='flights')


        cursor = cnx.cursor()

        query = ("SELECT src.city, dst.city, airplane, airline FROM routes JOIN airports src ON routes.src_airport_id = "
                 "src.id JOIN airports dst ON routes.dst_airport_id = dst.id WHERE src.city = %s AND dst.city = %s")

        cursor.execute(query, (first_city, second_city))

        lst = []
        for (city1, city2, airplane, airline) in cursor:
            lst.append((city1, city2, airplane, airline))

        cursor.close()
        cnx.close()
        print('getroutes finish')
        return lst
    except TypeError as e:
        print("Something went wrong: {}".format(e))
    except ValueError as e:
        print("Something went wrong: {}".format(e))
    except mysql.connector.Error as e:
        print("Something went wrong: {}".format(e))


# cnx = mysql.connector.connect(user='', password='',
#                               host='127.0.0.1',
#                               database='flights')
#
# cnx.close()
