from prefect import flow, task, variables

@task
def test_task(x:int) -> int:
    print(variables.get("testvar"))
    print(type(variables.get("testvar")))
    return x * int(variables.get("testvar"))

@flow(log_prints=True)
def test210(x : int = 2):
    print("This is a test of 2.10")
    y = test_task(x)
    print(y)
    return y

if __name__ == "__main__":
    test210()