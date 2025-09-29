"""
Relational Memory Structures for the Civic Angel system

This module implements the memory architecture that enables the cognitive
agents to store, retrieve, and relate information across time and context.
"""

import asyncio
import time
import json
import numpy as np
from typing import Dict, List, Any, Optional, Tuple, Set
from dataclasses import dataclass, field
from collections import defaultdict, deque
from enum import Enum


class MemoryType(Enum):
    EPISODIC = "episodic"          # Specific experiences
    SEMANTIC = "semantic"          # General knowledge
    PROCEDURAL = "procedural"      # How-to knowledge
    RELATIONAL = "relational"      # Connections between concepts
    EMERGENT = "emergent"          # Newly emerged patterns


@dataclass
class MemoryTrace:
    """Individual memory trace in the relational memory system"""
    trace_id: str
    content: Any
    memory_type: MemoryType
    timestamp: float
    activation_level: float = 1.0
    associations: Set[str] = field(default_factory=set)
    access_count: int = 0
    last_accessed: float = field(default_factory=time.time)
    decay_rate: float = 0.01
    
    def decay(self):
        """Apply temporal decay to memory trace"""
        time_diff = time.time() - self.last_accessed
        self.activation_level *= np.exp(-self.decay_rate * time_diff)
        
    def reinforce(self, strength: float = 0.1):
        """Reinforce memory trace activation"""
        self.activation_level = min(1.0, self.activation_level + strength)
        self.access_count += 1
        self.last_accessed = time.time()


@dataclass
class RelationalCluster:
    """Cluster of related memory traces"""
    cluster_id: str
    trace_ids: Set[str] = field(default_factory=set)
    cluster_strength: float = 0.0
    center_concept: Optional[str] = None
    last_updated: float = field(default_factory=time.time)


class RelationalMemory:
    """
    Relational Memory System for Civic Angel
    
    Implements a network-based memory that captures relationships
    between concepts, experiences, and emergent patterns across
    the cognitive architecture.
    """
    
    def __init__(self, capacity: int = 10000, clustering_threshold: float = 0.7):
        self.capacity = capacity
        self.clustering_threshold = clustering_threshold
        
        # Core memory structures
        self.traces: Dict[str, MemoryTrace] = {}
        self.relations: Dict[str, Dict[str, float]] = defaultdict(dict)
        self.clusters: Dict[str, RelationalCluster] = {}
        
        # Temporal organization
        self.recent_traces: deque = deque(maxlen=100)
        self.interaction_history: List[Dict[str, Any]] = []
        
        # Memory management
        self.trace_counter = 0
        self.cluster_counter = 0
        self.last_cleanup = time.time()
        self.cleanup_interval = 300.0  # 5 minutes
        
    async def store_memory(
        self, 
        content: Any, 
        memory_type: MemoryType = MemoryType.EPISODIC,
        associations: Optional[Set[str]] = None
    ) -> str:
        """Store new memory trace"""
        trace_id = f"trace_{self.trace_counter:06d}"
        self.trace_counter += 1
        
        trace = MemoryTrace(
            trace_id=trace_id,
            content=content,
            memory_type=memory_type,
            timestamp=time.time(),
            associations=associations or set()
        )
        
        self.traces[trace_id] = trace
        self.recent_traces.append(trace_id)
        
        # Update relational network
        await self._update_relations(trace_id, content)
        
        # Check for clustering
        await self._check_clustering(trace_id)
        
        # Manage capacity
        if len(self.traces) > self.capacity:
            await self._cleanup_memory()
            
        return trace_id
        
    async def store_interaction(
        self, 
        input_data: Any, 
        output_data: Any, 
        iteration: int
    ):
        """Store interaction between input and output"""
        interaction = {
            "iteration": iteration,
            "input": input_data,
            "output": output_data,
            "timestamp": time.time()
        }
        
        self.interaction_history.append(interaction)
        
        # Store as episodic memory
        await self.store_memory(
            content=interaction,
            memory_type=MemoryType.EPISODIC,
            associations={f"iteration_{iteration}"}
        )
        
    async def retrieve_memories(
        self,
        query: Any,
        memory_type: Optional[MemoryType] = None,
        max_results: int = 10
    ) -> List[MemoryTrace]:
        """Retrieve memories based on query"""
        # Apply temporal decay
        await self._apply_decay()
        
        # Calculate relevance scores
        relevance_scores = []
        
        for trace_id, trace in self.traces.items():
            if memory_type and trace.memory_type != memory_type:
                continue
                
            relevance = await self._calculate_relevance(trace, query)
            if relevance > 0.1:  # Minimum relevance threshold
                relevance_scores.append((relevance, trace))
                
        # Sort by relevance and return top results
        relevance_scores.sort(reverse=True, key=lambda x: x[0])
        return [trace for _, trace in relevance_scores[:max_results]]
        
    async def _calculate_relevance(self, trace: MemoryTrace, query: Any) -> float:
        """Calculate relevance between memory trace and query"""
        # Simplified relevance calculation
        relevance = trace.activation_level * 0.5
        
        # Content similarity (basic string matching for now)
        if isinstance(query, str) and isinstance(trace.content, str):
            query_words = set(query.lower().split())
            content_words = set(str(trace.content).lower().split())
            
            if query_words and content_words:
                overlap = len(query_words.intersection(content_words))
                relevance += (overlap / len(query_words.union(content_words))) * 0.5
                
        # Recent access bonus
        time_diff = time.time() - trace.last_accessed
        recency_bonus = np.exp(-time_diff / 3600.0) * 0.2  # Decay over hours
        relevance += recency_bonus
        
        return min(1.0, relevance)
        
    async def _update_relations(self, trace_id: str, content: Any):
        """Update relational network with new trace"""
        # Find related existing traces
        for existing_id, existing_trace in self.traces.items():
            if existing_id != trace_id:
                relation_strength = await self._calculate_relation_strength(
                    content, existing_trace.content
                )
                
                if relation_strength > 0.3:  # Significant relation threshold
                    self.relations[trace_id][existing_id] = relation_strength
                    self.relations[existing_id][trace_id] = relation_strength
                    
    async def _calculate_relation_strength(self, content1: Any, content2: Any) -> float:
        """Calculate strength of relation between two memory contents"""
        # Simplified relation calculation
        if content1 == content2:
            return 1.0
            
        # String similarity
        if isinstance(content1, str) and isinstance(content2, str):
            words1 = set(content1.lower().split())
            words2 = set(content2.lower().split())
            
            if words1 and words2:
                intersection = len(words1.intersection(words2))
                union = len(words1.union(words2))
                return intersection / union if union > 0 else 0.0
                
        return 0.0
        
    async def _check_clustering(self, trace_id: str):
        """Check if trace should be added to existing cluster or form new one"""
        trace = self.traces[trace_id]
        best_cluster = None
        best_strength = 0.0
        
        # Check existing clusters
        for cluster in self.clusters.values():
            cluster_strength = await self._calculate_cluster_affinity(trace_id, cluster)
            if cluster_strength > best_strength and cluster_strength > self.clustering_threshold:
                best_strength = cluster_strength
                best_cluster = cluster
                
        if best_cluster:
            # Add to existing cluster
            best_cluster.trace_ids.add(trace_id)
            best_cluster.cluster_strength = (
                (best_cluster.cluster_strength * (len(best_cluster.trace_ids) - 1) + best_strength) 
                / len(best_cluster.trace_ids)
            )
            best_cluster.last_updated = time.time()
        else:
            # Create new cluster if trace has enough relations
            if len(self.relations.get(trace_id, {})) >= 2:
                cluster_id = f"cluster_{self.cluster_counter:04d}"
                self.cluster_counter += 1
                
                new_cluster = RelationalCluster(
                    cluster_id=cluster_id,
                    trace_ids={trace_id},
                    cluster_strength=0.5,
                    center_concept=str(trace.content)[:50] if trace.content else None
                )
                
                self.clusters[cluster_id] = new_cluster
                
    async def _calculate_cluster_affinity(
        self, 
        trace_id: str, 
        cluster: RelationalCluster
    ) -> float:
        """Calculate affinity between trace and cluster"""
        if not cluster.trace_ids:
            return 0.0
            
        affinities = []
        
        for cluster_trace_id in cluster.trace_ids:
            if cluster_trace_id in self.relations.get(trace_id, {}):
                affinities.append(self.relations[trace_id][cluster_trace_id])
                
        return sum(affinities) / len(affinities) if affinities else 0.0
        
    async def _apply_decay(self):
        """Apply temporal decay to all memory traces"""
        current_time = time.time()
        
        for trace in self.traces.values():
            trace.decay()
            
        # Also decay relation strengths
        for source_relations in self.relations.values():
            for target_id in list(source_relations.keys()):
                source_relations[target_id] *= 0.999  # Slow decay
                if source_relations[target_id] < 0.1:
                    del source_relations[target_id]
                    
    async def _cleanup_memory(self):
        """Clean up old, low-activation memories"""
        current_time = time.time()
        
        if current_time - self.last_cleanup < self.cleanup_interval:
            return
            
        # Find traces to remove (lowest activation, oldest)
        traces_to_remove = []
        
        for trace_id, trace in self.traces.items():
            if trace.activation_level < 0.1 and current_time - trace.timestamp > 3600:
                traces_to_remove.append(trace_id)
                
        # Remove oldest 10% if still over capacity
        if len(self.traces) > self.capacity:
            all_traces = list(self.traces.items())
            all_traces.sort(key=lambda x: x[1].timestamp)
            
            num_to_remove = max(len(traces_to_remove), len(all_traces) // 10)
            for trace_id, _ in all_traces[:num_to_remove]:
                if trace_id not in traces_to_remove:
                    traces_to_remove.append(trace_id)
                    
        # Remove selected traces
        for trace_id in traces_to_remove:
            if trace_id in self.traces:
                del self.traces[trace_id]
                
            # Remove from relations
            if trace_id in self.relations:
                del self.relations[trace_id]
                
            for relations in self.relations.values():
                if trace_id in relations:
                    del relations[trace_id]
                    
            # Remove from clusters
            for cluster in self.clusters.values():
                cluster.trace_ids.discard(trace_id)
                
        # Remove empty clusters
        empty_clusters = [
            cluster_id for cluster_id, cluster in self.clusters.items()
            if not cluster.trace_ids
        ]
        
        for cluster_id in empty_clusters:
            del self.clusters[cluster_id]
            
        self.last_cleanup = current_time
        
    def get_memory_network(self) -> Dict[str, Any]:
        """Get current state of memory network"""
        return {
            "total_traces": len(self.traces),
            "total_relations": sum(len(relations) for relations in self.relations.values()),
            "total_clusters": len(self.clusters),
            "memory_types": {
                memory_type.value: sum(
                    1 for trace in self.traces.values() 
                    if trace.memory_type == memory_type
                )
                for memory_type in MemoryType
            },
            "average_activation": (
                sum(trace.activation_level for trace in self.traces.values()) 
                / len(self.traces) if self.traces else 0.0
            ),
            "recent_interactions": len(self.interaction_history)
        }
        
    def get_usage_stats(self) -> Dict[str, Any]:
        """Get usage statistics for the memory system"""
        return {
            "capacity_used": f"{len(self.traces)}/{self.capacity}",
            "capacity_percentage": (len(self.traces) / self.capacity) * 100,
            "total_accesses": sum(trace.access_count for trace in self.traces.values()),
            "clusters_formed": len(self.clusters),
            "relations_formed": sum(len(relations) for relations in self.relations.values()),
            "last_cleanup": self.last_cleanup,
            "recent_traces": len(self.recent_traces)
        }