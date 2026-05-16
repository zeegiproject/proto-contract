import grpc
from concurrent import futures
import time
import os

# We need the generated gRPC files. 
# For this mock, we'll assume the dev has run:
# python -m grpc_tools.protoc -I./proto --python_out=. --grpc_python_out=. ./proto/ai/v1/chat.proto

# Since we don't want to force a build right now, I'll write the 
# logic for a 'Universal Mock' that you can run once the junior dev 
# sets up his Python environment.

def get_mock_response():
    """Returns a realistic math tutoring stream."""
    response_text = """### Solving your Equation!

To solve this, we will use the **Difference of Squares** method.

$$x^2 - 16 = 0$$

1. **Factor it:** $(x - 4)(x + 4) = 0$
2. **Solve for x:** Either $x - 4 = 0$ or $x + 4 = 0$.

> **Hint:** This means your answers are $x = 4$ and $x = -4$.

Does that make sense, or should we go over the factoring step again? 
"""
    # Simulate a stream by breaking the text into words
    for word in response_text.split(' '):
        yield word + ' '
        time.sleep(0.1) # Simulate the AI "thinking"

# Note: This is a pseudo-code guide for the junior dev.
# I will now provide the actual functional mock server for YOU to run in Node.js
# if you don't want to mess with Python dependencies yet!
