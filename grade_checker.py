# 성적조회프로그램

lst = []

while True:
    name = input("이름 : ")
    age = int(input("나이 : "))
    phone = input("연락처 : ")

    if age <= 0:
        break

    student = {"name": name, "age": age, "phone": phone}
    lst.append(student)

for i in lst:
    print(f"이름 : {i['name']}, 나이 : {i['age']}, 연락처 : {i['phone']}")

# 학생 성적 조회

student = {"kim": 85, "lee": 90, "choi": 100}

# 조회할 학생의 이름을 입력하세요 :
while True:
    search_name = input("\n조회할 학생의 이름을 입력하세요 (exit 입력 시 종료): ")
    # .strip().lower()  --> strip 은 앞뒤 공백제거 / 소문자 변경

    # exit 입력하면 프로그램 종료
    if search_name == "exit":
        print("프로그램을 종료합니다.")
        break

    # " " 학생의 점수는 " "점 입니다.
    if search_name in student.keys():
        print(f"{search_name} 학생의 점수는 {student[search_name]}점 입니다.")

    # " " 학생을 찾을 수 없습니다.
    else:
        print(f"{search_name} 학생을 찾을 수 없습니다.")



