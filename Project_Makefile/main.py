def type_check(a: str) -> bool:
    if type(a) == str:
        return True
    return False


if __name__ == "__main__":
    print(type_check("hello"))
