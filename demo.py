d = {
    1: ["qwe","Done"], 
    2: ["asd","Not Done"], 
    3: ["zxc","Done"]
    }
# print(d)
print("Task ID|Task|Status")
for task_id, (task, status) in d.items():
    print(f"{task_id}|{task}|{status}")

# Testing dictionary for Adding tasks
f = {
    2:["tyu","ghj"]
}
a = "lkj"
f.update({5:[f"{a}","Not Done"]})
print(f)

# Testing dictionary for Deleting tasks
# f.pop(2)
# print("Delete:\t",f)

# Testing dictionary for Update tasks
print("old: ",d)
id = 2
ts = d.get(2)
print(ts)
ts[1] = "Done"
d.update({id:[ts[0],ts[1]]})
print("New :",d)

