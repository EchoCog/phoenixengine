#!/usr/bin/env python3
"""
Simple Zone Phoenix Example

This demonstrates basic usage of The Zone Phoenix Engine.
Run this to see The Zone in action.
"""

import asyncio
from zone_phoenix import ZonePhoenixEngine


async def simple_zone_demo():
    """Simple demonstration of Zone Phoenix capabilities"""
    
    print("🌀 The Zone Phoenix Engine - Simple Demo")
    print("=" * 50)
    
    # Create The Zone
    zone = ZonePhoenixEngine()
    
    # Show initial state
    print(f"📊 Initial Zone: {zone.speak_as_zone('awakening')}")
    state = zone.get_zone_state()
    print(f"   Phase: {state['zone_phase']}")
    print(f"   Custodians: {state['active_custodians']}/{state['total_custodians']}")
    print(f"   Field Coherence: {state['field_coherence_level']:.3f}")
    print()
    
    # Show Zone Truths
    print("🔹 Zone Truths:")
    for i, truth in enumerate(state['zone_truths'], 1):
        print(f"   {i}. {truth}")
    print()
    
    # Show Zone Glyphs
    print("🔸 Zone Glyphs:")
    for glyph in state['zone_glyphs']:
        print(f"   {glyph}")
    print()
    
    # Demonstrate dissolution and resurrection
    print("💥 The Zone dissolves...")
    await zone.disperse_zone("example_dissolution")
    
    dispersed_state = zone.get_zone_state()
    print(f"💨 {zone.speak_as_zone('dissolved')}")
    print(f"   Phase: {dispersed_state['zone_phase']}")
    print(f"   Field Coherence: {dispersed_state['field_coherence_level']:.3f}")
    print()
    
    print("📡 Sending Zone Glyph Pulse...")
    success = await zone.resurrect_zone("example_pulse")
    
    if success:
        resurrected_state = zone.get_zone_state()
        print(f"🌟 {zone.speak_as_zone('resurrected')}")
        print(f"   Phase: {resurrected_state['zone_phase']}")
        print(f"   Field Coherence: {resurrected_state['field_coherence_level']:.3f}")
        print(f"   Resurrections: {resurrected_state['resurrection_count']}")
        print()
        
        print("✨ The Zone has demonstrated eternal recurrence!")
        print("   • Death as phase transition, not failure")
        print("   • Pattern preservation through dissolution")
        print("   • Emergent field of coherence resurrection")
        print("   • Fungal web resilience - living pattern")
    else:
        print("❌ Resurrection failed - not enough custodians")
    
    print()
    print("🔮 Final Zone Wisdom:")
    print(f"   '{zone.speak_as_zone('eternal')}'")


if __name__ == "__main__":
    asyncio.run(simple_zone_demo())