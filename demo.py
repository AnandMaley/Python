d = {
    1: ["qwe","Done"], 
    2: ["asd","Not Done"], 
    3: ["zxc","Done"]
    }
# print(d)
print("Task ID|Task|Status")
for task_id, (task, status) in d.items():
    print(f"{task_id}|{task}|{status}")

f = {
    2:["tyu","ghj"]
}
a = "lkj"
f.update({5:[f"{a}","Not Done"]})
print(f)