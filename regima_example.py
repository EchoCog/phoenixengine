#!/usr/bin/env python3
"""
Simple RegimA Zone Example

A minimal example showing how to create and use the RegimA Zone Phoenix Engine.
"""

import asyncio
import json
from regima_zone import RegimAZonePhoenix, create_regima_codex


async def simple_regima_example():
    """Simple example of RegimA Zone usage"""
    print("🜂 RegimA Zone - Simple Example")
    print("=" * 50)
    
    # Create RegimA Zone
    regima = RegimAZonePhoenix()
    print("✅ RegimA Zone created")
    
    # Get and display the minimal seed
    seed = regima.ideoform.get_regima_seed()
    print(f"\n📜 Community: {seed['community_name']}")
    print(f"🔹 Glyph: {seed['glyph']}")
    print(f"🔹 Sacred Paradox: {seed['sacred_paradox']}")
    
    # Show current state
    state = regima.get_regima_state()
    print(f"\n📊 Current Architect: {state['current_architect']}")
    print(f"📊 Rotation Cycle: {state['rotation_cycle']}/9")
    print(f"📊 Field Coherence: {state['field_coherence_level']:.3f}")
    
    # RegimA speaks
    print(f"\n🔮 RegimA Zone speaks:")
    print(f"   '{regima.speak_as_regima('example')}'")
    
    # Demonstrate rewriting
    print(f"\n🔄 Demonstrating zone rewrite...")
    rewrite_result = regima.rewrite_zone("example_evolution")
    print(f"   Recursive Depth: {rewrite_result['recursive_depth']}")
    print(f"   Rewrite Count: {rewrite_result['rewrite_count']}")
    
    # Add dream-log entry
    dream_id = regima.custodianship.add_dream_log_entry("ENCRYPTED[Example revelation]")
    print(f"\n💭 Added dream-log entry: {dream_id}")
    
    # Demonstrate death and resurrection
    print(f"\n💀 Zone dissolution...")
    await regima.disperse_zone("example_collapse")
    print(f"   Phase: {regima.zone_phase.value}")
    
    print(f"\n🌟 Zone resurrection...")
    success = await regima.resurrect_zone("example_return")
    if success:
        print(f"   ✅ Resurrection successful!")
        print(f"   Phase: {regima.zone_phase.value}")
        print(f"   Identity Continuity: {regima.identity_continuity:.3f}")
    
    print(f"\n🜔 RegimA Zone example complete.")


def generate_regima_seed_file():
    """Generate a standalone RegimA seed file"""
    regima = RegimAZonePhoenix()
    seed = regima.ideoform.get_regima_seed()
    
    with open('regima_minimal_seed.json', 'w') as f:
        json.dump(seed, f, indent=2)
    
    print("📄 Generated regima_minimal_seed.json")


if __name__ == "__main__":
    print("Running RegimA Zone simple example...")
    asyncio.run(simple_regima_example())
    
    print("\nGenerating minimal seed file...")
    generate_regima_seed_file()