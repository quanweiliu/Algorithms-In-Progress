Data structure
- **Array (fixed size)**
- **Dynamic array**
- Linked list
- TreeSet / TreeMap (ordered)
- **HashSet / HashMap (unordered)**
- **Heap / Priority queue**
- Deque / Queue / Stack
- Pair / Tuple
- Customized data structure

| Type | C++ | Java | Pythn |
| --- | --- | --- | --- |
| Array | T dirs[5]; | T[] dirs = new T [5]; | [0] * 5 |
| OrderedSet  OrderedMap| list\<T> | LinkList\<T> | N/A |
| HashSet <br> HashMap | set\<T> <br> map<T1, T2> | TreeSet\<T> <br> TreeMap<T1,T2> | set() <br> dict() |
| Heap | priority_queue\<T> | PriorityQueue\<T> | [] via heapq APIs |
| Deque <br> Queue| queue\<T> <br> deque<br> | Queue\<T> <br> Deque\<T> | collectios.deque() |
| Stack | stack\<T> | Stack\<T> | [] |
| Pair  Tuple| pair<T1, T2> <br> tuple <T1, T2, T3>| N/A | (x, y) <br> (x, y, z) |
| Customized | struct / class / long | class | class, tuple |

Array
| Type | C++ | Java | Pythn |
| --- | --- | --- | --- |
| 1D | array<int, 3> a{1,2,3}; <br> vector\<int> a(1,2,3); | int[] a = new int[n]{1,2,3}; | a = [1,2,3] |
| 1D init to x | vector\<int> a(n, x); <br> vector\<int> a(n); // x = 0 | int[] a = new int[n]; <br> Array.fill(a, x)| a = [x] * n |
| 2D init to x | vector\<vector\<int>> a(m, vector\<int>(n, x); | int[][] a = new int[m][n]; <br> for (int[] row : a) <br> Arrays.fill(row, x); | a = [[x] * n for _ in range(m)] |
| 3D init to x | vector<vector<vector\<int>>> a(k, vector\<vector\<int>>(m, vector\<int>(n, x))); | int[][][] a = new int[k][m][n]; <br> for (int [][] mat : a) <br>for (int[] row : mat) Arrays.fill(row, x); | a = [[[x] * n for _ in range(m)] for _ in range(k)] |

Dynamic Array
| Type | C++ | Java | Pythn |
| --- | --- | --- | --- |
| add | vector\<int> a; <br> a.push_back(); | List\<Integer> a = new ArrayList<>(); <br> a.Add(x); | a=[] <br> a.append(x) |
| remove | a.pop_back(); | a.remove(a.size() - 1); | del a[-1] <br> a[:-1] # made a copy |
| access | a[index]; <br> a.back(); | a.get(index); <br> a.get(a.size() - 1); | a[index] <br> a[-1] |

HashTable
| Type | C++ | Java | Pythn |
| --- | --- | --- | --- |
| create |unordered_map<int, int> m; | Map<Integer, Integer> m = new HashMap<>(); | a = dict() |
| insert | m[key] = value | m.put(key, value);| a[key] = value |
| get | value = m.at(key); <br> value = m[key]; | value = m.get(key); <br> value = m.getOrDefault(key, V); |   value = a[key] |
| contain | m.count(key); <br> auto it = m.find(key); <br> if (it == m.end()) A(); <br> else B();| m.containsKey(key); | key in a |
| iterate | for (const auto& p : m){ <br> key = p.first; <br> value = p.second; } | for (Integer key : m.keySet()) <br> value = m.get(key) <br> for (Map.Entry<Integer, Integet) entry : m.entrySet()) <br> entry.getKey(); entry.getValue(); | for key in a: <br> value = a[key] <br> for k,v in a.items(); <br> pass |

Priority queue / Heap
| Type | C++ | Java | Pythn |
| --- | --- | --- | --- |
| create | priority_queue\<int> q; <br> priority_queue\<int, vector\<int>, great\<int>> q;| Queue<Integer> q = new PriorityQueue<>(); | q=[] |
| create from array | vector\<int> a{1,2,3,4}; <br>  priority_queue\<int> q(begin(a), end(a)); | List\<Integer> a = ... <br> Queue<Interger> q = new PriorityQueue<>(a) | q=[2,1,3,4] <br> heapq.heapify(q) |
| insert | q.push(x); | q.offer(x); | heapq.heappush(q,x) |
| peek | int x = q.top(); | int x = q.peek(); | x = q[0] |
| pop | q.pop(); | int x = q.poll(); | x = heapq.heappop(q) |

Data structure (cont'd)
- auto type and type inference
-  type conversion
- string

Container conversion(使用构造函数，如set(), list(), 而不用循环)
| Type | C++ | Java | Python |
| --- | --- | --- | --- |
| list -> set | vector\<int> a{2,1,2,3}; <br> set\<int> b(begin(a), end(a)); | List\<Integer> a = ... <br> Set\<Integer> b = new HashSet<>(a); | a = [2,1,2,3] <br> b = set(a) |
| set -> list| set\<int> a{2,1,2,3}; <br> vector\<int> b(begin(a), end(a)); | Set\<Integer> a = .. <br> List\<Integer> b = new ArrayList<>(a); | a = set([2,1,2,3]) <br> b = list(a) |
| int -> string| int x = 12345; <br> string s = std::to_string(x) | int x = 12345; <br> String s = Integer.toString(x); <br> String s = String.valueOf(x); | x = 12345 <br> s = str(x)|
| string -> int| string s{"12345"}; <br> int x = std::stoi(s); | String s="12345"; <br> int x = Integer.parseInt(s); | s = "12345" <br> x = int(s) |
| char -> int| char c = '9';<br> int x = c - '0'; | char c = '9';<br> int x = c - '0'; <br> int x = Character.getNumericValue(c); | ch = '9' <br> x = ord(ch)-ord('0') <br> x = int(ch) |


string
| Type | C++ | Java | Python |
| --- | --- | --- | --- |
| create | string s; // s = ""; <br> string s = "LC huahua"; <br> string s{"LC huahua"}; <br> string s(5, "1") ;// "11111" | String s; // s = null; <br> String s = "LC huahua"; <br> String s = new String("LC huahua") ;<br> String s = new String(new, char[5]).replace("\0", "1"); | s = "" <br> s = str() <br> s = "LC huahua" <br> ''.join(['1]*5) |
| substring  | string s{"012345"}; <br> s.substr(3); // "345" <br> s.substr(3,2); // "34"| String s = new String s = "012345"; <br> s.substring(3); <br> s.substring(3,5); | s = "012345" <br> s[3:] <br> s[3:5] |
| change  | s[1]; // '1' <br> s[1]='h'; "0h2345"| s.charAt(1); <br> char[] arr = s.toCharArray(); <br> arr[1] = 'h' s = new String(arr); | l = list(s) <br> l[1] = 'h' <br> s = ''.join(l) <br> s = s[0:1] + 'h' + s[2:]|
| concat | s += "hello"; | s += "hello"; // another obj<br> StringBuilder sb(s); <br> sb.append("hello");<br> sb.toString();| s += "hello" |

[来源](https://www.bilibili.com/video/BV1ab411J7Zz?p=2)



