
class LinkExtractorBase(object):
    def add_extracted_url(self, response, url):
        if not hasattr(response, 'spiro_extracted_urls'):
            response.spiro_extracted_urls = []
        response.spiro_extracted_urls.append(url)
