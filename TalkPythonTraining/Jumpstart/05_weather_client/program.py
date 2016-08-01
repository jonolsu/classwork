import requests
import bs4
import collections

WeatherReport = collections.namedtuple('WeatherReport',
                                       'cond, temp, scale, loc')


def main():
    print_the_header()

    code = input('What zipcode do you want the weather for (97201)? ')
    html = get_html_from_web(code)
    report = get_weather_from_html(html)
    print('The temperature in {} is {} {} and conditions are {}'.format(report.loc, report.temp, report.scale, report.cond))


def print_the_header():
    print('-------------------------------------')
    print('       Weather App')
    print('-------------------------------------')
    print()


def get_html_from_web(zipcode):
    url = 'http://www.wunderground.com/weather-forecast/{}'.format(zipcode)
    response = requests.get(url)
    return(response.text)


def get_weather_from_html(html):
    # cityCss = 'div#location h1'
    # weatherConditionCss = 'div#curCond span.wx-value'
    # weatherTempCss = 'div#curTemp span.wx-data span.wx-value'
    # weatherScaleCss = 'div#curTemp span.wx-data span.wx-unit'

    soup = bs4.BeautifulSoup(html, "html.parser")
    loc = soup.find(id='location').find('h1').get_text()
    condition = soup.find(id='curCond').find(class_='wx-value').get_text()
    temp = soup.find(id='curTemp').find(class_='wx-value').get_text()
    scale = soup.find(id='curTemp').find(class_='wx-unit').get_text()

    loc = cleanup_text(loc)
    loc = find_city_and_state_from_location(loc)
    condition = cleanup_text(condition)
    temp = cleanup_text(temp)
    scale = cleanup_text(scale)

    report = WeatherReport(cond=condition, temp=temp, scale=scale, loc=loc)
    return(report)

def cleanup_text(text):
    if not text:
        return text
    text = text.strip()
    return(text)


def find_city_and_state_from_location(loc):
    parts = loc.split('\n')
    return parts[0].strip()


if __name__ == '__main__':
    main()

