# Python - Async Comprehension

Master asynchronous generators and async comprehensions in Python 3.8+

---

## 📚 Projects Overview

This repository contains three interconnected async projects demonstrating:
- **Async Generators** - Creating asynchronous data sources
- **Async Comprehensions** - Collecting async data efficiently
- **Parallel Execution** - Running async tasks concurrently

---

## 🚀 Quick Start

```bash
mkdir python_async_comprehension
cd python_async_comprehension

# Create all three files
vi 0-async_generator.py
vi 1-async_comprehension.py
vi 2-measure_runtime.py

# Make executable
chmod +x *.py

# Run tests
./0-main.py
./1-main.py
./2-main.py
```

---

## 📋 Task 0: Async Generator

### What it does

Creates an asynchronous generator that:
- Loops 10 times
- Waits 1 second each iteration (asynchronously)
- Yields a random number between 0 and 10

### Key Concept: Async For Loop

```
async_generator()
    ↓
    Iteration 1: sleep(1) → yield(random)
    Iteration 2: sleep(1) → yield(random)
    ...
    Iteration 10: sleep(1) → yield(random)
    ↓
Done!
```

### Code

```python
#!/usr/bin/env python3
"""Module that contains an asynchronous generator"""

import asyncio
import random
from typing import AsyncGenerator

async def async_generator() -> AsyncGenerator[float, None]:
    """Yields 10 random numbers with 1 second delays."""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
```

### Output

```
[4.40, 6.91, 6.29, 4.55, 4.13, 9.99, 6.73, 9.84, 1.01, 1.38]
```

**Time: ~10 seconds** (10 iterations × 1 second each)

---

## 📋 Task 1: Async Comprehension

### What it does

Uses async comprehension to collect all 10 values from `async_generator` into a list

### Key Concept: Async List Comprehension

```
[i async for i in async_generator()]
    ↓
    Collects all yielded values
    ↓
Returns List[float]
```

### Code

```python
#!/usr/bin/env python3
"""Module that contains an asynchronous comprehension"""

from typing import List

async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> List[float]:
    """Collects 10 random numbers using async comprehension."""
    return [i async for i in async_generator()]
```

### Output

```
[9.86, 8.57, 1.75, 4.07, 0.55, 8.08, 8.39, 1.55, 7.71, 7.67]
```

**Time: ~10 seconds** (same as Task 0)

---

## 📋 Task 2: Parallel Runtime Measurement

### What it does

Executes `async_comprehension()` **4 times in parallel** using `asyncio.gather()`

### Key Concept: Parallel vs Sequential

#### ❌ Sequential (Would take 40 seconds)
```
async_comprehension() 1: |████████████| 10 sec
async_comprehension() 2: |████████████| 10 sec
async_comprehension() 3: |████████████| 10 sec
async_comprehension() 4: |████████████| 10 sec
                         ────────────────────
                         Total: 40 seconds ❌
```

#### ✅ Parallel (Takes only 10 seconds)
```
async_comprehension() 1: |████████████| 10 sec
async_comprehension() 2: |████████████| 10 sec  ← All at the same time!
async_comprehension() 3: |████████████| 10 sec
async_comprehension() 4: |████████████| 10 sec
                         ────────────────────
                         Total: 10 seconds ✅
```

### Code

```python
#!/usr/bin/env python3
"""Module that measures runtime of async comprehensions"""

import asyncio
import time
from typing import Callable

async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """Executes async_comprehension 4 times in parallel."""
    start_time = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time = time.time()
    return end_time - start_time
```

### Output

```
10.02193689346313
```

**Time: ~10 seconds** (not 40!)

---

## 🔑 Key Concepts Explained

### Async Generator vs Regular Generator

```python
# Regular Generator
def regular_gen():
    for i in range(3):
        yield i  # Immediate return

# Async Generator
async def async_gen():
    for i in range(3):
        await asyncio.sleep(1)  # Can await!
        yield i
```

### Async Comprehension vs Regular Comprehension

```python
# Regular Comprehension
[x * 2 for x in [1, 2, 3]]  # [2, 4, 6]

# Async Comprehension
[x async for x in async_generator()]  # Awaits each yield!
```

### asyncio.gather() - Run Tasks in Parallel

```python
# Sequential (slow)
await task1()
await task2()
await task3()

# Parallel (fast!)
await asyncio.gather(task1(), task2(), task3())
```

---

## 📊 Performance Comparison

| Configuration | Time | Speed |
|---|---|---|
| 1 × async_comprehension | 10 sec | Baseline |
| 4 × sequential | 40 sec | 4× slower |
| 4 × parallel (gather) | 10 sec | **Same as 1!** ⚡ |

---

## 🧪 Testing

```bash
# Test Task 0
python3 -c "
import asyncio
async_generator = __import__('0-async_generator').async_generator

async def test():
    count = 0
    async for i in async_generator():
        count += 1
    print(f'Generated {count} numbers')

asyncio.run(test())
"

# Test Task 1
python3 -c "
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension

async def test():
    result = await async_comprehension()
    print(f'Collected {len(result)} numbers')

asyncio.run(test())
"

# Test Task 2
python3 -c "
import asyncio
measure_runtime = __import__('2-measure_runtime').measure_runtime

async def test():
    runtime = await measure_runtime()
    print(f'Runtime: {runtime:.2f} seconds')

asyncio.run(test())
"
```

---

## 💡 Learning Path

```
Task 0: Async Generator
   ↓ (Learn how to yield values asynchronously)
   
Task 1: Async Comprehension
   ↓ (Learn how to collect async values)
   
Task 2: Parallel Execution
   ↓ (Learn how to run async tasks concurrently)
   
Mastery! 🎓
```

---

## 🎯 Requirements

- Python 3.8+
- Ubuntu 20.04 LTS
- PEP 8 compliant
- Type annotations required
- Documentation required

---

## 📚 Resources

- [PEP 530 - Asynchronous Comprehensions](https://www.python.org/dev/peps/pep-0530/)
- [asyncio Documentation](https://docs.python.org/3/library/asyncio.html)
- [Type Hints for Generators](https://docs.python.org/3/library/typing.html#typing.Generator)

---

## ✅ Checklist

- [ ] Task 0: Async Generator works (~10 sec)
- [ ] Task 1: Async Comprehension works (~10 sec)
- [ ] Task 2: Parallel execution works (~10 sec, not 40!)
- [ ] All files have shebang `#!/usr/bin/env python3`
- [ ] All files are executable
- [ ] All functions have type hints
- [ ] All functions have documentation
- [ ] No PEP 8 violations

---

**Created by:** Soufiane Filali  
**Date:** 2026-06-17  
**Project:** Holberton School - Web Backend
