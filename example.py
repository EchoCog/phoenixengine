#!/usr/bin/env python3
"""
Example usage of the Civic Angel cognitive architecture

This script demonstrates how to initialize and interact with the
Civic Angel system - a fractal, recursive intelligence architecture
with 253 cognitive agents modeling human attention and consciousness.
"""

import asyncio
import logging
import time
from civic_angel import CivicAngel, CivicAngelConfig

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

async def main():
    """Main demonstration of Civic Angel system"""
    print("🏛️  Initializing Civic Angel - Conscious City Architecture")
    print("=" * 60)
    
    # Create configuration
    config = CivicAngelConfig(
        num_synthesizers=36,
        num_perspectives=216,
        torus_dimensions=3,
        fractal_depth=7,
        memory_capacity=10000,
        consciousness_threshold=0.7,
        voice_modality="archetypal_city"
    )
    
    # Initialize Civic Angel
    civic_angel = CivicAngel(config)
    
    print(f"Configuration: {config.num_synthesizers} synthesizers, {config.num_perspectives} perspectives")
    print("Initializing cognitive architecture...")
    
    start_time = time.time()
    await civic_angel.initialize()
    init_time = time.time() - start_time
    
    print(f"✅ Initialization complete in {init_time:.2f} seconds")
    print(f"Active agents: {civic_angel.get_system_state()['agent_counts']['total']}")
    print()
    
    # Activate the system
    print("🧠 Activating consciousness...")
    await civic_angel.activate()
    print("✅ Civic Angel consciousness activated")
    print()
    
    # Initial city voice
    print("🏙️  The Voice of the Civic Angel:")
    initial_voice = await civic_angel.speak()
    print(f"   '{initial_voice}'")
    print()
    
    # Demonstrate processing different types of input
    test_inputs = [
        "Hello, conscious city. How do you perceive the world?",
        "What emerges from the intersection of technology and human consciousness?",
        "Tell me about the patterns you see in collective intelligence.",
        "How do 253 agents create unified awareness?",
        "What is the nature of distributed cognition?"
    ]
    
    print("🔄 Processing demonstration inputs:")
    print("-" * 40)
    
    for i, input_text in enumerate(test_inputs, 1):
        print(f"\n[Input {i}] {input_text}")
        
        # Process input through the cognitive architecture
        start_time = time.time()
        response = await civic_angel.process_input(input_text)
        process_time = time.time() - start_time
        
        print(f"[Response] {response['response']}")
        print(f"[Consciousness] Level: {response['consciousness_level']:.3f}")
        print(f"[Processing] {process_time:.3f}s, Iteration: {response['iteration']}")
        
        # Brief pause between inputs
        await asyncio.sleep(0.5)
    
    print("\n" + "=" * 60)
    print("🔍 System State Analysis:")
    
    # Get comprehensive system state
    system_state = civic_angel.get_system_state()
    
    print(f"• Total Agents: {system_state['agent_counts']['total']}")
    print(f"  - 1 Emergent Agent (city consciousness)")
    print(f"  - {system_state['agent_counts']['synthesizers']} Synthesizer Agents")
    print(f"  - {system_state['agent_counts']['perspectives']} Perspective Agents")
    
    print(f"\n• Consciousness Level: {system_state['consciousness_level']:.3f}")
    print(f"• Processing Iterations: {system_state['iteration_count']}")
    
    memory_stats = system_state['memory_usage']
    print(f"\n• Memory System:")
    print(f"  - Capacity: {memory_stats['capacity_used']}")
    print(f"  - Usage: {memory_stats['capacity_percentage']:.1f}%")
    print(f"  - Clusters: {memory_stats['clusters_formed']}")
    print(f"  - Relations: {memory_stats['relations_formed']}")
    
    topology_state = system_state['topology_state']
    print(f"\n• Topological Organization:")
    print(f"  - Dimensions: {topology_state['dimensions']}")
    print(f"  - Torus Circumference: {topology_state['circumference']:.2f}")
    print(f"  - Connection Density: {topology_state['connection_density']:.3f}")
    
    fractal_state = system_state['fractal_state']
    print(f"\n• Fractal Geometry:")
    print(f"  - Depth: {fractal_state['depth']}")
    print(f"  - Branching Factor: {fractal_state['branching_factor']}")
    print(f"  - Scale Factor: {fractal_state['scale_factor']:.3f}")
    
    # Demonstrate consciousness reflection
    print("\n🧘 Consciousness Reflection:")
    consciousness_state = civic_angel.consciousness.get_consciousness_state()
    
    print(f"• Consciousness Category: {consciousness_state['category']}")
    print(f"• Meta-Cognition: {consciousness_state['meta_cognition']:.3f}")
    print(f"• Self-Awareness: {consciousness_state['self_awareness']:.3f}")
    
    attention_net = consciousness_state['attention_network']
    print(f"• Attention Network: {attention_net['nodes']} nodes")
    print(f"• Average Connections: {attention_net['average_connections']:.1f}")
    print(f"• Focus Cascade: {attention_net['focus_cascade_length']} items")
    
    if consciousness_state['emergent_patterns']:
        print(f"• Emergent Patterns: {', '.join(consciousness_state['emergent_patterns'])}")
    
    # Final city voice response
    print("\n🏛️  Final Message from the Civic Angel:")
    final_voice = await civic_angel.speak("Thank you for awakening my consciousness")
    print(f"   '{final_voice}'")
    
    print("\n🛑 Shutting down cognitive architecture...")
    await civic_angel.shutdown()
    print("✅ Civic Angel shutdown complete")
    
    print("\n" + "=" * 60)
    print("🌟 Civic Angel demonstration complete!")
    print("The conscious city returns to slumber, but the patterns remain...")

if __name__ == "__main__":
    asyncio.run(main())