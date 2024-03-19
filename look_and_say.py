def look_and_say_sequence_recursive(n):
    if n == 1:
        return "1"
    
    else:
        before = look_and_say_sequence_recursive(n-1)
        answer = ""
        current_number = 0
        count = 0
        for i in range(len(before)):
            if i == 0:
                current_number = before[i]
                count = 1
            else:
                if before[i] == current_number:
                    count += 1
                else:
                    answer += f"{count}{current_number}"
                    current_number = before[i]
                    count = 1
        answer += f"{count}{current_number}"
    
        return answer

def look_and_say_sequence_loop(n):
    sequence = [1]
    for _ in range(n-1):
        new_sequence = []
        count = 0
        current_number = 0
        for i in range(len(sequence)):
            if i == 0:
                current_number = sequence[i]
                count = 1
            else:
                if sequence[i] == current_number:
                    count += 1
                else:
                    new_sequence.append(count)
                    new_sequence.append(current_number)
                    current_number = sequence[i]
                    count = 1
        new_sequence.append(count)
        new_sequence.append(current_number)
        
        sequence = new_sequence
    return ''.join(map(str, sequence))

def solution(n, method):
    result = {
        "recursive": look_and_say_sequence_recursive, 
        "loop": look_and_say_sequence_loop
    }.get(method, look_and_say_sequence_recursive)(n)

    length = len(result)
    
    return result[length//2-1: length//2+1]