# Lesson - 12 
# ================================
# Homework: Multithreading in Python
# ================================
# Author: Sizning Ismingiz
# Description: This file contains two exercises:
#   1. Threaded Prime Number Checker
#   2. Threaded File Processing
# All solutions are written in one file for GitHub upload.
# ================================

import threading
from collections import defaultdict
import math

# ======================================
# Exercise 1: Threaded Prime Number Checker
# ======================================

def is_prime(num):
    """Check if a number is prime"""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    # check divisibility up to sqrt(num)
    for i in range(5, int(math.sqrt(num)) + 1, 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False
    return True


def prime_worker(start, end, results):
    """Thread worker to find prime numbers in a given range"""
    local_primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            local_primes.append(num)
    results.extend(local_primes)


def threaded_prime_checker(start, end, num_threads=4):
    """Divide the range into multiple threads to find primes"""
    threads = []
    results = []
    step = (end - start + 1) // num_threads

    for i in range(num_threads):
        sub_start = start + i * step
        # last thread goes until end
        sub_end = start + (i + 1) * step - 1 if i != num_threads - 1 else end
        t = threading.Thread(target=prime_worker, args=(sub_start, sub_end, results))
        threads.append(t)
        t.start()

    # wait for all threads to finish
    for t in threads:
        t.join()

    return sorted(results)


# ======================================
# Exercise 2: Threaded File Processing
# ======================================

def file_worker(lines, word_counts):
    """Thread worker to count words in given lines"""
    local_counts = defaultdict(int)
    for line in lines:
        words = line.strip().split()
        for word in words:
            cleaned_word = word.lower().strip(".,!?;:\"'()[]{}")
            if cleaned_word:
                local_counts[cleaned_word] += 1

    # merge local counts into shared dictionary
    with threading.Lock():
        for word, count in local_counts.items():
            word_counts[word] += count


def threaded_file_processing(file_path, num_threads=4):
    """Process file in multiple threads and count word occurrences"""
    with open(file_path, 'r', encoding="utf-8") as f:
        lines = f.readlines()

    threads = []
    word_counts = defaultdict(int)
    step = len(lines) // num_threads

    for i in range(num_threads):
        sub_lines = lines[i * step: (i + 1) * step] if i != num_threads - 1 else lines[i * step:]
        t = threading.Thread(target=file_worker, args=(sub_lines, word_counts))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return dict(word_counts)


# ======================================
# Main section to test both exercises
# ======================================
if __name__ == "__main__":
    print("===== Exercise 1: Threaded Prime Checker =====")
    primes = threaded_prime_checker(1, 100, num_threads=4)
    print("Prime numbers between 1 and 100:")
    print(primes)

    print("\n===== Exercise 2: Threaded File Processing =====")
    # Example: create a sample text file to test
    sample_file = "sample_text.txt"
    with open(sample_file, "w", encoding="utf-8") as f:
        f.write("Python is great. Python is powerful.\n")
        f.write("Multithreading can make Python faster in some cases.\n")
        f.write("Threads are useful for file processing and network tasks.\n")

    word_counts = threaded_file_processing(sample_file, num_threads=3)
    print("Word counts from file:")
    for word, count in word_counts.items():
        print(f"{word}: {count}")
