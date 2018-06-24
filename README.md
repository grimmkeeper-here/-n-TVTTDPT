# Đồ Án Môn Truy Vấn Thông Tin Đa Phương Tiện
Đề tài: Khuyến nghị sách cho người dùng dựa vào dòng cảm nghĩ người dùng nhập vào trước đó.

# Ngôn ngữ lập trình
    1. Python 2.7
    2. Html + Css

# Thư viện sử dụng
    1. Scrapy
    2. Scikit Learn(SKlearn)
    3. Pandas

# Cài đặt
    A. Cài đặt python: https://www.python.org/
    B. Cài đặt Anaconda để có mọi thư viện cần thiết
    C. Thông qua pip
        1. Cài đặt Scrapy: pip install scrapy (https://scrapy.org/)
        2. Cài đặt Scrapy Proxies: pip install scrapy_proxies (https://github.com/aivarsk/scrapy-proxies)
        3. Cài đặt Scikit Learn: pip install -U scikit-learn (http://scikit-learn.org/stable/index.html)
        4. Cài đặt Pandas: pip install pandas (https://pandas.pydata.org/)

# Khởi động
    Mọi chức năng cần thiết đều có trong file "start.bat"
        1. Start Crawler _ crawl các sách thể loại văn học, kinh tế, phát triển bản thân đang bán trên vinabook.com
        2. Create Source _ tạo ra các file khởi tạo trong thư mục source
        3. Start Server _ khởi động server để các API hoạt động
        4. Enter Site _ truy cập vào trang giao diện

# Các lỗi có thể xảy ra và cách khắc phục khi crawl
    1. No module named scrapy_proxies _ thiếu thư viện Scrapy Proxies _ pip install scrapy_proxies
    2. No module named win32api _ thiếu thư viện win32api _ pip install pypiwin32

