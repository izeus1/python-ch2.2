
str3="""
ABC
가나다라마바사
"""
print(str3)

# escape
print("hello\nworld")

#
# 문자열 연산
#

str1 = "First String"
str2 = "Second String"

# 1. indexing
print(str1[0], str1[2], str1[4])

# 2. slicing
str3 = str2[2:5]
print(str3)

# 3. connect(+), + 생략 가능하다
print(str1 + " " + str2)
print("First String" " " " end")

# 에러: 문자열 객체끼리 +(연결) 연산을 할 수 있다.
name = "길동"
age = 40
print(name + str(40))
print(".....")

# 반복(*)
print(str1*3)

# len함수
print(len(str2))

# in, not in
print("S" in str2)
print("S" not in str2)

# 문자열은 객체는 변경할 수 없다.(immutable)
# str1[0] = "F"

# 서식(formating) - format() 함수
print("name: " + name + " age:" + format(age, "d"))
print("name: " + format(name, "s") + " age:" + format(age, "d"))

# 튜플을 이용한 서식(formating)
f = "name: %s, age:%d"
print(f)
print(f % (name, age))

# 서식 - formating that uses dictionary
f = "name:%(name)s, age:%(age)d"
print((f % {"name": "둘리", "age":30}))

f = "name:%(n)s, age:%(a)d"
print((f % {"n": "마이콜", "a":20}))









































