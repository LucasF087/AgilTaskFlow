import argparse
from .tasks import list_tasks, create_task, update_task, delete_task, get_task

def print_task(t):
    print(f"[{t.id}] {t.title} (priority={t.priority}) - {'done' if t.completed else 'todo'}")
    if t.description:
        print(f"    {t.description}")

def main():
    parser = argparse.ArgumentParser(description="Task manager CLI")
    sub = parser.add_subparsers(dest="cmd")

    sub_list = sub.add_parser("list")
    sub_create = sub.add_parser("create")
    sub_create.add_argument("title")
    sub_create.add_argument("--description", default="")
    sub_create.add_argument("--priority", default="medium")

    sub_get = sub.add_parser("get")
    sub_get.add_argument("id", type=int)

    sub_update = sub.add_parser("update")
    sub_update.add_argument("id", type=int)
    sub_update.add_argument("--title")
    sub_update.add_argument("--description")
    sub_update.add_argument("--completed", type=bool)
    sub_update.add_argument("--priority")

    sub_delete = sub.add_parser("delete")
    sub_delete.add_argument("id", type=int)

    args = parser.parse_args()
    if args.cmd == "list":
        for t in list_tasks():
            print_task(t)
    elif args.cmd == "create":
        t = create_task(args.title, args.description, args.priority)
        print("Created:")
        print_task(t)
    elif args.cmd == "get":
        t = get_task(args.id)
        if t:
            print_task(t)
        else:
            print("Not found")
    elif args.cmd == "update":
        t = update_task(args.id, title=args.title, description=args.description,
                        completed=args.completed, priority=args.priority)
        if t:
            print("Updated:")
            print_task(t)
        else:
            print("Not found")
    elif args.cmd == "delete":
        ok = delete_task(args.id)
        print("Deleted" if ok else "Not found")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()