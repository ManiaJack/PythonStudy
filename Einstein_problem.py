#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'爱因斯坦谜题'

__author__ = 'ManiaJack'


def cut_relation(string):
    import re
    match_rule = r'^([\w\s]+)-([\w\s]+)$'
    return [re.match(match_rule, string).group(1), re.match(match_rule, string).group(2)]


def find_attr(relation_dict, relation):
    for k, v in relation_dict.items():
        if relation in v:
            return k


def answer(relations, question):
    # 定义类型，并将每一个属性默认设定为None
    class People(object):
        __slots__ = ('color', 'pet', 'beverage', 'cigarettes', 'nationality', 'number')

        def __init__(self):
            self.color = None
            self.pet = None
            self.beverage = None
            self.cigarettes = None
            self.nationality = None
            self.number = None

    relation_dict = {
        'color': ['blue', 'green', 'red', 'white', 'yellow'],
        'pet': ['cat', 'bird', 'dog', 'fish', 'horse'],
        'beverage': ['beer', 'coffee', 'milk', 'tea', 'water'],
        'cigarettes': ['Rothmans', 'Dunhill', 'Pall Mall', 'Winfield', 'Marlboro'],
        'nationality': ['Brit', 'Dane', 'German', 'Norwegian', 'Swede'],
        'number': ['1', '2', '3', '4', '5'],
    }
    # 建立五个实例，并使用颜色进行初始化
    peoples = [People() for _ in range(5)]
    for i in range(5):
        peoples[i].color = relation_dict['color'][i]
    unused_relation_pool = []
    # 将所有关系添加到关系池
    for relation in relations:
        unused_relation_pool.append(relation)
    times_flag = 0
    # 循环关系池中的关系对，对每个实例的属性进行匹配
    while len(unused_relation_pool) > 0:
        relation_flag = 0
        relation1, relation2 = cut_relation(unused_relation_pool[0])
        type1, type2 = find_attr(relation_dict, relation1), find_attr(relation_dict, relation2)
        for i in range(5):
            if getattr(peoples[i], type1) == relation1 or getattr(peoples[i], type2) == relation2:
                setattr(peoples[i], type1, relation1)
                setattr(peoples[i], type2, relation2)
                relation_flag = 1
                break
        if relation_flag == 0:
            unused_relation_pool.append(unused_relation_pool[0])
        unused_relation_pool.pop(0)
        times_flag += 1
        # 当匹配循环次数足够大时，对无法直接匹配的属性进行双属性同时匹配
        if times_flag == 50:
            for relation in unused_relation_pool:
                relation1, relation2 = cut_relation(relation)
                type1, type2 = find_attr(relation_dict, relation1), find_attr(relation_dict, relation2)
                count_flag = 0
                for i in range(5):
                    if not getattr(peoples[i], type1) and not getattr(peoples[i], type2):
                        count_flag += 1
                if count_flag == 1:
                    for i in range(5):
                        if not getattr(peoples[i], type1) and not getattr(peoples[i], type2):
                            setattr(peoples[i], type1, relation1)
                            setattr(peoples[i], type2, relation2)
                            break
            times_flag = 0
    # 当关系池匹配结束之后，根据属性字典补齐属性
    all_type = ['pet', 'color', 'beverage', 'cigarettes', 'nationality', 'number']
    for i in range(5):
        for types in all_type:
            if not getattr(peoples[i], types):
                temp_attr_list = []
                for j in range(5):
                    if getattr(peoples[j], types):
                        temp_attr_list.append(getattr(peoples[j], types))
                for attr in relation_dict[types]:
                    if attr not in temp_attr_list:
                        setattr(peoples[i], types, attr)
                        break
    # 分割问题，找出问题中给出的属性类型，并返回拥有该属性的实例的相应属性
    question_relation, question_type = cut_relation(question)
    question_relation_type = find_attr(relation_dict, question_relation)
    for i in range(5):
        if getattr(peoples[i], question_relation_type) == question_relation:
            return getattr(peoples[i], question_type)


if __name__ == '__main__':
    assert answer(('Norwegian-Dunhill', 'Marlboro-blue', 'Brit-3',
                   'German-coffee', 'beer-white', 'cat-water',
                   'horse-2', 'milk-3', '4-Rothmans',
                   'dog-Swede', 'Norwegian-1', 'horse-Marlboro',
                   'bird-Brit', '4-green', 'Winfield-beer',
                   'Dane-blue', '5-dog', 'blue-horse',
                   'yellow-cat', 'Winfield-Swede', 'tea-Marlboro'),
                  'fish-color') == 'green'  # What is the color of the house where the Fish lives?
    assert answer(('Norwegian-Dunhill', 'Marlboro-blue', 'Brit-3',
                   'German-coffee', 'beer-white', 'cat-water',
                   'horse-2', 'milk-3', '4-Rothmans',
                   'dog-Swede', 'Norwegian-1', 'horse-Marlboro',
                   'bird-Brit', '4-green', 'Winfield-beer',
                   'Dane-blue', '5-dog', 'blue-horse',
                   'yellow-cat', 'Winfield-Swede', 'tea-Marlboro'),
                  'tea-number') == '2'  # What is the number of the house where tea is favorite beverage?
    assert answer(('Norwegian-Dunhill', 'Marlboro-blue', 'Brit-3',
                   'German-coffee', 'beer-white', 'cat-water',
                   'horse-2', 'milk-3', '4-Rothmans',
                   'dog-Swede', 'Norwegian-1', 'horse-Marlboro',
                   'bird-Brit', '4-green', 'Winfield-beer',
                   'Dane-blue', '5-dog', 'blue-horse',
                   'yellow-cat', 'Winfield-Swede', 'tea-Marlboro'),
                  'Norwegian-beverage') == 'water'  # What is the favorite beverage of the Norwegian man?
