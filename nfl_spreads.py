from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError, URLError


def process_url(url):
    """Function that takes in a url and returns the data back to the caller.
    :param url: A string representation of a url that contains NFL Football Point Spread stats.
    :return: html: The html response after opening the url and reading the contents.
    """

    with urlopen(url) as response:
        html = response.read()
    return html


def scrape_url(response):
    """Function that takes in the data from a url and processes it with bs4.

    :param response: The html data from a url.
    :return: soup_rows: A list of the games for the week with point spread stats.
    """

    # create bs4 object and pass in the url response
    soup = BeautifulSoup(response, features='lxml')

    # search the soup for the current week table containing the spread data
    soup_table = soup.find('table', {'cols': '4'})

    # search the table for all of this weeks games, skipping the header <tr> tag
    soup_rows = soup_table.find_all('tr')[1:]

    return soup_rows


def display_scraped_data(scrapped_data):
    """Function that takes in the scrapped data and displays it formatted.

    :param scrapped_data: The bs4 data pulled from the url.
    :return:
    """

    # print statements to make data presentable

    print('\nNFL Point Spread - Games Left in Current Week')
    print('-' * 44)
    print('{:^15} | {:^12} | {:^12}'.format('Favorite', 'Underdog', 'Spread'))
    print('-' * 44)

    # default setup for displaying the player stats
    display = '{:^15} | {:^12} | {:^12}'

    # create list that will contain the text version of the rows
    row_list = []

    # loop through each row append the text to the list
    for game in scrapped_data:
        row_list.append(game.text.splitlines())

    # for each row in list, print the stats
    for row in row_list:
        print(display.format(row[2], row[4], row[3]))

    # print blank space for readability
    print('\n')

def main():
    """Function that manages the structure of this application."""

    # url to NFL Point Spread site
    url = 'http://www.footballlocks.com/nfl_point_spreads.shtml'

    # try exception to make sure that url is working
    try:
        # call function to process the url and save the response for later use
        url_response = process_url(url)

    except HTTPError as e:

        print('The server couldn\'t fulfill the request. Please check your url!')
        print('Error code: ', e.code)

    except URLError as e:

        print('We are unable to reach the server. Please check your url!')
        print('Reason: ', e.reason)

    else:
        # call function scrape the url response
        stats = scrape_url(url_response)

        # call function to display the scraped data
        display_scraped_data(stats)


if __name__ == '__main__':

    main()
