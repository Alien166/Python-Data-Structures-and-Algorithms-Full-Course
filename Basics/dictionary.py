capitals = {
    'Usa':'New york',
    "china":"beilig",
    "Russia":"Mosscow"
}
capitals.update({"German" : "Berlin"})
capitals.update({"china" : "mosk"})
capitals.pop("china")
print(capitals.keys())
print(capitals.values())
print(capitals.items())
print(capitals["Usa"])
print(capitals.get("china"))
