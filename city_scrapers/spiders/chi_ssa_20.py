import re
from city_scrapers_core.constants import NOT_CLASSIFIED
from city_scrapers_core.items import Meeting
from city_scrapers_core.spiders import CityScrapersSpider
import w3lib.html as w3

class ChiSsa20Spider(CityScrapersSpider):
    name = "chi_ssa_20"
    agency = "Chicago Special Service Area #20 South Western Avenue"
    timezone = "America/Chicago"
    start_urls = ["https://www.mpbhba.org/business-resources/"]

    def parse(self, response):

        h2 = response.xpath(
             "//h2[contains(text(), 'SPECIAL SERVICE AREAS')]/following-sibling::*"
             ).getall()

        print('!!!!!!!!')

        for list_index, list_line in enumerate(h2):
            if 'ssa meetings' in list_line.lower():
                del h2[:list_index]

        for list_index, list_line in enumerate(h2):
            if 'ssa 64' in list_line.lower():
                del h2[list_index:]

        for entry in h2:
                    print(w3.remove_tags(entry))
                    entry = w3.remove_tags(entry)


                    meeting = Meeting(
#                    title=self._parse_title(entry),
#                    description=self._parse_description(entry),
#                    classification=self._parse_classification(entry),
                    start=self._parse_start(entry),
#                    end=self._parse_end(entry),
#                    all_day=self._parse_all_day(entry),
#                    time_notes=self._parse_time_notes(entry),
#                    location=self._parse_location(entry),
#                    links=self._parse_links(entry),
#                    source=self._parse_source(response),
                    )
#                    meeting["status"] = self._get_status(meeting)
#                    meeting["id"] = self._get_id(meeting)

#        yield meeting

    def _parse_title(self, item):
        """Parse or generate meeting title."""
        return ""

    def _parse_description(self, item):
        """Parse or generate meeting description."""
        return ""

    def _parse_classification(self, item):
        """Parse or generate classification from allowed options."""
        return NOT_CLASSIFIED

    def _parse_start(self, item, fuzzy=False):
        return None

    def _parse_end(self, item):
        """Parse end datetime as a naive datetime object. Added by pipeline if None"""
        return None

    def _parse_time_notes(self, item):
        """Parse any additional notes on the timing of the meeting"""
        return ""

    def _parse_all_day(self, item):
        """Parse or generate all-day status. Defaults to False."""
        return False

    def _parse_location(self, item):
        """Parse or generate location."""
        return {
            "address": "",
            "name": "",
        }

    def _parse_links(self, item):
        """Parse or generate links."""
        return [{"href": "", "title": ""}]

    def _parse_source(self, response):
        """Parse or generate source."""
        return response.url
