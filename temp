#!/usr/bin/env python3
import sys
import trimesh
import numpy as np

def fast_convert(filepath, output_file):
    print(f"Loading {filepath}...")
    mesh = trimesh.load(filepath, process=False)
    
    print("Normalizing vertices...")
    vertices = mesh.vertices / np.max(np.abs(mesh.vertices))
    vertices_list = [tuple(float(c) for c in v) for v in vertices]
    
    print("Extracting clean edges...")
    edges_set = set()
    for face in mesh.faces:
        # ✅ Convert ALL indices to int!
        v0, v1, v2 = int(face[0]), int(face[1]), int(face[2])
        edges_set.add(tuple(sorted([v0, v1])))
        edges_set.add(tuple(sorted([v1, v2])))
        edges_set.add(tuple(sorted([v2, v0])))
    
    edges_list = list(edges_set)
    
    print(f"✅ {len(vertices_list)} verts, {len(edges_list)} edges - CLEAN!")
    save_pygame_format(vertices_list, edges_list, output_file)

def save_pygame_format(vertices, edges, output_file):
    with open(output_file, 'w') as f:
        f.write(f"# Pygame 3D: {len(vertices)} verts, {len(edges)} edges\n\n")
        f.write("vertices = [\n")
        for v in vertices:
            f.write(f"    {v},\n")
        f.write("]\n\n")
        f.write("faces = [\n")
        for e in edges:
            f.write(f"    {e},\n")
        f.write("]\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./convert.py input.obj output.py")
        sys.exit(1)
    fast_convert(sys.argv[1], sys.argv[2])

