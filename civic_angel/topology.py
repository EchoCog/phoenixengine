"""
Topological Metaphors and Fractal Geometry for the Civic Angel system

This module implements the torus topology and fractal geometries that
organize the cognitive agents in meaningful spatial arrangements.
"""

import numpy as np
import math
from typing import List, Tuple, Dict, Any, Optional
from dataclasses import dataclass


@dataclass 
class TopologicalState:
    """Current state of the topological system"""
    torus_circumference: float
    current_mapping: Dict[str, Tuple[float, ...]]
    connection_density: float
    dimensional_coherence: float


class TorusTopology:
    """
    Torus Topology - The fundamental spatial organization
    
    Models the cognitive space as a torus, enabling wrapped connections
    and embodied symmetry that mirrors human attention patterns.
    """
    
    def __init__(self, dimensions: int = 3, major_radius: float = 2.0, minor_radius: float = 1.0):
        self.dimensions = dimensions
        self.major_radius = major_radius  # R - distance from center of tube to center of torus
        self.minor_radius = minor_radius  # r - radius of the tube
        self.circumference = 2 * math.pi * major_radius
        
        # Topological parameters
        self.wrap_threshold = 0.8  # When to wrap around the torus
        self.connection_radius = 0.3  # Radius for local connections
        
        self.state = TopologicalState(
            torus_circumference=self.circumference,
            current_mapping={},
            connection_density=0.0,
            dimensional_coherence=1.0
        )
        
    def map_to_torus(self, linear_position: float) -> Tuple[float, float, float]:
        """Map a linear position to 3D torus coordinates"""
        # Convert linear position to angular coordinates
        theta = 2 * math.pi * linear_position  # Angle around the tube
        phi = 2 * math.pi * (linear_position * 3.14159) % (2 * math.pi)  # Angle around the torus
        
        # Convert to Cartesian coordinates
        x = (self.major_radius + self.minor_radius * math.cos(theta)) * math.cos(phi)
        y = (self.major_radius + self.minor_radius * math.cos(theta)) * math.sin(phi)
        z = self.minor_radius * math.sin(theta)
        
        return (x, y, z)
        
    def calculate_distance(self, pos1: Tuple[float, ...], pos2: Tuple[float, ...]) -> float:
        """Calculate distance between two positions on the torus"""
        if len(pos1) != len(pos2):
            raise ValueError("Positions must have same dimensionality")
            
        # Standard Euclidean distance with torus wrapping
        squared_sum = 0.0
        for i in range(len(pos1)):
            diff = abs(pos1[i] - pos2[i])
            # Consider wrapping around the torus
            wrapped_diff = min(diff, self.circumference - diff)
            squared_sum += wrapped_diff ** 2
            
        return math.sqrt(squared_sum)
        
    def get_neighbors(
        self, 
        position: Tuple[float, ...], 
        all_positions: List[Tuple[float, ...]], 
        max_neighbors: int = 6
    ) -> List[Tuple[float, ...]]:
        """Get neighboring positions within connection radius"""
        neighbors = []
        distances = []
        
        for other_pos in all_positions:
            if other_pos != position:
                distance = self.calculate_distance(position, other_pos)
                if distance <= self.connection_radius:
                    neighbors.append(other_pos)
                    distances.append(distance)
                    
        # Sort by distance and return closest neighbors
        if neighbors:
            sorted_pairs = sorted(zip(distances, neighbors))
            return [pos for _, pos in sorted_pairs[:max_neighbors]]
        
        return []
        
    def get_local_neighbors(
        self,
        position: Tuple[float, ...],
        all_positions: List[Tuple[float, ...]],
        radius: float = 0.1
    ) -> List[Tuple[float, ...]]:
        """Get very local neighbors within small radius"""
        local_neighbors = []
        
        for other_pos in all_positions:
            if other_pos != position:
                distance = self.calculate_distance(position, other_pos)
                if distance <= radius:
                    local_neighbors.append(other_pos)
                    
        return local_neighbors
        
    def wrap_coordinate(self, coordinate: float) -> float:
        """Wrap coordinate around torus boundary"""
        return coordinate % self.circumference
        
    def calculate_curvature(self, position: Tuple[float, ...]) -> float:
        """Calculate local curvature at position on torus"""
        # Simplified curvature calculation
        x, y, z = position[:3]
        
        # Distance from central axis
        distance_from_center = math.sqrt(x**2 + y**2)
        
        # Gaussian curvature for torus: K = cos(theta) / (R(R + r*cos(theta)))
        if distance_from_center > 0:
            cos_theta = z / self.minor_radius if abs(z) <= self.minor_radius else 0
            denominator = self.major_radius * (self.major_radius + self.minor_radius * cos_theta)
            curvature = cos_theta / denominator if denominator != 0 else 0
        else:
            curvature = 0
            
        return curvature
        
    def get_state(self) -> Dict[str, Any]:
        """Get current topological state"""
        return {
            "dimensions": self.dimensions,
            "major_radius": self.major_radius,
            "minor_radius": self.minor_radius,
            "circumference": self.circumference,
            "mapped_positions": len(self.state.current_mapping),
            "connection_density": self.state.connection_density,
            "dimensional_coherence": self.state.dimensional_coherence
        }


class FractalGeometry:
    """
    Fractal Geometry - Recursive, self-similar spatial organization
    
    Generates fractal arrangements for agents, enabling recursive
    structures and perspectival cognitive geometries.
    """
    
    def __init__(self, depth: int = 7, branching_factor: int = 6):
        self.depth = depth
        self.branching_factor = branching_factor
        self.golden_ratio = (1 + math.sqrt(5)) / 2  # φ for natural proportions
        
        # Fractal parameters
        self.scale_factor = 0.618  # Based on golden ratio
        self.rotation_angle = 2 * math.pi / self.branching_factor
        
    def generate_synthesizer_positions(self, num_synthesizers: int) -> List[Tuple[float, float, float]]:
        """Generate positions for synthesizer agents in fractal arrangement"""
        positions = []
        
        # Arrange synthesizers in 6 layers of 6 agents each
        layers = 6
        agents_per_layer = num_synthesizers // layers
        
        for layer in range(layers):
            layer_radius = 1.0 + layer * 0.3  # Increasing radius per layer
            
            for i in range(agents_per_layer):
                angle = (2 * math.pi * i) / agents_per_layer
                # Add golden ratio spacing for natural distribution
                angle += layer * self.golden_ratio
                
                x = layer_radius * math.cos(angle)
                y = layer_radius * math.sin(angle)
                z = layer * 0.5  # Stack layers vertically
                
                positions.append((x, y, z))
                
        return positions[:num_synthesizers]
        
    def generate_perspective_positions(
        self, 
        num_perspectives: int,
        synthesizer_positions: List[Tuple[float, float, float]]
    ) -> List[Tuple[Tuple[float, float, float], int]]:
        """Generate positions for perspective agents nested around synthesizers"""
        positions_with_parents = []
        perspectives_per_synthesizer = num_perspectives // len(synthesizer_positions)
        
        for synthesizer_idx, synth_pos in enumerate(synthesizer_positions):
            # Generate fractal cluster around each synthesizer
            cluster_positions = self._generate_fractal_cluster(
                center=synth_pos,
                num_points=perspectives_per_synthesizer,
                radius=0.2
            )
            
            for pos in cluster_positions:
                positions_with_parents.append((pos, synthesizer_idx))
                
        return positions_with_parents[:num_perspectives]
        
    def _generate_fractal_cluster(
        self,
        center: Tuple[float, float, float],
        num_points: int,
        radius: float
    ) -> List[Tuple[float, float, float]]:
        """Generate fractal cluster of points around center"""
        positions = []
        cx, cy, cz = center
        
        # Use Fibonacci spiral for natural distribution
        for i in range(num_points):
            # Fibonacci spiral parameters
            t = i / num_points
            angle = 2 * math.pi * t * self.golden_ratio
            r = radius * math.sqrt(t)
            
            # Add fractal perturbation
            fractal_noise = self._fractal_noise(i, self.depth) * 0.1
            
            x = cx + r * math.cos(angle) + fractal_noise
            y = cy + r * math.sin(angle) + fractal_noise
            z = cz + (t - 0.5) * radius + fractal_noise
            
            positions.append((x, y, z))
            
        return positions
        
    def _fractal_noise(self, seed: int, depth: int) -> float:
        """Generate fractal noise for natural variation"""
        noise = 0.0
        amplitude = 1.0
        frequency = 1.0
        
        np.random.seed(seed)
        
        for i in range(depth):
            noise += amplitude * (np.random.random() - 0.5)
            amplitude *= self.scale_factor
            frequency *= 2.0
            
        return noise
        
    def calculate_fractal_dimension(self, positions: List[Tuple[float, ...]]) -> float:
        """Calculate approximate fractal dimension of position set"""
        if len(positions) < 2:
            return 0.0
            
        # Box-counting method approximation
        distances = []
        for i, pos1 in enumerate(positions):
            for pos2 in positions[i+1:]:
                dist = math.sqrt(sum((a - b)**2 for a, b in zip(pos1, pos2)))
                distances.append(dist)
                
        if not distances:
            return 0.0
            
        # Simple fractal dimension estimate
        min_dist = min(distances)
        max_dist = max(distances)
        
        if max_dist > min_dist:
            # Rough approximation based on scale invariance
            dimension = math.log(len(positions)) / math.log(max_dist / min_dist)
            return min(dimension, 3.0)  # Cap at 3D
        
        return 2.0  # Default planar dimension
        
    def get_recursive_structure(self, positions: List[Tuple[float, ...]]) -> Dict[str, Any]:
        """Analyze recursive structure in position arrangement"""
        if len(positions) < 3:
            return {"recursion_depth": 0, "self_similarity": 0.0}
            
        # Calculate center of mass
        center = tuple(
            sum(pos[i] for pos in positions) / len(positions)
            for i in range(len(positions[0]))
        )
        
        # Analyze scale-invariant patterns
        scales = [0.1, 0.3, 0.6, 1.0]
        similarities = []
        
        for scale in scales:
            scaled_positions = [
                tuple(center[i] + scale * (pos[i] - center[i]) for i in range(len(pos)))
                for pos in positions
            ]
            
            # Measure structural similarity (simplified)
            similarity = self._measure_structural_similarity(positions, scaled_positions)
            similarities.append(similarity)
            
        avg_similarity = sum(similarities) / len(similarities)
        
        return {
            "recursion_depth": len(scales),
            "self_similarity": avg_similarity,
            "scale_invariance": max(similarities) - min(similarities),
            "fractal_dimension": self.calculate_fractal_dimension(positions)
        }
        
    def _measure_structural_similarity(
        self, 
        positions1: List[Tuple[float, ...]], 
        positions2: List[Tuple[float, ...]]
    ) -> float:
        """Measure structural similarity between two position sets"""
        if len(positions1) != len(positions2):
            return 0.0
            
        # Simple distance-based similarity
        total_diff = 0.0
        for pos1, pos2 in zip(positions1, positions2):
            diff = math.sqrt(sum((a - b)**2 for a, b in zip(pos1, pos2)))
            total_diff += diff
            
        avg_diff = total_diff / len(positions1)
        # Convert to similarity score (0-1)
        similarity = 1.0 / (1.0 + avg_diff)
        
        return similarity
        
    def get_state(self) -> Dict[str, Any]:
        """Get current fractal geometry state"""
        return {
            "depth": self.depth,
            "branching_factor": self.branching_factor,
            "scale_factor": self.scale_factor,
            "golden_ratio": self.golden_ratio,
            "rotation_angle": self.rotation_angle
        }