import json
import os # 파이썬을 이용해서 시스템 내부에 접근이 가능하다


task_file = 'task.json'

def load_task():
    if os.path.exists(task_file):
        with open(task_file, 'r', encoding='utf-8') as file:
            return json.load(file) #json.load() 함수라고 하지만 메소드는 클래스 안에 구현된 함수다
    return []
def save_task(tasks): #add_task를 통해 전달받은 해야할일을 파일에 저장하는 기능
    with open(task_file, 'w', encoding='utf-8') as file: #file => open(task_file, 'w', encoding='utf-8')
        json.dump(tasks, file, indent=4, ensure_ascii=False)

def add_task(task_name): # 1번에 할일을추가하는 함수
    tasks = load_task()
    task = {'name': task_name, "completed":False}
    tasks.append(task)
    save_task(tasks)

def view_task(): # 할 일 목록보기, merge 진행
    tasks = load_task() # 파일이 있는 경우 안에 내용물이 tasks에 들어가고 없으면 빈 리스트가 들어감
    if not tasks: # tasks는 if문을 만나면 결과는 
        print("현재 등록된 작업이 없습니다.")
    else :
        print("작업 목록:")
        for i, task in enumerate(tasks, start=1):#enumerate() -> i = 1, task= {"name" : "파이썬 공부하기", "completed": false }
            status = "완료" if task ['complete'] else "미완료"  # 키값을 넣으면 자동적으로 반환(출력 또는 돌려주는거) 값을 준다
            print(f"{i}.{task['name']} - {status}")

def complete_task(task_number): # 할일 완료 함수
    tasks = load_task() #tasks = [{"name":"파이썬 공부하기", "completed":false}, ]
    if 1 <= task_number <= len (tasks):
        tasks[task_number-1]["completed"] = True
        save_task(tasks)
        print(f"할 일 : {tasks[task_number-1]['name']}이(가) 완료 처리 되었습니다")
    else :
        print("유효하지 않은 번호입니다. 다시 확인 후 입력해주세요.")
        
def delete_task(task_number): # 할일 삭제 함수
    pass


def show_menu():#메뉴를 보여주는 함수
    print("작업 관리 애플리케이션")
    print("1. 할 일 추가")
    print("2. 할 일 목록보기")
    print("3. 할 일 완료")
    print("4. 할 일 삭제")
    print("5. 종료")

def main():
    while True: 
        show_menu()
        choice = input("원하는 작업을 선택해주세요(1~5):")

        if choice == "1":
            task_name = input("추가할 작업을 입력해주세요") 
            add_task(task_name)
        elif choice == "2":
            view_task()
        elif choice == "3":
            task_number = int(input("완료를 원하는 작업의 번호를 입력해주세요"))
            complete_task(task_number)
        elif choice == "4":
            task_number = int(input("삭제를 원하는 작업의 번호를 입력해주세요"))
            delete_task(task_number)

        elif choice == "5":
            print("시스템을 종료합니다.")
            break
        else :
            print("잘못 입력하셨습니다. 1부터 5번까지의 기능을 선택하십시오")
main()