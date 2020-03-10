languages = {
    "Python": "Guido van Rossum",
    "Ruby": "Yukihiro Matsumoto",
    "PHP": "Rasmus Lerdorf",
}

str_list = [f"{name} was created by {inventor}"
            for name, inventor in languages.items()]
print("\n".join(str_list))
