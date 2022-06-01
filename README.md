# Implementing-BFS-and-DFS-for-robotic-path-planning
## Intoduction
Search-Based Planning is a motion planning approach that uses graph search methods to compute paths or
trajectories in a discretized environment, this project uses **Breadth-First Search (BFS)** and **Depth-First Search (DFS)**
as a Search-Based Planning Algorithms, and it's implemented using python with a predefined bitmap.

## Trials
a various trials have been carried out with different start and goal points.

**- Breadth-First-Search Algorithm 1st Trial,**  This path was generated using point **[0,0]** as an initial
point _(Start)_ and **[0,5]** as an ending point _(Goal)_, as we see the
algorithm was succeeded to achieve its mission and we have a free-obstacles path from start
point to the end one.

![BFS_Lec_EX](https://user-images.githubusercontent.com/105011124/171450127-c29e2ea1-218b-4338-ba71-12b9129ac4a3.png)

**- Breadth-First-Search Algorithm 2nd Trial,** This path was generated using point **[0,0]** as an initial
point _(Start)_ and **[180,620]** as an ending point _(Goal)_ , the map is updated to be a number-like obstacle.

![BFS_Ex2](https://user-images.githubusercontent.com/105011124/171450151-46619bd5-7b6a-483a-a355-ef5b258c574d.png)

**- Depth-First-Search Algorithm 1st Trial,** This path was generated using depth first algorithm with
**[0,0]** as initial point _(Start)_ to point [0,5] as ending point _(Goal)_

![DFS_Lec_EX](https://user-images.githubusercontent.com/105011124/171450148-c1eb4aca-ab25-4b46-ad30-631feb5a1772.png)

**- Depth-First-Search Algorithm 2nd Trial,** This path was generated using depth first algorithm with
**[0,0]** as initial point _(Start)_ to point **[5,5]** as ending point _(Goal)_ , and as we see the path isn’t optimal at all
however we reached to our goal at the end.

![BFS_Ex2](https://user-images.githubusercontent.com/105011124/171450151-46619bd5-7b6a-483a-a355-ef5b258c574d.png)

<p align="center">
  <img src="https://user-images.githubusercontent.com/105011124/171453434-75faf015-21cc-4973-aad7-bfc8310dd2c9.png">
</p>







