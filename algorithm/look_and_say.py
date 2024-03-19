def look_and_say_sequence(n):
    if n == 1:
        return "1"
    
    else:
        before = list(look_and_say_sequence(n-1))
        answer = ""
        queue = []
        while before != []:
            num = before.pop(0)
            if queue == []:
                queue.append(num)
            elif queue[-1] == num:
                queue.append(num)
            else:
                answer += str(len(queue)) + queue[0]
                queue = [num]
        
        answer += str(len(queue)) + queue[0]
    
        return answer
    
def solution(n):
    result = look_and_say_sequence(n)
    length = len(result)
    
    return result[length//2-1: length//2+1]