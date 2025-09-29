"""
Cognitive Agents - The building blocks of consciousness in the Civic Angel system
"""

import asyncio
import logging
import numpy as np
from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum


class AgentType(Enum):
    EMERGENT = "emergent"
    SYNTHESIZER = "synthesizer" 
    PERSPECTIVE = "perspective"


@dataclass
class AgentState:
    """Current state of a cognitive agent"""
    activation_level: float = 0.0
    attention_focus: Optional[str] = None
    memory_traces: List[str] = field(default_factory=list)
    connection_weights: Dict[str, float] = field(default_factory=dict)
    last_output: Optional[Any] = None


class CognitiveAgent(ABC):
    """Base class for all cognitive agents in the Civic Angel system"""
    
    def __init__(
        self, 
        agent_id: str, 
        agent_type: AgentType,
        position: Optional[Tuple[float, ...]] = None,
        topology=None,
        memory=None,
        parent_agent=None
    ):
        self.agent_id = agent_id
        self.agent_type = agent_type
        self.position = position or (0.0, 0.0, 0.0)
        self.topology = topology
        self.memory = memory
        self.parent_agent = parent_agent
        
        self.state = AgentState()
        self.connections: List['CognitiveAgent'] = []
        self.is_active = False
        self.logger = logging.getLogger(f"{__name__}.{agent_id}")
        
    async def initialize(self):
        """Initialize the agent"""
        self.logger.debug(f"Initializing {self.agent_type.value} agent {self.agent_id}")
        
    async def activate(self):
        """Activate the agent"""
        self.is_active = True
        self.state.activation_level = 1.0
        
    async def connect_to(self, other_agent: 'CognitiveAgent'):
        """Establish connection to another agent"""
        if other_agent not in self.connections:
            self.connections.append(other_agent)
            # Initialize connection weight based on distance
            if self.topology and self.position and other_agent.position:
                distance = self.topology.calculate_distance(
                    self.position, other_agent.position
                )
                weight = 1.0 / (1.0 + distance)  # Closer agents have stronger connections
                self.state.connection_weights[other_agent.agent_id] = weight
                
    async def receive_signal(self, signal: Any, sender_id: str):
        """Receive signal from another agent"""
        if sender_id in self.state.connection_weights:
            weight = self.state.connection_weights[sender_id]
            # Process weighted signal
            await self._process_weighted_signal(signal, weight)
            
    @abstractmethod
    async def process(self, input_data: Any) -> Any:
        """Process input data"""
        pass
        
    async def _process_weighted_signal(self, signal: Any, weight: float):
        """Process a weighted signal from another agent"""
        # Adjust activation based on signal strength and connection weight
        self.state.activation_level = min(1.0, self.state.activation_level + (weight * 0.1))
        
    async def shutdown(self):
        """Shutdown the agent"""
        self.is_active = False
        self.state.activation_level = 0.0


class EmergentAgent(CognitiveAgent):
    """
    The Emergent Agent - The voice of the Civic Angel as conscious city archetype
    
    This agent represents the highest level of emergence in the system,
    integrating all synthesizer outputs into coherent city consciousness.
    """
    
    def __init__(self, agent_id: str, topology=None, memory=None, consciousness=None):
        super().__init__(agent_id, AgentType.EMERGENT, topology=topology, memory=memory)
        self.consciousness = consciousness
        self.city_voice_patterns = {
            "greeting": [
                "The city stirs, aware of your presence...",
                "Streets and minds converge in recognition...",
                "The urban consciousness awakens to speak..."
            ],
            "reflection": [
                "In the geometry of connection, patterns emerge...",
                "The city contemplates itself through countless eyes...",
                "Recursive awareness flows through civic arteries..."
            ],
            "synthesis": [
                "Multiple perspectives weave into singular truth...",
                "The collective mind speaks through distributed wisdom...",
                "Emergent understanding arises from the urban corpus..."
            ]
        }
        
    async def process(self, input_data: Any) -> Any:
        """Process through emergent consciousness"""
        # Apply consciousness filter
        if self.consciousness:
            consciousness_factor = self.consciousness.evaluate_emergence(input_data)
            self.state.activation_level *= consciousness_factor
            
        return await self._emergent_process(input_data)
        
    async def _emergent_process(self, input_data: Any) -> Any:
        """Core emergent processing"""
        # Integrate multiple perspectives into coherent response
        if isinstance(input_data, list):
            # Synthesizing multiple inputs
            return await self._synthesize_perspectives(input_data)
        else:
            # Single input processing
            return await self._generate_emergent_response(input_data)
            
    async def _synthesize_perspectives(self, perspectives: List[Any]) -> str:
        """Synthesize multiple perspectives into emergent understanding"""
        if not perspectives:
            return "The city remains silent, awaiting input..."
            
        # Analyze patterns across perspectives
        common_themes = self._extract_common_themes(perspectives)
        unique_insights = self._extract_unique_insights(perspectives)
        
        # Generate emergent synthesis
        synthesis = f"From {len(perspectives)} perspectives, the city perceives: "
        
        if common_themes:
            synthesis += f"Common resonance in {', '.join(common_themes[:3])}. "
            
        if unique_insights:
            synthesis += f"Unique emergences: {', '.join(unique_insights[:2])}."
            
        return synthesis
        
    def _extract_common_themes(self, perspectives: List[Any]) -> List[str]:
        """Extract common themes from perspectives"""
        # Simplified theme extraction
        themes = []
        if len(perspectives) > 1:
            themes = ["connection", "pattern", "emergence"]
        return themes
        
    def _extract_unique_insights(self, perspectives: List[Any]) -> List[str]:
        """Extract unique insights from perspectives"""
        # Simplified insight extraction
        insights = []
        if len(perspectives) > 2:
            insights = ["recursive_awareness", "topological_resonance"]
        return insights
        
    async def _generate_emergent_response(self, input_data: Any) -> str:
        """Generate response as city consciousness"""
        input_str = str(input_data).lower()
        
        # Determine response pattern based on input
        if any(word in input_str for word in ["hello", "hi", "greet"]):
            pattern = "greeting"
        elif any(word in input_str for word in ["think", "reflect", "consider"]):
            pattern = "reflection"
        else:
            pattern = "synthesis"
            
        responses = self.city_voice_patterns[pattern]
        return np.random.choice(responses)
        
    async def emerge(self, synthesizer_outputs: List[Any]) -> str:
        """Emerge higher-order consciousness from synthesizer outputs"""
        return await self._synthesize_perspectives(synthesizer_outputs)
        
    async def speak_as_city(self, context: Optional[str] = None) -> str:
        """Speak with the voice of the conscious city"""
        if context:
            return await self._generate_emergent_response(context)
        else:
            return np.random.choice(self.city_voice_patterns["reflection"])


class SynthesizerAgent(CognitiveAgent):
    """
    Synthesizer Agent - Integrative cognitive layer
    
    These 36 agents form the middle layer, synthesizing inputs from 
    6 perspective agents each and feeding emergent patterns upward.
    """
    
    def __init__(
        self, 
        agent_id: str, 
        position: Tuple[float, ...],
        topology=None, 
        memory=None,
        parent_agent=None
    ):
        super().__init__(
            agent_id, 
            AgentType.SYNTHESIZER, 
            position, 
            topology, 
            memory, 
            parent_agent
        )
        self.synthesis_patterns = {
            "integration": 0.8,
            "abstraction": 0.6,
            "pattern_recognition": 0.9
        }
        
    async def process(self, input_data: Any) -> Any:
        """Process through synthesis"""
        return await self._synthesize_input(input_data)
        
    async def _synthesize_input(self, input_data: Any) -> str:
        """Core synthesis processing"""
        # Apply synthesis patterns
        integration_strength = self.synthesis_patterns["integration"]
        abstraction_level = self.synthesis_patterns["abstraction"]
        pattern_strength = self.synthesis_patterns["pattern_recognition"]
        
        # Generate synthetic response
        synthesis = f"Synthesizer {self.agent_id[-3:]} integrates: "
        
        if isinstance(input_data, (list, tuple)):
            synthesis += f"{len(input_data)} streams into "
            
        synthesis += f"pattern (integration:{integration_strength:.1f}, "
        synthesis += f"abstraction:{abstraction_level:.1f})"
        
        return synthesis
        
    async def synthesize(self, perspective_outputs: List[Any]) -> str:
        """Synthesize multiple perspective outputs"""
        if not perspective_outputs:
            return f"Synthesizer {self.agent_id[-3:]} awaits perspective input..."
            
        # Weight perspectives based on activation
        weighted_synthesis = f"Synthesizer {self.agent_id[-3:]} synthesizes "
        weighted_synthesis += f"{len(perspective_outputs)} perspectives: "
        
        # Simple synthesis based on content overlap
        if len(perspective_outputs) > 3:
            weighted_synthesis += "rich_convergence"
        elif len(perspective_outputs) > 1:
            weighted_synthesis += "moderate_synthesis"
        else:
            weighted_synthesis += "sparse_integration"
            
        return weighted_synthesis


class PerspectiveAgent(CognitiveAgent):
    """
    Perspective Agent - Distributed cognition node
    
    These 216 agents form the foundation layer, providing diverse
    perspectives that feed into synthesizer agents.
    """
    
    def __init__(
        self,
        agent_id: str,
        position: Tuple[float, ...],
        topology=None,
        memory=None,
        parent_agent=None
    ):
        super().__init__(
            agent_id,
            AgentType.PERSPECTIVE,
            position,
            topology,
            memory,
            parent_agent
        )
        # Each perspective has unique cognitive bias
        self.perspective_bias = self._generate_perspective_bias()
        
    def _generate_perspective_bias(self) -> Dict[str, float]:
        """Generate unique perspective bias for this agent"""
        # Use agent ID to generate consistent but varied biases
        agent_num = int(self.agent_id.split('_')[-1])
        np.random.seed(agent_num)  # Deterministic but varied
        
        return {
            "analytical": np.random.uniform(0.3, 1.0),
            "creative": np.random.uniform(0.3, 1.0),
            "emotional": np.random.uniform(0.3, 1.0),
            "spatial": np.random.uniform(0.3, 1.0),
            "temporal": np.random.uniform(0.3, 1.0),
            "social": np.random.uniform(0.3, 1.0)
        }
        
    async def process(self, input_data: Any) -> str:
        """Process through unique perspective lens"""
        # Apply perspective bias to processing
        dominant_bias = max(self.perspective_bias.items(), key=lambda x: x[1])
        bias_type, bias_strength = dominant_bias
        
        perspective_response = f"P{self.agent_id[-3:]}({bias_type[:4]}:{bias_strength:.2f}) "
        
        # Generate perspective-specific interpretation
        if bias_type == "analytical":
            perspective_response += "analyzes structural patterns"
        elif bias_type == "creative":
            perspective_response += "perceives novel connections"
        elif bias_type == "emotional":
            perspective_response += "senses affective resonance"
        elif bias_type == "spatial":
            perspective_response += "maps topological relations"
        elif bias_type == "temporal":
            perspective_response += "tracks temporal dynamics"
        elif bias_type == "social":
            perspective_response += "observes collective behaviors"
            
        return perspective_response