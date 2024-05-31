import scrapy
from scrapy.http import Request


class MpmaSpider(scrapy.Spider):
    name = "mpma"
    allowed_domains = ["www.mpmadirectory.org.my"]
    start_urls = ["https://www.mpmadirectory.org.my/all-members?limit=200"]

    def parse(self, response):
        # extract profile links
        profile_links = response.css("span.fc_item_title > a::attr(href)").getall()

        # loop through profile links, get full link url and save to text file
        for link in profile_links:
            user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0"
            full_link = f"https://www.mpmadirectory.org.my{link}"
            yield response.follow(full_link, self.parse_profile)

        # save full link urls to text file
        with open("../docs/links.txt", "a") as f:
            for link in profile_links:
                full_link = f"https://www.mpmadirectory.org.my/{link}"
                f.write(f"{full_link}\n")

        # get the url of each page
        next_page_text = [
            f"https://www.mpmadirectory.org.my/all-members?limit=200&start={num_start}"
            for num_start in range(200, 801, 200)
        ]

        # loop throught each page and scrape content
        for page in next_page_text:
            yield response.follow(page, self.parse)

    # Create method to scrape content/attributes for each profile
    def parse_profile(self, response):
        name = response.css(
            "div.flexi.bottomblock.infoblock.onecols ul.flexi li.flexi.lvbox.field_company.span12 div div.flexi.value.field_company::text"
        ).get()

        registration_number = response.css(
            "div.flexi.bottomblock.infoblock.onecols ul.flexi li.flexi.lvbox.field_business-registration.span12 div div.flexi.value.field_business-registration::text"
        ).get()

        year_incorporation = response.css(
            "div.flexi.bottomblock.infoblock.onecols ul.flexi li.flexi.lvbox.field_year-of-incorporation.span12 div div.flexi.value.field_year-of-incorporation::text"
        ).get()

        chief_exec = response.css(
            "div.flexi.bottomblock.infoblock.onecols ul.flexi li.flexi.lvbox.field_chief-executive.span12 div div.flexi.value.field_chief-executive::text"
        ).get()

        ceo_position = response.css(
            "div.flexi.bottomblock.infoblock.onecols ul.flexi li.flexi.lvbox.field_ceo-position.span12 div div.flexi.value.field_ceo-position::text"
        ).get()

        business_enquiry = response.css(
            "div.flexi.bottomblock.infoblock.onecols ul.flexi li.flexi.lvbox.field_business-enquiry.span12 div div.flexi.value.field_business-enquiry::text"
        ).get()

        business_contact_position = response.css(
            "div.flexi.bottomblock.infoblock.onecols ul.flexi li.flexi.lvbox.field_business-contact-person-position.span12 div div.flexi.value.field_business-contact-person-position::text"
        ).get()

        office_address = response.css(
            "div.flexi.bottomblock.infoblock.onecols ul.flexi li.flexi.lvbox.field_office-address.span12 div div.flexi.value.field_office-address::text"
        ).get()

        postcode = response.css(
            "div.flexi.bottomblock.infoblock.onecols ul.flexi li.flexi.lvbox.field_postcode.span12 div div.flexi.value.field_postcode::text"
        ).get()

        city_town = response.css(
            "div.flexi.bottomblock.infoblock.onecols ul.flexi li.flexi.lvbox.field_city-town.span12 div div.flexi.value.field_city-town::text"
        ).get()

        state = response.css(
            "div.flexi.bottomblock.infoblock.onecols ul.flexi li.flexi.lvbox.field_state-2.span12 div div.flexi.value.field_state-2::text"
        ).get()

        country = response.css(
            "div.flexi.bottomblock.infoblock.onecols ul.flexi li.flexi.lvbox.field_country.span12 div div.flexi.value.field_country::text"
        ).get()

        phone = response.css(
            "div.flexi.bottomblock.infoblock.onecols ul.flexi li.flexi.lvbox.field_telephone.span12 div div.flexi.value.field_telephone::text"
        ).get()

        fax = response.css(
            "div.flexi.bottomblock.infoblock.onecols ul.flexi li.flexi.lvbox.field_fax.span12 div div.flexi.value.field_fax::text"
        ).get()

        website = response.css(
            " div.flexi.bottomblock.infoblock.onecols ul.flexi li.flexi.lvbox.field_website.span12 div div.flexi.value.field_website a::text"
        ).get()

        raw_materials = response.css(
            "div.flexi.bottomblock.infoblock.onecols ul.flexi li.flexi.lvbox.field_raw-material-used.span12 div div.flexi.value.field_raw-material-used::text"
        ).get()

        production_process = response.css(
            "div.flexi.bottomblock.infoblock.onecols ul.flexi li.flexi.lvbox.field_production-processes.span12 div div.flexi.value.field_production-processes::text"
        ).get()

        products_manufactured = response.css(
            "div.flexi.bottomblock.infoblock.onecols ul.flexi li.flexi.lvbox.field_products-manufactured-business-line.span12 div div.flexi.value.field_products-manufactured-business-line::text"
        ).get()

        export_markets = response.css(
            "div.flexi.bottomblock.infoblock.onecols ul.flexi li.flexi.lvbox.field_current-export-markets.span12 div div.flexi.value.field_current-export-markets::text"
        ).get()

        yield {
            "Company": name,
            "Business Registration": registration_number,
            "Year of Incorporation": year_incorporation,
            "Chief Executive": chief_exec,
            "CEO Position": ceo_position,
            "Business Enquiry": business_enquiry,
            "Business Contact Person Position": business_contact_position,
            "Office Address": office_address,
            "Postcode": postcode,
            "City/Town": city_town,
            "State": state,
            "Country": country,
            "Telephone": phone,
            "Fax": fax,
            "Website": website,
            "Production Processes": production_process,
            "Products Manufactured/Business Line": products_manufactured,
            "Current Export Markets": export_markets,
        }
