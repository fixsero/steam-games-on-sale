import requests
import webbrowser
import json

def get_on_sale_games():
    # Retrieve the JSON data for the current sales
    url = 'https://store.steampowered.com/api/featuredcategories'
    response = requests.get(url)
    data = response.json()
    categories = data['specials']['items']
    
    # Loop through the sales data and get information for each game
    on_sale_games = []
    for game in categories:
        appid = game['id']
        name = game['name']
        final_price = game['final_price']
        discount_percent = game['discount_percent']
        if final_price != 0:
            price = f"${final_price/100:.2f}"
        else:
            price = "Free"
        link = f"https://store.steampowered.com/app/{appid}"
        on_sale_games.append({'name': name, 'price': price, 'discount_percent': discount_percent, 'link': link})

    return on_sale_games

def main():
    on_sale_games = get_on_sale_games()
    print("Games on sale or free this month:")
    for game in on_sale_games:
        print(f"{game['name']} ({game['price']}, {game['discount_percent']}% off): {game['link']}")
        webbrowser.open(game['link'], new=2)
    input("Press Enter to close.")

if __name__ == '__main__':
    main()
