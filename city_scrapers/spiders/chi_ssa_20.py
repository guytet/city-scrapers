import re
from datetime import datetime

from city_scrapers_core.constants import COMMISSION
from city_scrapers_core.items import Meeting
from city_scrapers_core.spiders import CityScrapersSpider

class ChiSsa20Spider(CityScrapersSpider):
    name = "chi_ssa_20"
    agency = "Chicago Special Service Area #20 South Western Avenue"
    timezone = "America/Chicago"
    #start_urls = ["https://www.mpbhba.org/business-resources/"]
    start_urls = ["http://localhost:8000"]
    location = {
        "name": "Beverly Bank & Trust",
        "address": "10258 S Western Ave, Chicago, IL 60643",
    }

    def parse(self, response):

        for item in response.xpath("//*[self::p or self::a[@href]]"):
        #for item in response.xpath("//*[self::p or self::a]"):
        #for item in response.xpath("//*[self::a[@href]]"):

            start = self._parse_start(item)
            if not start:
                continue

            meeting = Meeting(
              title="Commision",
              start=start,
              description=self._parse_description(item),
              classification=COMMISSION,
              end=None,
              all_day=False,
              time_notes=self._parse_time_notes(item),
              location=self.location,
              links=self._parse_links(item),
              source=response.url
            )

            meeting["status"] = self._get_status(meeting)
            meeting["id"] = self._get_id(meeting)

            yield meeting


    def _parse_start(self, item):
        #items_lists = item.css("*::text").getall()
        #items_lists = item.css("*::text")
        #items_str  = "".join(items_lists)
        #print(items_str, '\n')
        print(item, '\n')
  
#         if re.match('^\D*\d{4}\D*$', item):
#             year = re.match('^\d{4}', item)[0]

#         if not any(word in item for word in ['beverly', 'ssa']):
#
#             item = re.sub(r'([,\.])', '', item).strip()
#             ready_date = item + ' ' + str(self.year)
#             date_object=datetime.strptime(ready_date, "%A %B %d %I %p %Y")
#             return(date_object)


    def _parse_time_notes(self, item):
        """Parse any additional notes on the timing of the meeting"""
        return ""


    def _parse_location(self, item):
        """Parse or generate location."""
        return {
            "address": "",
            "name": "",
        }

    def _parse_links(self, item):
        """Parse or generate links."""
        return [{"href": "", "title": ""}]













#        for item in response.css("body p or body a"): 


#        if (self.location['name'].lower() + ' ' + 
#        self.location['address'].lower()) not in base:
#            print('address has changed')

#            if re.match(r'^\s*$', item):
#                continue

#        for index, line in enumerate(response):
#            if 'ssa meetings' in line:
#                del base[:index]
#
#        for index, line in enumerate(base):
#            if 'ssa 64' in line:
#                del base[index:]

#        base = [ re.sub(r"\s+", " ", item).lower() for item in base ]

#        base = response.xpath(
#               "//*[self::p or self::strong or self::h3]/text()").getall()
