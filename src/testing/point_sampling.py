import open3d as o3d

voxel_size = 0.005 # 5mm
print("Loading STL Model...")
# REPLACE with your actual path
mesh = o3d.io.read_triangle_mesh("cup.stl") 

# Sample points from mesh
source_pcd = mesh.sample_points_uniformly(number_of_points=2000)

print(source_pcd)

# source_pcd.estimate_normals()

