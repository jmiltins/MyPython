import os 
import csv
#python3 -m pip install Pillow
#python3 -m pip install SimpleImage

#from simpleimage import SimpleImage
import simpleimage
# Final visualization Dimensions

VISUALIZATION_WIDTH = 1512
VISUALIZATION_HEIGHT = 698

MIN_LONGITUDE =  -178 # as bigger, as compressed 180(def, too narrow), 170(too wide), 175(too wide), 172 (too wide), 178 too narrow), 177 (too wide)
MAX_LONGITUDE = 178
MIN_LATITUDE = -82 # as bigger, as compressed 90(def, too narrow),80(too wide), 83, lit to narr, 81 lit to wide
MAX_LATITUDE = 82

OFFSET = 50

YELLOW = [255, 204, 0]
WHITE = [255, 255, 255]
BLACK = [0, 0, 0, ]
RED = [255, 0, 0]
DARK_RED = [128, 0, 0]
DARK_ORANGE = [153, 51, 0]

BACKGROUND_COLOR = BLACK
MOST_PLACES_COLOR = DARK_ORANGE
ALL_COUNTRIES_COLOR = YELLOW
COUNTRY_FROM_COLOR = WHITE
COUNTRY_TO_COLOR = RED

COUNTRY_DIRECTORY = "/home/Bring_light_force/countries/"

def average_pixel_country(country_filename):
    """
    Calculates the average pixel of all cities of the country, returns x and y of a country pixel
    """
    lat_list = []
    lon_list = []
    with open(country_filename) as cities_file:
        next(cities_file) # skip the header line
        reader = csv.reader(cities_file)

        for line in reader:
            lat_list.append(float(line[1]))
            lon_list.append(float(line[2]))

    lat = int(latitude_to_y(average(lat_list)))
    lon = int(longitude_to_x(average(lon_list)))
    
    return lat, lon


def plot_country(visualization, filename, color, offset_x, offset_y,p_size):
    """
    Responsible for reading in geographic data from a file 
    about the cities in a particular country and plotting them 
    in the visualization. 

    Parameters:
        - `visualization` is the SimpleImage that will eventually be 
          shown to the user
        - `filename` is the file we want to read through
    """
    with open(filename) as cities_file:
        next(cities_file) # skip the header line
        reader = csv.reader(cities_file)
        for line in reader:
            lat = float(line[1])
            lon = float(line[2])
            
            plot_one_city(visualization, lat, lon, color, offset_x, offset_y,p_size)


def is_WHITE(pixel):
    """
    This function checks pixel for being white
    returns True or False.
    """
    average = (pixel.red + pixel.green + pixel.blue) / 3
    white_average = (WHITE[0] + WHITE[1] + WHITE[2]) / 3

    if average < white_average:
        return True
    else:
        return False 

def paint_pixel(pixel, color):
    """
    This function Paints  pixel in color, passed to this ftion, returns pixel
    """
    pixel.red = color[0] 
    pixel.green = color[1] 
    pixel.blue = color[2] 
    return pixel

def paint_all_pixels(image, color):
    """
    This function Paints all pixels in color, passed to this ftion, returns pixel
    """
    for pixel in image:
        pixel.red = color[0] 
        pixel.green = color[1] 
        pixel.blue = color[2] 

def copy_image(image_from, image_to):
    """
    This function copys image to another image
    """
    for pixel in image_from:
        x = pixel.x
        y = pixel.y
        image_to.set_pixel(x , y ,pixel)
    

def copy_notwhite_pixels(image_from, image_to, color, offset_x = 0, offset_y = 0):
    """
    This function checks all pixel colors in image to be less than white pixel
    and if so, copys to another picture
    """
    for pixel in image_from:
        average = (pixel.red + pixel.green + pixel.blue) // 3
        # See if this pixel is not white red
        if is_WHITE(pixel):
            pixel = paint_pixel(pixel, color)
            x = pixel.x
            y = pixel.y
            image_to.set_pixel(x + OFFSET + offset_x, y + OFFSET + offset_y ,pixel) # plus passed ofset and GLOBAL
    
    
    """for y in range(image_from.height):
        for x in range (image_from.width):
            pixel = image.get_pixel(x, y)
            if 
            image_to.set_pixel(x, y, pixel)"""
            
def main():
    #import image all places
    # Show Original

    all_places = SimpleImage('/home/Bring_light_force/image_with_all_populated_places.png') # green
    #all_places.show()
    #print(all_places.width, all_places.height)

    #import image most cities
    most_places = SimpleImage('/home/Bring_light_force/image_with_most_populated_places.png') #blue
    #most_places.show()
    #print(most_places.width, most_places.height)

    # create new empty image
    
    final_map = SimpleImage.blank(VISUALIZATION_WIDTH + OFFSET * 2, VISUALIZATION_HEIGHT + OFFSET * 2)

    #paint final image background color
    paint_all_pixels(final_map, BACKGROUND_COLOR)
    
    # Add layer all_places, color
    copy_notwhite_pixels(all_places, final_map, DARK_RED)
    final_map.show()
    
    # Add layer most_places, color
    copy_notwhite_pixels(most_places, final_map, MOST_PLACES_COLOR, 8, 13) # Offset must be adjusted manualy, since picture sizes dont mach _8_13_BEST
    # Add layer most_places, color
    final_map.show()
    countries = get_countries()

    # iterate through each of the countries and plot it
    for country in countries:
        country_filename = COUNTRY_DIRECTORY + country + ".csv"
        plot_country(final_map, country_filename, ALL_COUNTRIES_COLOR, -43, 44, 1) # Adjust offset manualy to mach the images
    
    final_map.show()
    # askwould you like to bring_ligth_force

    # ask for your_country
    country_from = get_country_from()
        # Add layer your_country, color
        # iterate through each of the countries and plot it
    for country in country_from:
        country_from_filename = COUNTRY_DIRECTORY + country + ".csv"
        plot_country(final_map, country_from_filename, COUNTRY_FROM_COLOR, -43, 44, 3) #

    # calculate average lat and lon of all cities in country
    avg_y_from, avg_x_from = average_pixel_country(country_filename) # returns average
    
    # plot average pixel as a city
    #draw_square(final_map, avg_x_from, avg_y_from, WHITE, -43, 44, 3) #plot_pixel(visualization, x , y)
    # ask for the name
    final_map.show()
    # ask where to bring light
    country_to = get_country_to()
        # Add layer choice_country, color
        # iterate through each of the countries and plot it
    for country in country_to:
        country_to_filename = COUNTRY_DIRECTORY + country + ".csv"
        plot_country(final_map, country_to_filename, COUNTRY_TO_COLOR, -43, 44, 3) #

    # calculate average lat and lon of all cities in country
    avg_y_to, avg_x_to = average_pixel_country(country_to_filename) # returns average
    
    # plot average pixel as a city
    draw_square(final_map, avg_x_to, avg_y_to, WHITE, -43, 44, 3) #plot_pixel(visualization, x , y)
    
    final_map.show()
    #copy final_map
    final_map_no_beams = SimpleImage.blank(VISUALIZATION_WIDTH + OFFSET * 2, VISUALIZATION_HEIGHT + OFFSET * 2)
    copy_image(final_map, final_map_no_beams)

    # Send light
    line_xy_from_to(final_map, country_from_filename, avg_x_to, avg_y_to, WHITE, -43, 44)
    
    # Show light image
    final_map.show()
    # Light up the country_to
    for country in country_to:
        country_to_filename = COUNTRY_DIRECTORY + country + ".csv"
        plot_country(final_map, country_to_filename, WHITE, -43, 44, 3) #

    #display Final image with light on
    final_map.show()
    
    # Light on image with no beams
    for country in country_to:
        country_to_filename = COUNTRY_DIRECTORY + country + ".csv"
        plot_country(final_map_no_beams, country_to_filename, WHITE, -43, 44, 3) #
    
    # Show image with no beams
    final_map_no_beams.show()

    # print thanks for bringing light to country_to_support
    
    #Add input info to csv file date,name,from, where,why

    # create gif

def cerate_zoom_in_map(visualization, avg_y_from, avg_x_from ,avg_y_to, avg_x_to):
    
    zoom_map = SimpleImage.blank(VISUALIZATION_WIDTH + OFFSET * 2, VISUALIZATION_HEIGHT + OFFSET * 2)
    copy_image(final_map, final_map_no_beams)




def line_xy_from_to(visualization, filename, x, y, color, offset_x, offset_y):
    """Takes country file and destination x, y.
    converts country's citys lat, lon to x any y
    passes to a draw line function

    """
    with open(filename) as cities_file:
        next(cities_file) # skip the header line
        reader = csv.reader(cities_file)
        for line in reader:
            lat = float(line[1])
            lon = float(line[2])

            lat = int(latitude_to_y(lat))
            lon = int(longitude_to_x(lon))
            if 0 < x < visualization.width and 0 < y < visualization.height:
                #print(lon, lat, x, y) # test
                draw_line(visualization, lon, lat, x, y, color, offset_x, offset_y) #draw_line(final_map, from_x, from_y, to_x, to_y, WHITE, offset_x, offset_y):

def draw_line(visualization, from_x, from_y, to_x, to_y, color, offset_x, offset_y):
    #plot_pixel(visualization, from_x, from_y, WHITE, offset_x, offset_y)
    while (not(int(from_x) == int(to_x))) and (not(int(from_y) == int(to_y))):
        #print('went in', from_x, to_x, from_y, to_y)#test line
        #draw_square(visualization, from_x, from_y, WHITE, offset_x, offset_y,3)
        if 0 < from_x < visualization.width and 0 < from_y < visualization.height:
            plot_pixel(visualization, from_x, from_y, color, offset_x, offset_y)
            #draw_square(visualization, from_x, from_y, color, offset_x, offset_y,3)
            
        x_step = abs(to_x - from_x)/abs(to_y - from_y)
        y_step = abs(to_y - from_y)/abs(to_x - from_x)
        
        
        if from_x > to_x :
            from_x = (from_x - x_step)
        elif from_x < to_x: 
            from_x = (from_x + x_step)
        if from_y > to_y :
            from_y = (from_y - y_step)
        elif from_y < to_y: 
            from_y = (from_y + y_step)
        #print(from_x, from_y)

def draw_square(visualization, coo_x, coo_y, WHITE, offset_x, offset_y, size):
    coo_x -= size/2
    coo_y -= size/2
    
    for y in range (size):
        for x in range (size):
            plot_pixel(visualization, x + coo_x, y + coo_y, WHITE, offset_x, offset_y)
    
def get_country_to():
    """
    Gets the list of countries from the user, but doesn't check that 
    the user types in valid country names. 

    Returns a list of country names
    """
    country_to = []
    all_countries = [s.split(".")[0] for s in os.listdir(COUNTRY_DIRECTORY)]
    
    country = 'Belarus'#input("Enter a country, you would like to send LIGHT FORCE to! ")
    if country == "":
        return all_countries
    country_to.append(country.strip())
    return country_to

def get_country_from():
    """
    Gets the list of countries from the user, but doesn't check that 
    the user types in valid country names. 

    Returns a list of country names
    """
    country_from = []
    all_countries = [s.split(".")[0] for s in os.listdir(COUNTRY_DIRECTORY)]
    
    country = 'Latvia'#'Togo'#input("Enter a country, you would like to send LIGHT FORCE from! ")
    if country == "":
        return all_countries
    country_from.append(country.strip())
    return country_from
    
def get_countries():    
    """
    Gets the list of countries Returns a list of country names
    """
    return [s.split(".")[0] for s in os.listdir(COUNTRY_DIRECTORY)]

def plot_one_city(visualization, latitude, longitude, color, offset_x, offset_y,p_size):
    """
    Given the visualization image as well as a single city's latitude and longitude,
    plot the city on the image

    """

    # convert the Earth coordinates to pixel coordinates
    x = longitude_to_x(longitude)
    y = latitude_to_y(latitude)

    # if the pixel is in bounds of the window we specified through constants,
    # plot it
    if 0 < x < visualization.width and 0 < y < visualization.height:
        #plot_pixel(visualization, x , y, color, offset_x, offset_y)
        draw_square(visualization, x, y, color, offset_x, offset_y,p_size)


def plot_pixel(visualization, x, y, color, offset_x, offset_y): #GOOD
    """
    Set a pixel at a particular coordinate. 

    """
    if 0 < x < visualization.width and 0 < y < visualization.height:
        pixel = visualization.get_pixel(x + OFFSET + offset_x, y + OFFSET + offset_y) # Glogal ofset + manual setup
        pixel.red = color[0]
        pixel.green = color[1] 
        pixel.blue = color[2]

def longitude_to_x(longitude): #GOOD
    """
    Scales a longitude coordinate to a coordinate in the visualization email
    """
    return VISUALIZATION_WIDTH * (longitude - MIN_LONGITUDE) / (MAX_LONGITUDE - MIN_LONGITUDE)

def latitude_to_y(latitude): #GOOD
    """
    Scales a latitude coordinate to a coordinate in the visualization email
    """
    return VISUALIZATION_HEIGHT * (1.0 - (latitude - MIN_LATITUDE) / (MAX_LATITUDE - MIN_LATITUDE))

def average(lst): #GOOD
    """ python -m doctest bring.py
    average(lst)
    >>> average([4,2,3,4,5,6])
    4.0
    
    """
    avg = (sum(lst) / len(lst))
    return avg

# if __name__ ==  "__main__":
#     main()
