#!/usr/bin/env python3
"""
Test script to validate the Cognitive Agent Hierarchy and the number 37.

This script verifies that the system correctly implements:
- 1 Governor (Emergent Agent) - The Quintessence
- 36 Conductors (Synthesizer Agents) - The Sulphur principle  
- Total top hierarchy = 37 agents
- No connection to mitochondrial DNA aspects
"""

import asyncio
import sys
import logging
from civic_angel.core import CivicAngel, CivicAngelConfig

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)


def test_hierarchy_validation():
    """Test that the hierarchy validation works correctly"""
    logger.info("🧪 Testing hierarchy validation...")
    
    # Test valid configuration
    try:
        config = CivicAngelConfig()
        assert config.validate_hierarchy() == True
        logger.info("✓ Valid hierarchy configuration passes validation")
    except Exception as e:
        logger.error(f"❌ Valid configuration failed: {e}")
        return False
        
    # Test invalid configurations
    try:
        invalid_config = CivicAngelConfig(num_synthesizers=35)  # Wrong number
        invalid_config.validate_hierarchy()
        logger.error("❌ Invalid configuration should have failed but didn't")
        return False
    except AssertionError:
        logger.info("✓ Invalid configuration correctly rejected")
    except Exception as e:
        logger.error(f"❌ Unexpected error: {e}")
        return False
        
    return True


async def test_agent_hierarchy():
    """Test the actual agent creation and hierarchy structure"""
    logger.info("🧪 Testing agent hierarchy creation...")
    
    try:
        # Create Civic Angel instance
        civic_angel = CivicAngel()
        
        # Initialize the system
        await civic_angel.initialize()
        
        # Verify hierarchy structure
        state = civic_angel.get_system_state()
        
        # Check core numbers
        assert state["agent_counts"]["emergent"] == 1, "Must have 1 Governor"
        assert state["agent_counts"]["synthesizers"] == 36, "Must have 36 Conductors"
        assert state["agent_counts"]["perspectives"] == 216, "Must have 216 Perspectives"
        assert state["agent_counts"]["total"] == 253, "Must have 253 total agents"
        
        # Check hierarchy 37
        hierarchy_info = state["hierarchy_37"]
        assert hierarchy_info["governor_count"] == 1, "Must have 1 Governor"
        assert hierarchy_info["conductor_count"] == 36, "Must have 36 Conductors"
        assert hierarchy_info["top_hierarchy_total"] == 37, "Top hierarchy must be 37"
        assert hierarchy_info["validates_37"] == True, "Must validate 37-agent hierarchy"
        
        # Check agent naming
        assert civic_angel.emergent_agent.agent_id == "governor_quintessence", "Governor has correct ID"
        assert all(agent.agent_id.startswith("conductor_") for agent in civic_angel.synthesizer_agents), "Conductors have correct naming"
        
        logger.info("✓ Agent hierarchy structure is correct")
        logger.info(f"  • Governor: {civic_angel.emergent_agent.agent_id}")
        logger.info(f"  • Conductors: {len(civic_angel.synthesizer_agents)} agents")
        logger.info(f"  • Perspectives: {len(civic_angel.perspective_agents)} agents")
        logger.info(f"  • Top hierarchy total: {hierarchy_info['top_hierarchy_total']}")
        logger.info(f"  • Note: {hierarchy_info['note']}")
        
        # Test system functionality
        response = await civic_angel.process_input("Test the 37-agent hierarchy")
        assert "response" in response, "System must respond to input"
        logger.info("✓ System processes input correctly")
        
        # Cleanup
        await civic_angel.shutdown()
        
        return True
        
    except Exception as e:
        logger.error(f"❌ Agent hierarchy test failed: {e}")
        return False


def test_mitochondrial_disclaimer():
    """Test that the system explicitly disclaims mitochondrial connections"""
    logger.info("🧪 Testing mitochondrial DNA disclaimer...")
    
    try:
        civic_angel = CivicAngel()
        state = civic_angel.get_system_state()
        
        # Check that the disclaimer is present
        disclaimer = state["hierarchy_37"]["note"]
        assert "No connection to mitochondrial DNA" in disclaimer, "Must include mitochondrial disclaimer"
        assert "purely cognitive architecture" in disclaimer, "Must emphasize cognitive nature"
        
        logger.info("✓ Mitochondrial DNA disclaimer is present")
        logger.info(f"  Note: {disclaimer}")
        
        return True
        
    except Exception as e:
        logger.error(f"❌ Mitochondrial disclaimer test failed: {e}")
        return False


async def run_all_tests():
    """Run all hierarchy tests"""
    logger.info("🚀 Starting Cognitive Agent Hierarchy Tests")
    logger.info("=" * 60)
    
    all_passed = True
    
    # Test 1: Hierarchy validation
    if not test_hierarchy_validation():
        all_passed = False
        
    # Test 2: Agent hierarchy structure  
    if not await test_agent_hierarchy():
        all_passed = False
        
    # Test 3: Mitochondrial disclaimer
    if not test_mitochondrial_disclaimer():
        all_passed = False
        
    logger.info("=" * 60)
    
    if all_passed:
        logger.info("🎉 ALL TESTS PASSED")
        logger.info("✓ Cognitive Agent Hierarchy correctly implements the number 37")
        logger.info("✓ 1 Governor + 36 Conductors = 37 top-level agents")
        logger.info("✓ No connection to mitochondrial DNA confirmed")
        logger.info("✓ System functions correctly with new hierarchy")
        return True
    else:
        logger.error("❌ SOME TESTS FAILED")
        return False


if __name__ == "__main__":
    # Run the tests
    result = asyncio.run(run_all_tests())
    
    # Exit with appropriate code
    sys.exit(0 if result else 1)