from googlesearch import search

def get_competitor_urls(competitor_name: str, num_results: int = 1):
    """
    Get URLs to scrape data for the specified competitor using predefined URLs.

    Args:
        competitor_name (str): Name of the competitor.
        num_results (int): Number of search results to return.

    Returns:
        list: List of URLs found for the competitor.
    """
    urls_dict = {
        "Reliance Digital": [
            "https://www.ril.com/ar2022-23/pdf/RIL-Integrated-Annual-Report-2022-23.pdf"
        ],
        "Bajaj": [
            "https://iide.co/case-studies/marketing-strategy-of-bajaj-electricals/",
            "https://www.livemint.com/companies/bajaj-electricals-to-firm-up-new-offerings-over-2-3-years-11712666278760.html",
            "https://www.icicidirect.com/research/equity/bajaj-electricals-ltd/6004",
            "https://www.bajajelectricals.com/media/7856/bajaj-electricals-limited-annual-report-for-fy-2023-24.pdf",
        ],
        "Adithya Vision": [
            "https://www.equitymaster.com/research-it/annual-results-analysis/AVL/ADITYA-VISION-2022-23-Annual-Report-Analysis/7071",
            "https://trendlyne.com/research-reports/stock/52912/AVL/aditya-vision-ltd/",
            "https://adityavision.in/media/attachments/2024/07/10/cc-_annual-report-aditya-vision-fy-2023-24_spread-sheet.pdf",
            "https://www.dsij.in/productattachment/BrokerRecommendation/Aditya%20Vision%20-%2011%20-%2012%20-%202023%20-%20emkay111223.pdf",
        ],
        "Poojara": [
            "https://www.infomerics.com/admin/uploads/pr-poojara-telecom-7jul23.pdf",
        ],
        "Vijay Sales": [
            "https://nielseniq.com/global/en/insights/success-story/2023/vijay-sales-planning-aggressive-and-defensive-sales-strategies/",
            "https://www.careratings.com/upload/CompanyFiles/PR/202401120134_Vijay_Sales_(India)_Private_Limited.pdf",
            "https://www.vijaysales.com/about-us",
        ]
    }

    # Get the URLs for the specified competitor, defaulting to an empty list if not found
    urls = urls_dict.get(competitor_name, [])
    # urls = ["https://iide.co/case-studies/marketing-strategy-of-bajaj-electricals/"]
    # Limit the number of results if necessary
    return urls  # Return the specified number of results

def main():
    competitor_name = input("Enter the name of the competitor: ")
    urls = get_competitor_urls(competitor_name)
    
    if urls:
        print(f"Found URLs for {competitor_name}:")
        for url in urls:
            print(url)
    else:
        print(f"No URLs found for {competitor_name}.")

if __name__ == "__main__":
    main()
