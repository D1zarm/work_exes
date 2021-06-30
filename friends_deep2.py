import json
import networkx as nx
import matplotlib.pyplot as plt

#Исследуемый пользователь - https://vk.com/id471883704 - Kodoku Rtn
#Пример первого уровня друзей - https://vk.com/id180945182 - Максим Вакулович
#Второй уровень друзей пользователя указанного выше - https://vk.com/id333007714 -Альбина Боковня

def main():
    graph = {}

    with open("test.json","r",encoding="utf-8") as file:
        graph = json.load(file)

    G = nx.from_dict_of_lists(graph)

    options = {
        'node_color': 'red',
        'node_size': 100, 
        'with_labels': True,
        'font_color': 'black',
        'style': 'dotted'
    }

    nx.draw(G, **options)

#Узлы не имеющие никаких связей отражают закрытые или удаленные профили
   
    plt.show()

  
if __name__ == '__main__':
    main()