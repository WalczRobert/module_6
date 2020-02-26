"""
Robert Walczak
This program will calculate the area and the perimeter of a rectangle.
:param measurements [n,n] - this takes in the dimentions of each side
"""


def measurements(measurement_list):
    def area(area_list):
        if len(area_list) > 1:
            return area_list[0]*area_list[1]
        else:
            area_squared = area_list[0] * area_list[0]
            return area_squared

    def perimeter(perimeter_list):
        if len(perimeter_list) > 1:
            perimeter_result = perimeter_list[0] + perimeter_list[1]
            return perimeter_result * 2
        else:
            perimeter_squared = perimeter_list[0] * 4
            return perimeter_squared

    area = area(measurement_list)
    perimeter = perimeter(measurement_list)
    return "Perimeter = " + str(perimeter) + " Area = " + str(area)


if __name__ == '__main__':
    print(measurements([2, 4]))