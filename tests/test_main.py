import pytest
from unittest.mock import patch
from data_scraper import scrape_competitor_data

@patch('data_scraper.requests.get')
def test_scrape_competitor_data(mock_get):
    # Mock the response from requests.get
    mock_get.return_value.status_code = 200
    mock_get.return_value.text = '<html><body><div class="content">Scraped Content Here</div></body></html>'

    url = "https://example.com/competitor"
    content = scrape_competitor_data(url)

    assert content == "Scraped Content Here"
    mock_get.assert_called_once_with(url)

@patch('data_scraper.requests.get')
def test_scrape_competitor_data_no_content(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.text = '<html><body></body></html>'

    url = "https://example.com/competitor"
    content = scrape_competitor_data(url)

    assert content == "No content found"
    mock_get.assert_called_once_with(url)
