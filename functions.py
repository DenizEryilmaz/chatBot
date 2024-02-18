import json

def get_order_status():
    order_number = input("Sipariş numaranızı veya adınızı yazabilir misiniz? ")
    with open("data/user_data.json", "r", encoding="utf-8") as file:
        user_data = json.load(file)
        for user in user_data['users']:
            if user['name'].lower() == order_number.lower() or user['tracking_number'] == order_number.upper():
                return f"Sayın {user['name']}, siparişinizin durumu: {user['order_status']}"
        return "Üzgünüm, belirttiğiniz sipariş numarası veya adı ile eşleşen bir sipariş bulunamadı."

def cancel_order():
    order_number = input("Sipariş numaranızı yazabilir misiniz? ")
    with open("data/user_data.json", "r", encoding="utf-8") as file:
        user_data = json.load(file)
        for user in user_data['users']:
            if user['tracking_number'] == order_number.upper():
                confirm_cancel = input("Siparişinizi iptal etmek istediğinizi onaylamak için lütfen 'Evet' yanıtını verin: ")
                if confirm_cancel.lower() == 'evet':
                    user['order_status'] = "Cancelled"
                    with open("data/user_data.json", "w", encoding="utf-8") as outfile:
                        json.dump(user_data, outfile, ensure_ascii=False, indent=4)
                    return f"Sayın {user['name']}, siparişiniz iptal edilmiştir."
                else:
                    return "Sipariş iptal işlemi iptal edildi."
    return "Üzgünüm, belirttiğiniz sipariş numarası veya adı ile eşleşen bir sipariş bulunamadı."

def complaint():
    order_number = input("Sipariş numaranızı giriniz: ")
    complaint_text = input("Şikayetinizi yazınız: ")
    complaint_data = {
        "order_number": order_number,
        "complaint_text": complaint_text
    }
    with open("data/complaints.json", "a", encoding="utf-8") as file:
        json.dump(complaint_data, file, ensure_ascii=False)
        file.write("\n")
    return "Şikayetiniz başarıyla kaydedildi."

def customer_feedback():
    feedback_text = input("Geri bildiriminizi yazınız: ")
    feedback_data = {
        "feedback_text": feedback_text
    }
    with open("data/customer_feedback.json", "a", encoding="utf-8") as file:
        json.dump(feedback_data, file, ensure_ascii=False)
        file.write("\n")
    return "Geri bildiriminiz başarıyla kaydedildi."

def get_delivery_time():
    order_number = input("Sipariş numaranızı yazabilir misiniz? ")
    with open("data/user_data.json", "r", encoding="utf-8") as file:
        user_data = json.load(file)
        for user in user_data['users']:
            if user['tracking_number'] == order_number.upper():
                delivery_date = user['delivery_date']
                return f"Sayın {user['name']}, siparişiniz {delivery_date} tarihinde teslim edilecek."
    return "Üzgünüm, belirttiğiniz sipariş numarası veya adı ile eşleşen bir sipariş bulunamadı."

def get_sales_trends(tarih_araligi):
    with open("data/sales_trends.json", "r", encoding="utf-8") as file:
        sales_trends_data = json.load(file)["sales_trends"]

    response = f"{tarih_araligi} tarih aralığındaki satış trendleri:\n"
    for trend in sales_trends_data:
        response += f"{trend['tarih']}: {trend['satış_miktarı']} adet satış, {trend['gelir']} TL gelir\n"

    return response

def best_selling_products():
    with open("data/best_selling_products.json", "r", encoding="utf-8") as file:
        best_selling_data = json.load(file)["best_selling_products"]

    response = "En çok satan ürünler:\n"
    for product in best_selling_data:
        response += f"{product['ürün']}: {product['satış_adedi']} adet satış, {product['gelir']} TL gelir\n"

    return response
