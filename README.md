# ftf

**ftf** is an abbreviation of the saying "first things first". In the context of this project **ftf** can be thought of as both a framework
(i.e. "put first things first") and a tool. The framework aims to enable individuals to effectively and efficently prioritize tasks, and 
the tool is a concrete instantition of this framework.

## Description

One of my main gripes with most task managers and to-do apps is their simplistic approach to time. They do frequently include defer
and due dates, and they sometimes also include task durations. However, I've yet to find an app that allows these components of time to 
interact, either with each other or with other task-relavant factors, in a way that determines priorities.

I think one of the main reasons why some neurodivergent folks struggle with many to-do apps is this neglect of the role of time in prioritization. It's not
enough to know that something is due on a certain day, you also need some indication of how much work is involved, and how that will 
affect your day-to-day. **ftf** is my attempt to correct for that oversight.

I have already explored some ideas by making a sort of prototype with Coda, so it is likely that **ftf** some form of the following:
- Tasks will interact with each other, e.g. dependencies, related tasks, etc.
- Prioritization will not only include due dates, but also duration estimates, and even subjective measures of importance.
- The user will be able to view tasks and task relationships in many different ways.
- It should always be absolutely clear to the user what the most important and/or pressing thing is that they could be doing.
- The tool should be as simple as humanly possible.

The prioritization algorithm is currently nothing more than a system of weights, collectively referred to (by me, nenakh) as "ROSEBuD":
- **R**equirement: Is the thing _required_ in some absolute sense, i.e. in the sense that taxes and life-saving treatments are required?
- **O**bligation: Is there some sort of "social obligation" involved, i.e. will your decisions effect others?
- **S**ignificance: How _significant_ is the thing to your own goals and motivations?
- **E**nthusiasm: How _enthusiastic_ are you about doing the thing?
- **Bu**rden: How much time, per day, will it take to complete the thing?
- **D**ue (or **D**eadline): How much total time do you have left until the thing is due?

The details of the algorithm may change, but the fundamental approach will likely remain more or less the same.

## Authors

just nenakh
