from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def dashboard(request):
    return render(request, 'dashboard.html')

def orders(request):
    fake_orders = [
        {"id": 1, "pair": "BTC → USDT", "amount": "0.5 BTC", "status": "Ожидание"},
        {"id": 2, "pair": "ETH → USDT", "amount": "2 ETH", "status": "Завершено"},
        {"id": 3, "pair": "LTC → BTC", "amount": "5 LTC", "status": "Отменено"},
        {"id": 4, "pair": "BNB → USDT", "amount": "1.5 BNB", "status": "Ожидание"},
        {"id": 5, "pair": "DOGE → USDT", "amount": "1000 DOGE", "status": "Завершено"},
    ]
    return render(request, 'orders.html', {"orders": fake_orders})