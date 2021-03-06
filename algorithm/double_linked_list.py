class Node(object):
    # 双向链表节点
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None


class DLinkList(object):
    '''
    双向链表
    '''
    def __init__(self):
        self._head = None

    def is_empty(self):
        '''
        判断链表是否为空
        '''
        return self._head == None

    def get_length(self):
        '''
        返回链表长度
        '''
        cur = self._head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        '''
        遍历链表
        '''
        cur = self._head
        while cur != None:
            print(cur.item)
            cur = cur.next
        print("")

    def add(self, item):
        '''
        头部插入元素
        '''
        node = Node(item)
        if self.is_empty():
            '''
            如果是空链表,将node赋值给 _head
            '''
            self._head = node
        else:
            '''
            循环移动到链表尾部结点的位置
            '''
            cur = self._head
            while cur.next != None:
                cur = cur.next
            '''将尾结点 cur 的 next 指针指向 node '''
            cur.next = node
            ''' 将 node 的 prev 指针指向 cur '''
            node.prev = cur

    def search(self, item):
        ''' 查找元素是否存在 '''
        cur = self._head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False

    def insert(self, pos, item):
        ''' 在指定位置添加节点 '''
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            node = Node(item)
            cur = self._head
            count = 0
            ''' 移动到指定位置的前一个位置 '''
            while count < (pos - 1):
                count += 1
                cur = cur.next
            ''' 将 node 的前驱指针 prev 指向 cur '''
            node.prev = cur
            ''' 将 node 的后驱指针 next 指向 cur 的下一个结点 '''
            node.next = cur.next
            ''' 将 cur 的下一个结点的前驱指针指向 node '''
            cur.next.prev = node
            ''' 将 cur 的后驱指针 next 指向node '''
            cur.next = node

    def remove(self, item):
        ''' 删除元素 '''
        if self.is_empty():
            return
        else:
            cur = self._head
            if cur.item == item:
                ''' 如果首节点的元素即是要删除的元素 '''
                if cur.next == None:
                    ''' 如果链表只有一个节点 '''
                    self._head = None
                else:
                    ''' 将第二个节点的前驱指针 prev 设置为None '''
                    cur.next.prev = None
                    ''' 将 _head 头节点 指向下一个节点 '''
                    self._head = cur.next
                return
            while cur != None:
                if cur.item == item:
                    ''' 将 cur 的前一个节点的后驱指针 next 指向 cur 的后一个节点 '''
                    cur.prev.next = cur.next
                    ''' 将 cur 的后一个节点的前驱指针 prev 指向 cur 的前一个结点 '''
                    cur.next.prev = cur.prev
                    break
                cur = cur.next

