from bs4 import BeautifulSoup 
from dotenv import load_dotenv 
import os 
from models.product import read_products_from_csv
from services.email_service import send_email, get_html_template
from services.scrap_hp import scrape_hp_site

# Load environment variables from .env file
load_dotenv()

# Example usage
if __name__ == "__main__":
    data_path = os.environ.get('DATA_PATH')
    api_key = os.environ.get('API_KEY')
    scraper_api = os.environ.get('SCRAPER_API_URL')
    products = read_products_from_csv(data_path)
    table_rows: str = ""
    for product in products:
        price = scrape_hp_site(scraper_api, api_key, product.url, 'true', 'true', 'true', 'true', product.selector)
        # print(f'Product: {product.name} - Target Price: {product.price} - Current Price: {price}')
        if price and float(price) < product.price:
            # print(f"Sending email to {os.getenv('RECIPIENT_EMAILS')}")
            table_rows += f"<tr><td><b>{product.name}</b></td><td>${price}</td><td>${product.price}</td><td><a href='{product.url}'>Link</a></td></tr>"
            
    if table_rows:
        email_body = get_html_template(table_rows)
        # print(email_body)
        send_email('Price Drop Alert', email_body, os.getenv('RECIPIENT_EMAILS'))
