#!/usr/bin/env python3
import sys
import trimesh
import numpy as np

def fast_convert(filepath, output_file):
    print(f"Loading {filepath}...")
    mesh = trimesh.load(filepath, process=False)
    
    vertices_list = []
    edges_list = []
    
    # ✅ UNIVERSAL: Handle both Mesh and Scene
    if isinstance(mesh, trimesh.Scene):
        print(f"Scene: {len(mesh.geometry)} objects")
        for geom_name, geom in mesh.geometry.items():
            if isinstance(geom, trimesh.Trimesh) and len(geom.vertices) > 0:
                print(f"  Processing {geom_name} ({len(geom.vertices)} verts)")
                process_mesh(geom, vertices_list, edges_list)
    else:
        print("Single mesh")
        process_mesh(mesh, vertices_list, edges_list)
    
    print(f"✅ {len(vertices_list)} verts, {len(edges_list)} edges")
    save_pygame_format(vertices_list, edges_list, output_file)

def process_mesh(mesh, vertices_list, edges_list):
    """Process single Trimesh"""
    # Normalize vertices
    vertices = mesh.vertices / np.max(np.abs(mesh.vertices))
    vstart = len(vertices_list)
    vertices_list.extend([tuple(float(c) for c in v) for v in vertices])
    
    # Extract edges
    edges_set = set()
    for face in mesh.faces:
        v0, v1, v2 = int(face[0]), int(face[1]), int(face[2])
        edges_set.add(tuple(sorted([v0 + vstart, v1 + vstart])))
        edges_set.add(tuple(sorted([v1 + vstart, v2 + vstart])))
        edges_set.add(tuple(sorted([v2 + vstart, v0 + vstart])))
    
    edges_list.extend(list(edges_set))

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

