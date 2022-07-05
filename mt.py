import copy
import hashlib

def leaf_add(data,hash_function = 'sha256'):
    '''添加叶节点，前缀为00'''
    hash_function = getattr(hashlib, hash_function)
    data = b'\x00'+data.encode('utf-8')
    return hash_function(data).hexdigest()

def node_add(data,hash_function = 'sha256'):
    '''非叶节点，前缀为01'''
    hash_function = getattr(hashlib, hash_function)
    data = b'\x01'+data.encode('utf-8')
    return hash_function(data).hexdigest()

def display(merkle_tree,h):
    '''打印merkle树'''
    print('高度:',h)
    print('自底向上每层节点hash值为:')
    for i in range(h+1):
        print('第{0}层:\n{1}\n'.format(i+1,",\n".join(merkle_tree[i])))

def build_new(lst,hash_function = 'sha256'):
    lst_hash = []
    for i in lst:
        lst_hash.append(leaf_add(i))
    merkle_tree = [copy.deepcopy(lst_hash)]

    if len(lst_hash)<2:
        print("no tracnsactions to be hashed");return 0
    h = 0
    
    while len(lst_hash) >1:
        h += 1
        if len(lst_hash)%2 == 0:
            v = []
            while len(lst_hash)>1 :
                a = lst_hash.pop(0)
                b = lst_hash.pop(0)
                v.append(node_add(a+b, hash_function))
            merkle_tree.append(v[:])
            lst_hash = v
        else:
            v = []
            last_node = lst_hash.pop(-1)
            while len(lst_hash)>1:
                a = lst_hash.pop(0)
                b = lst_hash.pop(0)
                v.append(node_add(a+b, hash_function))
            v.append(last_node)
            merkle_tree.append(v[:])
            lst_hash = v
    return merkle_tree,h

def proof(merkle_tree,h,n,leaf,hash_function = 'sha256'):
    '''存在证明'''
    if n>=len(merkle_tree[0]):
        print("节点号错误");return 0
    print("序号:{0}，字符:{1}\n查找路径:".format(n,leaf))
    j=0 
    L = len(merkle_tree[0])
    if L%2 == 1 and L-1==n:
        hash_value = leaf_add(leaf)
        print('第{0}层Hash值:{1}'.format(j+1,hash_value))
    elif n%2==1:
        hash_value = node_add(merkle_tree[0][n-1]+leaf_add(leaf),hash_function)
        print('第{0}层查询值:{1}，\n\t生成的Hash值:{2}'.format(j+1,merkle_tree[0][n-1],hash_value))
    elif n%2==0:
        hash_value = node_add(leaf_add(leaf)+merkle_tree[0][n+1],hash_function)
        print('第{0}层查询值:{1}，\n\t生成的Hash值:{2}'.format(j+1,merkle_tree[0][n+1],hash_value))
    n = n//2
    j += 1 
    while j<h:
        L = len(merkle_tree[j])
        if L%2 == 1 and L-1==n:
            print('第{0}层hash值:{1}'.format(j+1,hash_value))
        elif n%2==1:
            hash_value = node_add(merkle_tree[j][n-1]+hash_value,hash_function)
            print('第{0}层查询值:{1}，\n\t生成的hash值:{2}'.format(j+1,merkle_tree[j][n-1],hash_value))
        elif n%2==0:
            hash_value = node_add(hash_value+merkle_tree[j][n+1],hash_function)
            print('第{0}层查询值:{1}，\n\t生成的hash值:{2}'.format(j+1,merkle_tree[j][n+1],hash_value))
        n = n//2
        j += 1

    print('\n根节点hash值:',merkle_tree[h][0])
    if hash_value==merkle_tree[h][0]:
        print("节点%s存在"%leaf)
    else:
        print("节点%s不存在"%leaf)


ls = []
for i in range(100000):
    ls.append(str(i))
merkleTree,h = build_new(ls)
print('节点:',', '.join(ls))
display(merkleTree,h)

leaf = input('要查找的节点：')
p = int(input('节点序号：'))
proof(merkleTree,h,p,leaf)
display(merkleTree,h)
proof(merkleTree,h,4,'e')
