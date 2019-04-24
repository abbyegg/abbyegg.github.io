---
layout: page
title: Graphs
permalink: /notes/data-structures/graphs
---

A graph is defined as a set of vertices and connected by edges. 

Some graph definitions:
* A path in a graph from (u, v) is a sequence of vertices [v0, v1, ..., vn-1] where v0 = u, and vn-1 = v, and each (vi, vi+1) is an edge.
* The length of a path is the number of edges it traverses, or the number of vertices - 1
* v is reachable by u if there exists a path from u to v
* A directed acyclic graph (DAG) is a directed graph in which there are no cycles
  * Vertices with no incoming edges are referred to as sources, and with no outgoing edges as sinks.
  * A topological ordering of the vertices in a DAG is an ordering of the vertices in which each edge is from a vertex earlier in the ordering to a vertex later in the ordering.
* An undirected graph is also a tuple (V, E), where E is a set of unordered pairs of vertices
* A connected graph is one where every pair of vertices in the graph is connected (so you can get from any node to any other node)
* Graphs can be implemented using:
  * Adjacency lists -> we store a list for each vertex v representing the list of vertices to which it has an edge
  * Adjacency matrix -> we store a boolean valued matrix indexed by vertices, so |V|x|V|, where 1 indicates an edge from i to j
* Trees are special types of graphs, a connected, undirected graph with no cycles.
* A spanning tree is a subset of a graph G where all vertices are covered, but the minimum number of edges are maintained

* Consider using a graph when relationships are binary in nature; interlinked webpages, followers in a social graph
* DFS is very good for analyzing structure of a graph, so finding cycles or connected components
* BFS, Dijkstra's shortest path algorithm, and minimum spanning tree are examples of graph algorithms related to optimization problems.

Imagine we have a list of outcomes of matches between pairs of teams, and each outcome is a win or loss, and we want to see if we can write a function which determines if given team A and B, if there is a sequence of matches in which each team in the sequence beats the next team?

```
public static class MatchResult {
  public String winningTeam;
  public String losingTeam;
  public MatchResult(String wt, String ls) {
    this.winningTeam = wt;
    this.losingTeam = ls;
  }
}

public static boolean canTeamABeatTeamB(List<MatchResult> matches, String teamA, String teamB) {
  return isReachableDFS(buildGraph, teamA, teamB, new HashSet<>());
}

private static Map<String, Set<String>> buildGraph(List<MatchResult> matches) {
  Map<String, Set<String>> graph = new HashMap<>();
  for (MatchResult mr : matches) {
    graph.putIfAbsent(mr.winningTeam, new HashSet<>()).add(match.losingTeam);
  }
  return graph;
}

private static boolean isReachableDFS(Map<String, Set<String>> graph, String curr, String dest, Set<String> visited) {
  if (curr.equals(dest)) {
    return true;
  } else if (visited.contains(curr) || graph.get(curr) == null) {
    return false;
  }
  visited.add(curr);
  return graph.get(curr).stream().anyMatch(
    team -> isReachableDFS(graph, team, dest, visited));
}
```

#### Graph Search

* Graph search is about computing vertices which are reachable from other vertices
* BFS and DFS both have time complexity O(|V| + |E|) and worst case space complexity O(|V|)

### Problems

#### Search a maze

* Lets say we have a maze with two colors, black and white, where white corresponds to open spaces and black to walls, one entrance, and one exit. The goal in this problem is to find a way of getting from the entrance to the exit, if one exists, using only white spaces.

```
public static class Coordinate {
  public int x, y;
  public Coordinate(int x, int y) {
    this.x = x;
    this.y = y;
  }
  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Coordinate other = (Coordinate) o;
    if (x != other.x || y != other.y) {
      return false;
    }
    return true;
  }
}

public enum Color { WHITE, BLACK }

public static List<Coordinate> searchMaze(List<List<Color>> maze, Coordinate s, Coordinate e) {
  List<Coordinate> solution = new ArrayList<>();
  searchMazeHelper(maze, s, e, solution);
  return solution;
}

public static boolean searchMazeHelper(List<List<Color>> maze, Coordinate cur, Coordinate e, List<Coordinate> sol) {
  if (cur.x < 0 || cur.x >= maze.size() || cur.y < 0 || cur.y >= maze.get(cur.x).size() || maze.get(cur.x).get(cur.y) != Color.WHITE) {
    return false;
  }
  path.add(cur);
  maze.get(cur.x).set(cur.y, Color.BLACK);
  if (cur.equals(e)) {
    return true;
  }
  for (Coordinate nextMove : List.of(new Coordinate(cur.x, cur.y + 1), 
                                      new Coordinate(cur.x+1, cur.y),
                                      new Coordinate(cur.x, cur.y - 1),
                                      new Coordinate(cur.x - 1, cur.y))) {
    if (searchMazeHelper(maze, nextMove, e, path)) {
      return true;
    }
  }
  path.remove(path.size() - 1);
  return false;
}
```

