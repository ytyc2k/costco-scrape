import re
aa='''\n\t\t\t\t\t\n\t\t\t\t\t\tSurprise your loved one; show your appreciation to friends, colleagues and clients. This is the opportunity to offer the world’s renowned Belgian chocolates. Made according to century-old traditions and flown in fresh from Brussels. Leonidas guarantees the freshness and quality of its chocolates. Theses are always made according to traditional methods, using only the finest ingredients like 100% pure cocoa butter for the coating, natural ingredients like fresh butter and fresh cream, and delicaci'''
bb=''.join(aa.split())
#filter(lambda x: x.strip() != "", str)
print(bb)