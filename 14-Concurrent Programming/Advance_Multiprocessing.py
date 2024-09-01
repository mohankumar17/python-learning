from concurrent.futures import ProcessPoolExecutor
import time

def square_number(number):
    time.sleep(0.5)
    return number**2

if __name__ == "__main__":

    numbers=[1,2,3,4,5,6,7,8,9]
    
    with ProcessPoolExecutor(max_workers=3) as executor:
        start_time = time.time()
        
        results = list(executor.map(square_number,numbers))
        
        elapsed_time = time.time() - start_time
    
    for result in results:
        print(result, end = " ")

    print()
    print(f"Elapsed Time (in Seconds): {elapsed_time}")