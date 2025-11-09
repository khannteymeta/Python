# Function no return & no return value
def my_function():
    print("Inside the function") 
    
    
# Lambda function
x = lambda a, b : a * b
y = lambda a : a + 10

print("x: ", x(5, 10))
print("y: ", y(5))



# Filter with lambda
numbers = [2,4,6,7,34,6,7,88]
# build in function filter
filter_result = filter(lambda n: n >= 34, numbers)
print("Filter result:", list(filter_result))

def my_function(x):
    # x = lambda name: print("Hello", x)
    x("Meta")
my_function(lambda x: print("Hello", x))



score_list = [23,45,67,89,12,90,34,56]
# Create function filter with lambda
def my_filter(compar, score_list):
    result = []
    for score in score_list:
        if compar(score):
            result.append(score)
    return result



filtered_scored = my_filter(lambda score: score >= 45, score_list)
print("Filtered scores:", filtered_scored)
