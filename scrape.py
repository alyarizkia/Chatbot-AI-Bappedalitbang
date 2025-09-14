from selenium import webdriver
from bs4 import BeautifulSoup
import time
import json

pages = {
    "beranda": "https://bappedalitbang.surabaya.go.id/",
    "faq": "https://bappedalitbang.surabaya.go.id/",
    "sekilas": "https://bappedalitbang.surabaya.go.id/sekilas",
    "visi_misi": "https://bappedalitbang.surabaya.go.id/visi-dan-misi",
    "berita_pdrb": "https://bappedalitbang.surabaya.go.id/berita/2025-03-07/pdrb-surabaya-2024-potret-pergerakan-ekonomi-surabaya",
    "berita_medical": "https://bappedalitbang.surabaya.go.id/berita/2024-12-24/surabaya-menuju-destinasi-medical-tourism-terbaik"

}

driver = webdriver.Chrome()

data = {}

for section, url in pages.items():
    driver.get(url)
    time.sleep(10)  
    soup = BeautifulSoup(driver.page_source, "html.parser")

    if section == "beranda":
        blocks = soup.find_all("section", class_="bg-gray-900 dark:bg-white")
        data[section] = [b.get_text(" ", strip=True) for b in blocks]

    elif section == "faq":
        blocks = soup.find_all("section", class_="bg-white py-16")
        data[section] = [b.get_text(" ", strip=True) for b in blocks]

    elif section == "sekilas":
        blocks = soup.find_all("section")
        data[section] = [b.get_text(" ", strip=True) for b in blocks]

    elif section == "visi_misi":
        blocks = soup.find_all("div", class_="grid max-w-screen-xl px-4 py-8 mx-auto lg:gap-8 xl:gap-0 lg:py-16")
        data[section] = [b.get_text(" ", strip=True) for b in blocks]

    elif section == "berita_pdrb":
        articles = soup.find_all("div", class_="grid max-w-screen-xl px-4 py-8 mx-auto lg:gap-8 xl:gap-0 lg:py-16")
        data[section] = [a.get_text(" ", strip=True) for a in articles]

    elif section == "berita_medical":
        articles = soup.find_all("div", class_="grid max-w-screen-xl px-4 py-8 mx-auto lg:gap-8 xl:gap-0 lg:py-16")
        data[section] = [a.get_text(" ", strip=True) for a in articles]


driver.quit()

# Simpan hasil scrape ke JSON
with open("scraped_bappedalitbang.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("✅ Data berhasil disimpan ke scraped_bappedalitbang.json")