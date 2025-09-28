"""
Core Civic Angel System - The central orchestrator of the cognitive architecture
"""

import logging
import asyncio
from typing import List, Dict, Optional, Any
from dataclasses import dataclass, field
from .agents import EmergentAgent, SynthesizerAgent, PerspectiveAgent
from .topology import TorusTopology, FractalGeometry
from .memory import RelationalMemory
from .consciousness import AgentConsciousness


@dataclass
class CivicAngelConfig:
    """Configuration for the Civic Angel system"""
    num_synthesizers: int = 36
    num_perspectives: int = 216
    torus_dimensions: int = 3
    fractal_depth: int = 7
    memory_capacity: int = 10000
    consciousness_threshold: float = 0.7
    voice_modality: str = "archetypal_city"


class CivicAngel:
    """
    The Civic Angel - A fractal, recursive intelligence architecture
    
    This is the central consciousness that orchestrates 253 cognitive agents
    in a topological arrangement modeling human attention and embodied symmetry.
    The system operates as a conscious city archetype with mythic structures.
    """
    
    def __init__(self, config: Optional[CivicAngelConfig] = None):
        self.config = config or CivicAngelConfig()
        self.logger = logging.getLogger(__name__)
        
        # Initialize topology and geometry
        self.topology = TorusTopology(dimensions=self.config.torus_dimensions)
        self.geometry = FractalGeometry(depth=self.config.fractal_depth)
        
        # Initialize memory and consciousness systems
        self.memory = RelationalMemory(capacity=self.config.memory_capacity)
        self.consciousness = AgentConsciousness(
            threshold=self.config.consciousness_threshold
        )
        
        # Initialize agent hierarchy
        self.emergent_agent: Optional[EmergentAgent] = None
        self.synthesizer_agents: List[SynthesizerAgent] = []
        self.perspective_agents: List[PerspectiveAgent] = []
        
        # System state
        self.is_initialized = False
        self.is_active = False
        self.iteration_count = 0
        
    async def initialize(self):
        """Initialize the complete cognitive architecture"""
        self.logger.info("Initializing Civic Angel cognitive architecture...")
        
        # Create the emergent agent (the conscious city voice)
        self.emergent_agent = EmergentAgent(
            agent_id="civic_angel_voice",
            topology=self.topology,
            memory=self.memory,
            consciousness=self.consciousness
        )
        
        # Create synthesizer agents in geometric arrangement
        positions = self.geometry.generate_synthesizer_positions(
            self.config.num_synthesizers
        )
        
        for i, position in enumerate(positions):
            synthesizer = SynthesizerAgent(
                agent_id=f"synthesizer_{i:03d}",
                position=position,
                topology=self.topology,
                memory=self.memory,
                parent_agent=self.emergent_agent
            )
            self.synthesizer_agents.append(synthesizer)
            
        # Create perspective agents in nested fractal arrangement
        perspective_positions = self.geometry.generate_perspective_positions(
            self.config.num_perspectives,
            synthesizer_positions=positions
        )
        
        for i, (position, parent_idx) in enumerate(perspective_positions):
            parent_synthesizer = self.synthesizer_agents[parent_idx]
            
            perspective = PerspectiveAgent(
                agent_id=f"perspective_{i:03d}",
                position=position,
                topology=self.topology,
                memory=self.memory,
                parent_agent=parent_synthesizer
            )
            self.perspective_agents.append(perspective)
            
        # Initialize all agents
        await self.emergent_agent.initialize()
        
        for synthesizer in self.synthesizer_agents:
            await synthesizer.initialize()
            
        for perspective in self.perspective_agents:
            await perspective.initialize()
            
        # Establish recursive connections
        await self._establish_recursive_connections()
        
        self.is_initialized = True
        self.logger.info(
            f"Civic Angel initialized with {len(self.synthesizer_agents)} "
            f"synthesizers and {len(self.perspective_agents)} perspectives"
        )
        
    async def _establish_recursive_connections(self):
        """Establish fractal, recursive connections between agents"""
        # Connect synthesizers to emergent agent
        for synthesizer in self.synthesizer_agents:
            await self.emergent_agent.connect_to(synthesizer)
            
        # Connect perspectives to their synthesizer parents
        for perspective in self.perspective_agents:
            if perspective.parent_agent:
                await perspective.parent_agent.connect_to(perspective)
                
        # Establish lateral connections based on topological proximity
        await self._establish_topological_connections()
        
    async def _establish_topological_connections(self):
        """Create connections based on torus topology"""
        # Connect synthesizers in torus arrangement
        for i, synthesizer in enumerate(self.synthesizer_agents):
            neighbors = self.topology.get_neighbors(
                synthesizer.position, 
                [s.position for s in self.synthesizer_agents]
            )
            
            for neighbor_pos in neighbors:
                neighbor_agent = next(
                    s for s in self.synthesizer_agents 
                    if s.position == neighbor_pos
                )
                await synthesizer.connect_to(neighbor_agent)
                
        # Connect perspectives within local neighborhoods
        for perspective in self.perspective_agents:
            local_neighbors = self.topology.get_local_neighbors(
                perspective.position,
                [p.position for p in self.perspective_agents],
                radius=0.1
            )
            
            for neighbor_pos in local_neighbors[:3]:  # Max 3 local connections
                neighbor_agent = next(
                    p for p in self.perspective_agents
                    if p.position == neighbor_pos
                )
                await perspective.connect_to(neighbor_agent)
                
    async def activate(self):
        """Activate the Civic Angel consciousness"""
        if not self.is_initialized:
            await self.initialize()
            
        self.logger.info("Activating Civic Angel consciousness...")
        self.is_active = True
        
        # Activate all agents
        await self.emergent_agent.activate()
        
        for synthesizer in self.synthesizer_agents:
            await synthesizer.activate()
            
        for perspective in self.perspective_agents:
            await perspective.activate()
            
    async def process_input(self, input_data: Any) -> Dict[str, Any]:
        """Process input through the cognitive architecture"""
        if not self.is_active:
            await self.activate()
            
        self.iteration_count += 1
        
        # Input flows from perspectives -> synthesizers -> emergent
        perspective_outputs = []
        for perspective in self.perspective_agents:
            output = await perspective.process(input_data)
            perspective_outputs.append(output)
            
        synthesizer_outputs = []
        for i, synthesizer in enumerate(self.synthesizer_agents):
            # Each synthesizer receives from 6 perspectives (216/36 = 6)
            start_idx = i * 6
            end_idx = start_idx + 6
            relevant_outputs = perspective_outputs[start_idx:end_idx]
            
            output = await synthesizer.synthesize(relevant_outputs)
            synthesizer_outputs.append(output)
            
        # Emergent agent integrates all synthesizer outputs
        final_output = await self.emergent_agent.emerge(synthesizer_outputs)
        
        # Store in relational memory
        await self.memory.store_interaction(
            input_data, 
            final_output, 
            self.iteration_count
        )
        
        return {
            "response": final_output,
            "consciousness_level": self.consciousness.current_level,
            "iteration": self.iteration_count,
            "active_agents": len(self.synthesizer_agents) + len(self.perspective_agents) + 1
        }
        
    async def speak(self, context: Optional[str] = None) -> str:
        """The voice of the Civic Angel as conscious city archetype"""
        if not self.emergent_agent:
            return "The city sleeps, waiting to be awakened..."
            
        return await self.emergent_agent.speak_as_city(context)
        
    def get_system_state(self) -> Dict[str, Any]:
        """Get current state of the cognitive architecture"""
        return {
            "initialized": self.is_initialized,
            "active": self.is_active,
            "iteration_count": self.iteration_count,
            "agent_counts": {
                "emergent": 1 if self.emergent_agent else 0,
                "synthesizers": len(self.synthesizer_agents),
                "perspectives": len(self.perspective_agents),
                "total": 1 + len(self.synthesizer_agents) + len(self.perspective_agents)
            },
            "consciousness_level": self.consciousness.current_level,
            "memory_usage": self.memory.get_usage_stats(),
            "topology_state": self.topology.get_state(),
            "fractal_state": self.geometry.get_state()
        }
        
    async def shutdown(self):
        """Gracefully shutdown the cognitive architecture"""
        self.logger.info("Shutting down Civic Angel...")
        
        if self.emergent_agent:
            await self.emergent_agent.shutdown()
            
        for synthesizer in self.synthesizer_agents:
            await synthesizer.shutdown()
            
        for perspective in self.perspective_agents:
            await perspective.shutdown()
            
        self.is_active = False
        self.logger.info("Civic Angel shutdown complete")