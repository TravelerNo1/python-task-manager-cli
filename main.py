from task import Task
from storage import load_tasks, save_tasks


def add_task(tasks):
    title = input("请输入任务标题: ")
    tasks.append(Task(title))
    print("✅ 添加成功")


def show_tasks(tasks):
    if not tasks:
        print("暂无任务")
        return

    for i, task in enumerate(tasks):
        status = "✔" if task.done else "✘"
        print(f"{i + 1}. [{status}] {task.title}")


def main():
    tasks = load_tasks()

    while True:
        print("\n=== 任务管理系统 ===")
        print("1. 查看任务")
        print("2. 添加任务")
        print("3. 标记完成")
        print("4. 删除任务")
        print("5. 修改任务")
        print("0. 退出")

        choice = input("请选择: ")

        if choice == "1":
            show_tasks(tasks)

        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks)

        elif choice == "3":
            show_tasks(tasks)
            index = int(input("编号: ")) - 1
            if 0 <= index < len(tasks):
                tasks[index].done = True
                save_tasks(tasks)

        elif choice == "4":
            show_tasks(tasks)
            index = int(input("编号: ")) - 1
            if 0 <= index < len(tasks):
                tasks.pop(index)
                save_tasks(tasks)

        elif choice == "5":
            show_tasks(tasks)
            index = int(input("编号: ")) - 1
            if 0 <= index < len(tasks):
                tasks[index].title = input("新标题: ")
                save_tasks(tasks)

        elif choice == "0":
            save_tasks(tasks)
            break
if __name__ == "__main__":
    main()