# HotData

Written for CS 491 by Derek Stratton and Nick Harris

## Useful Things:
Microsoft Trace Download: http://iotta.snia.org/traces/158

Getting Started with TensorFlow: https://www.tensorflow.org/get_started/get_started_for_beginners

Microsoft Trace Info Paper: http://www.iiswc.org/iiswc2008/Papers/012.pdf

## Tasks:
1. Label each request in trace.csv as "hot" or "cold" based on if the FileObject associated is hot or cold
  - run through trace.csv and count the number of requests associated with each file FileObject (dictionary)
    - done
  - in the set of all request counts, find the 80th percentile (the 80% smallest on one side, the 20% biggest on the other)
    - done
  - associate each FileObject with "hot" if its in the top 20% and "cold" if its in the bottom 80%
    - done
  - go back thru the trace.csv and append "hot" or "cold", now that each FileObject has been recognized
    - done
2. Set up estimator for TensorFlow with python, using premade_estimator.py as a template for supervised learning Model
  - Import and parse the data
  - Create feature columns to describe the data
  - Train the data (let's use maybe 70-80% of the data from tracesample.csv)
  - Evaluate the model (maybe use a different 10-20% of the data from tracesample.csv)
  - Make sure the predictor works reasonably
3. Deploying our program to work on big data framework for our entire dataset
  - todo
