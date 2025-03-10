#LATIHAN 1

# def print_menu(menu_dict, parent_id=0, depth=0):
#     if parent_id in menu_dict:
#         for id_menu, label in menu_dict[parent_id]:
#             print("...." * depth + label)
#             print_menu(menu_dict, id_menu, depth + 1)

# def main():
#     n = int(input("Masukkan jumlah menu: "))
#     menu_dict = {}

#     for _ in range(n):
#         id_menu, parent, label = input().split(maxsplit=2)
#         id_menu, parent = int(id_menu), int(parent)

#         if parent not in menu_dict:
#             menu_dict[parent] = []
#         menu_dict[parent].append((id_menu, label))

#     print("\nOutput Menu:")
#     print_menu(menu_dict)

# main()


#LATIHAN 2

# def pali(n):
#     n = n.replace(" ", "").replace(",", "").replace(".", "")
#     n = n.lower()
#     if len(n)== 0 or len(n)==1:
#         return True
#     elif n[0] == n[-1]:
#         return pali(n[1:-1])
#     else:
#         return False

# print (pali("Aku suka rajawali, bapak. Apabila wajar, aku suka"))
# print (pali("Kasur ini rusak."))
# print (pali("Kasur Nababan rusak."))
# print (pali("Kasur Koh Ahok rusak."))
# print (pali("Ibu Ratna antar ubi."))
# print (pali("Ria Irawan nawari air"))
# print (pali("Harum semar kayak rames murah."))
# print (pali("Ira hamil lima hari."))