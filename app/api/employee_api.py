# app/api/freee_api.py
import requests
import logging

# ログの設定
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FreeeAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.freee.co.jp/hr/api/v1"

    def get_employees(self, company_id, year, month, limit=50, with_no_payroll_calculation=True):
        url = f"{self.base_url}/employees"
        params = {
            "company_id": company_id,
            "year": year,
            "month": month,
            "limit": limit,
            "with_no_payroll_calculation": str(with_no_payroll_calculation).lower()
        }
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "FREEE-VERSION": "2022-02-01"
        }
        logging.info(f"Request URL: {url}")
        logging.info(f"Request Headers: {headers}")
        logging.info(f"Request Params: {params}")
        response = requests.get(url, headers=headers, params=params)
        logging.info(f"Response Status Code: {response.status_code}")
        logging.info(f"Response Text: {response.text}")
        if response.status_code == 200:
            return response.json()
        else:
            logging.error(f"Error: {response.status_code} - {response.text}")
            response.raise_for_status()

    def get_user_info(self):
        url = "https://api.freee.co.jp/api/1/users/me"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "FREEE-VERSION": "2022-02-01"
        }
        logging.info(f"Request URL: {url}")
        logging.info(f"Request Headers: {headers}")
        response = requests.get(url, headers=headers)
        logging.info(f"Response Status Code: {response.status_code}")
        logging.info(f"Response Text: {response.text}")
        if response.status_code == 200:
            return response.json()
        else:
            logging.error(f"Error: {response.status_code} - {response.text}")
            response.raise_for_status()