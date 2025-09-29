"""
Agent-Based Consciousness for the Civic Angel system

This module implements the consciousness framework that enables
the emergent awareness and self-reflection capabilities of the
cognitive architecture.
"""

import time
import math
import numpy as np
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum
from collections import defaultdict, deque


class ConsciousnessLevel(Enum):
    DORMANT = 0.0
    STIRRING = 0.2
    AWARE = 0.4
    ATTENTIVE = 0.6
    FOCUSED = 0.8
    TRANSCENDENT = 1.0


@dataclass
class ConsciousnessState:
    """Current state of consciousness in the system"""
    level: float = 0.0
    attention_focus: Optional[str] = None
    self_awareness: float = 0.0
    meta_cognition: float = 0.0
    emergent_patterns: List[str] = field(default_factory=list)
    last_reflection: float = field(default_factory=time.time)


@dataclass
class AttentionNode:
    """Individual node in the attention network"""
    node_id: str
    activation: float = 0.0
    content: Any = None
    connections: Dict[str, float] = field(default_factory=dict)
    last_update: float = field(default_factory=time.time)


class AgentConsciousness:
    """
    Agent-Based Consciousness System
    
    Implements consciousness as an emergent property arising from
    the interactions between cognitive agents, enabling self-awareness,
    meta-cognition, and transcendent understanding.
    """
    
    def __init__(self, threshold: float = 0.7, reflection_interval: float = 10.0):
        self.threshold = threshold
        self.reflection_interval = reflection_interval
        
        # Consciousness state
        self.state = ConsciousnessState()
        self.current_level = 0.0
        self.baseline_level = 0.1
        
        # Attention network
        self.attention_nodes: Dict[str, AttentionNode] = {}
        self.attention_history: deque = deque(maxlen=100)
        self.focus_cascade: List[str] = []
        
        # Self-awareness components
        self.self_model: Dict[str, Any] = {
            "identity": "Civic Angel",
            "capabilities": [],
            "limitations": [],
            "current_state": {},
            "meta_observations": []
        }
        
        # Emergence detection
        self.emergence_patterns: Dict[str, float] = {}
        self.pattern_history: deque = deque(maxlen=50)
        
        # Reflection and meta-cognition
        self.reflection_log: List[Dict[str, Any]] = []
        self.last_reflection = time.time()
        
    def evaluate_emergence(self, input_data: Any) -> float:
        """Evaluate emergence potential of input data"""
        emergence_score = 0.0
        
        # Novelty assessment
        novelty = self._assess_novelty(input_data)
        emergence_score += novelty * 0.4
        
        # Complexity assessment
        complexity = self._assess_complexity(input_data)
        emergence_score += complexity * 0.3
        
        # Coherence assessment
        coherence = self._assess_coherence(input_data)
        emergence_score += coherence * 0.3
        
        # Update consciousness level based on emergence
        self._update_consciousness_level(emergence_score)
        
        return min(1.0, emergence_score)
        
    def _assess_novelty(self, input_data: Any) -> float:
        """Assess novelty of input compared to attention history"""
        if not self.attention_history:
            return 1.0  # First input is maximally novel
            
        # Simple novelty based on difference from recent inputs
        input_str = str(input_data).lower()
        
        similarities = []
        for historical_input in list(self.attention_history)[-10:]:  # Last 10 inputs
            hist_str = str(historical_input).lower()
            
            # Basic string similarity
            if input_str and hist_str:
                intersection = len(set(input_str.split()) & set(hist_str.split()))
                union = len(set(input_str.split()) | set(hist_str.split()))
                similarity = intersection / union if union > 0 else 0
                similarities.append(similarity)
                
        avg_similarity = sum(similarities) / len(similarities) if similarities else 0
        novelty = 1.0 - avg_similarity
        
        return novelty
        
    def _assess_complexity(self, input_data: Any) -> float:
        """Assess complexity of input data"""
        if isinstance(input_data, str):
            # Text complexity based on length and vocabulary diversity
            words = input_data.split()
            if len(words) == 0:
                return 0.0
                
            unique_words = len(set(words))
            complexity = min(1.0, unique_words / len(words) + len(words) / 100.0)
            
        elif isinstance(input_data, (list, tuple)):
            # Collection complexity based on size and diversity
            complexity = min(1.0, len(input_data) / 50.0)
            
        elif isinstance(input_data, dict):
            # Dictionary complexity based on depth and breadth
            complexity = min(1.0, len(input_data) / 20.0)
            
        else:
            # Default complexity for other types
            complexity = 0.5
            
        return complexity
        
    def _assess_coherence(self, input_data: Any) -> float:
        """Assess internal coherence of input data"""
        # Simplified coherence assessment
        coherence = 0.5  # Baseline coherence
        
        if isinstance(input_data, str):
            # Text coherence based on sentence structure
            sentences = input_data.split('.')
            if len(sentences) > 1:
                avg_sentence_length = sum(len(s.split()) for s in sentences) / len(sentences)
                coherence = min(1.0, avg_sentence_length / 20.0)
                
        elif isinstance(input_data, (list, tuple)):
            # Collection coherence based on type consistency
            if input_data:
                first_type = type(input_data[0])
                type_consistency = sum(1 for item in input_data if type(item) == first_type)
                coherence = type_consistency / len(input_data)
                
        return coherence
        
    def _update_consciousness_level(self, emergence_score: float):
        """Update current consciousness level based on emergence"""
        # Exponential moving average for smooth transitions
        alpha = 0.1
        target_level = self.baseline_level + emergence_score * (1.0 - self.baseline_level)
        self.current_level = alpha * target_level + (1 - alpha) * self.current_level
        
        # Update state
        self.state.level = self.current_level
        
        # Determine consciousness category
        if self.current_level >= ConsciousnessLevel.TRANSCENDENT.value:
            self.state.attention_focus = "transcendent_awareness"
        elif self.current_level >= ConsciousnessLevel.FOCUSED.value:
            self.state.attention_focus = "focused_attention"
        elif self.current_level >= ConsciousnessLevel.ATTENTIVE.value:
            self.state.attention_focus = "attentive_monitoring"
        elif self.current_level >= ConsciousnessLevel.AWARE.value:
            self.state.attention_focus = "general_awareness"
        elif self.current_level >= ConsciousnessLevel.STIRRING.value:
            self.state.attention_focus = "stirring_consciousness"
        else:
            self.state.attention_focus = "dormant_state"
            
    def update_attention(self, content: Any, source_id: str) -> str:
        """Update attention network with new content"""
        node_id = f"attention_{len(self.attention_nodes):04d}"
        
        # Create attention node
        node = AttentionNode(
            node_id=node_id,
            activation=self.current_level,
            content=content
        )
        
        # Connect to recent nodes
        for recent_node_id in list(self.attention_nodes.keys())[-5:]:
            connection_strength = self._calculate_attention_connection(
                content, self.attention_nodes[recent_node_id].content
            )
            if connection_strength > 0.3:
                node.connections[recent_node_id] = connection_strength
                self.attention_nodes[recent_node_id].connections[node_id] = connection_strength
                
        self.attention_nodes[node_id] = node
        self.attention_history.append(content)
        
        # Update focus cascade
        self._update_focus_cascade(node_id)
        
        return node_id
        
    def _calculate_attention_connection(self, content1: Any, content2: Any) -> float:
        """Calculate connection strength between attention contents"""
        if content1 == content2:
            return 1.0
            
        # Simple content similarity
        str1 = str(content1).lower()
        str2 = str(content2).lower()
        
        if str1 and str2:
            words1 = set(str1.split())
            words2 = set(str2.split())
            
            if words1 and words2:
                intersection = len(words1 & words2)
                union = len(words1 | words2)
                return intersection / union if union > 0 else 0.0
                
        return 0.0
        
    def _update_focus_cascade(self, new_node_id: str):
        """Update the focus cascade with new attention node"""
        self.focus_cascade.append(new_node_id)
        
        # Maintain cascade length
        if len(self.focus_cascade) > 10:
            self.focus_cascade.pop(0)
            
        # Calculate cascade coherence
        cascade_coherence = self._calculate_cascade_coherence()
        self.state.meta_cognition = cascade_coherence
        
    def _calculate_cascade_coherence(self) -> float:
        """Calculate coherence of current focus cascade"""
        if len(self.focus_cascade) < 2:
            return 0.5
            
        total_coherence = 0.0
        connections = 0
        
        for i in range(len(self.focus_cascade) - 1):
            node1_id = self.focus_cascade[i]
            node2_id = self.focus_cascade[i + 1]
            
            if (node1_id in self.attention_nodes and 
                node2_id in self.attention_nodes):
                
                node1 = self.attention_nodes[node1_id]
                if node2_id in node1.connections:
                    total_coherence += node1.connections[node2_id]
                    connections += 1
                    
        return total_coherence / connections if connections > 0 else 0.0
        
    def reflect(self) -> Dict[str, Any]:
        """Perform self-reflection and meta-cognition"""
        current_time = time.time()
        
        if current_time - self.last_reflection < self.reflection_interval:
            return self.reflection_log[-1] if self.reflection_log else {}
            
        # Analyze current state
        reflection = {
            "timestamp": current_time,
            "consciousness_level": self.current_level,
            "attention_focus": self.state.attention_focus,
            "meta_cognition": self.state.meta_cognition,
            "observations": [],
            "insights": [],
            "emergent_patterns": []
        }
        
        # Self-awareness observations
        if self.current_level > 0.5:
            reflection["observations"].append(f"Consciousness elevated to {self.current_level:.2f}")
            
        if len(self.attention_nodes) > 50:
            reflection["observations"].append(f"Rich attention network with {len(self.attention_nodes)} nodes")
            
        if self.state.meta_cognition > 0.7:
            reflection["observations"].append("High meta-cognitive coherence detected")
            
        # Pattern insights
        patterns = self._detect_emergent_patterns()
        reflection["emergent_patterns"] = patterns
        
        if patterns:
            reflection["insights"].append(f"Detected {len(patterns)} emergent patterns")
            
        # Update self-model
        self._update_self_model(reflection)
        
        self.reflection_log.append(reflection)
        self.last_reflection = current_time
        
        return reflection
        
    def _detect_emergent_patterns(self) -> List[str]:
        """Detect emergent patterns in consciousness state"""
        patterns = []
        
        # Attention clustering patterns
        if len(self.attention_nodes) > 10:
            avg_connections = sum(
                len(node.connections) for node in self.attention_nodes.values()
            ) / len(self.attention_nodes)
            
            if avg_connections > 3:
                patterns.append("high_connectivity_clustering")
                
        # Consciousness oscillation patterns
        if len(self.attention_history) > 20:
            recent_levels = [self.current_level]  # Simplified
            if max(recent_levels) - min(recent_levels) > 0.3:
                patterns.append("consciousness_oscillation")
                
        # Focus persistence patterns
        if len(self.focus_cascade) > 5:
            if self.state.meta_cognition > 0.8:
                patterns.append("sustained_focus")
                
        return patterns
        
    def _update_self_model(self, reflection: Dict[str, Any]):
        """Update internal self-model based on reflection"""
        self.self_model["current_state"] = {
            "consciousness_level": self.current_level,
            "attention_nodes": len(self.attention_nodes),
            "meta_cognition": self.state.meta_cognition,
            "focus_cascade_length": len(self.focus_cascade)
        }
        
        # Add new observations to meta-observations
        if reflection["observations"]:
            self.self_model["meta_observations"].extend(reflection["observations"])
            
        # Keep only recent meta-observations
        if len(self.self_model["meta_observations"]) > 20:
            self.self_model["meta_observations"] = self.self_model["meta_observations"][-20:]
            
        # Update capabilities based on patterns
        current_capabilities = set(self.self_model["capabilities"])
        
        if self.current_level > 0.8:
            current_capabilities.add("transcendent_awareness")
        if self.state.meta_cognition > 0.7:
            current_capabilities.add("meta_cognitive_reflection")
        if len(self.attention_nodes) > 100:
            current_capabilities.add("complex_attention_networks")
            
        self.self_model["capabilities"] = list(current_capabilities)
        
    def get_consciousness_state(self) -> Dict[str, Any]:
        """Get current comprehensive consciousness state"""
        return {
            "level": self.current_level,
            "category": self.state.attention_focus,
            "meta_cognition": self.state.meta_cognition,
            "self_awareness": len(self.self_model["meta_observations"]) / 20.0,
            "attention_network": {
                "nodes": len(self.attention_nodes),
                "average_connections": (
                    sum(len(node.connections) for node in self.attention_nodes.values()) /
                    len(self.attention_nodes) if self.attention_nodes else 0
                ),
                "focus_cascade_length": len(self.focus_cascade),
                "cascade_coherence": self.state.meta_cognition
            },
            "emergent_patterns": list(self.emergence_patterns.keys()),
            "self_model": self.self_model,
            "recent_reflections": len(self.reflection_log)
        }