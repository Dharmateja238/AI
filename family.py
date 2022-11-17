from collections import defaultdict
class Solution:
  def __init__(self,head_name):
      self.family = defaultdict(list)
      self.head_name = head_name
      self.dead = set()
  def birth(self,parent_name,child_name):
      self.family[parent_name].append(child_name)
  def death(self,death_name):
    self.dead.add(death_name)
  def inheritance(self):
    self.ans = []
    self.depth_search(self.head_name)
    return self.ans
  def depth_search(self,current):
    if current not in self.dead:
      self.ans.append(current)
    for child in self.family[current]:
      self.depth_search(child)#recursion

obj=Solution('Paul')
obj.birth('Paul','Zach')
obj.birth('Paul','Jesse')
obj.birth('Jesse','Ursula')
obj.birth('Jesse','Ryan')
obj.birth('Jesse','Thea')
print("\n the curent family relation ship tree is \n",obj.inheritance())
obj.death('Paul')
print("\n after the head of the family 'Paul' is dead \n",obj.inheritance())
obj.death('Zach')
print("\n after the head of the family 'Zach' is dead \n",obj.inheritance())