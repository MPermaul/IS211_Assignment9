from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError, URLError


def process_url(url):
    """Function that takes in a url and returns the data
    :param url: A string representation of a url that contains NFL Football touchdown stats.
    :return: html: The html response after opening the url and reading the contents.
    """

    with urlopen(url) as response:
        html = response.read()
    return html


def scrape_url(response):
    """Function that takes in the data from a url and processes it.

    :param response: The html data from a url
    :return:
    """

    # create bs4 object and pass in the url response
    soup = BeautifulSoup(response, features='lxml')

    # search the soup for the specific data(in this case we have
    soup_table = soup.find('table', class_='data')
    soup_rows = soup_table.find_all(class_={'row1', 'row2'})

    return soup_rows


def display_scraped_data(scrapped_data):
    """Function that takes in the scrapped data and displays it formatted.

    :param scrapped_data: The bs4 data pulled from the url
    :return:
    """

    # print statements to make data presentable

    print('\n   NFL\'s TOP 20 Touchdown Scorers for 2019 Regular Season')
    print('-' * 60)
    print('{:^20} | {:^10} | {:^10} | {:^10}'.format('Player', 'Position', 'Team', 'Touchdowns'))
    print('-' * 60)

    # default setup for displaying the player stats
    display = '{:<20} | {:^10} | {:^10} | {:^10}'

    # counter to keep track of which number of player is being processed
    counter = 0

    # loop to make sure only top 20 are displayed
    while counter < 20:

        print(display.format(scrapped_data[counter].contents[0].text, scrapped_data[counter].contents[1].text,
                             scrapped_data[counter].contents[2].text, scrapped_data[counter].contents[6].text))

        # increase the counter after each loop
        counter += 1

    # print blank space for readability
    print('\n')

def main():
    """Function that manages the structure of this application."""

    # url to NFL touchdown stats
    url = 'https://www.cbssports.com/nfl/stats/playersort/nfl/year-2019-season-regular-category-touchdowns'

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
