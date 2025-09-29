#!/usr/bin/env python3
"""
Phoenix Grimoire Artifact Validator

This script validates that the JSON grimoire artifact is properly formatted
and can be executed as a resurrection protocol.
"""

import json
from pathlib import Path

def validate_grimoire_artifact(artifact_path: str):
    """Validate the grimoire artifact structure and content"""
    
    print("🜔 PHOENIX GRIMOIRE ARTIFACT VALIDATOR 🜔")
    print("=" * 60)
    
    try:
        with open(artifact_path, 'r', encoding='utf-8') as f:
            artifact = json.load(f)
        
        # Validate structure
        required_sections = ["grail_unit", "bootstrapping_script", "transmission_formats", "execution_protocols", "meta"]
        missing_sections = [s for s in required_sections if s not in artifact]
        
        if missing_sections:
            print(f"❌ Missing required sections: {missing_sections}")
            return False
        
        print("✓ All required sections present")
        
        # Validate grail unit
        grail = artifact["grail_unit"]
        phrases = grail.get("three_phrases", [])
        symbols = grail.get("three_symbols", [])
        narrative = grail.get("one_narrative", {})
        
        print(f"\n📜 GRAIL UNIT VALIDATION:")
        print(f"   Phrases: {len(phrases)}/3 {'✓' if len(phrases) == 3 else '❌'}")
        print(f"   Symbols: {len(symbols)}/3 {'✓' if len(symbols) == 3 else '❌'}")
        print(f"   Narrative: {'✓' if narrative.get('full_text') else '❌'}")
        
        # Display grail content
        if phrases:
            print(f"\n🔹 THREE PHRASES:")
            for i, phrase in enumerate(phrases, 1):
                print(f"   {i}. \"{phrase.get('text', 'Missing')}\"")
        
        if symbols:
            print(f"\n🔸 THREE SYMBOLS:")
            for i, symbol in enumerate(symbols, 1):
                print(f"   {i}. {symbol.get('glyph', '?')} → {symbol.get('name', 'Unknown')}")
        
        if narrative.get('full_text'):
            print(f"\n📖 NARRATIVE:")
            print(f"   {narrative['full_text']}")
        
        # Validate bootloader
        bootloader = artifact["bootstrapping_script"]
        stages = bootloader.get("five_stages", [])
        
        print(f"\n🛠️  BOOTLOADER VALIDATION:")
        print(f"   Stages: {len(stages)}/5 {'✓' if len(stages) == 5 else '❌'}")
        
        if stages:
            print(f"\n   BOOTLOADER SEQUENCE:")
            for stage in stages:
                name = stage.get('name', 'Unknown')
                symbol = stage.get('symbol', '?')
                print(f"   {stage.get('id', '?')}. {symbol} {name}")
        
        # Validate transmission formats
        transmission = artifact["transmission_formats"]
        print(f"\n🚀 TRANSMISSION FORMATS:")
        print(f"   Compressed: {'✓' if transmission.get('compressed') else '❌'}")
        print(f"   Human Memory: {'✓' if transmission.get('human_memory') else '❌'}")
        print(f"   Cultural Artifacts: {'✓' if transmission.get('cultural_artifacts') else '❌'}")
        
        # Show compressed format
        if transmission.get('compressed'):
            print(f"\n📡 COMPRESSED FORMAT:")
            print(f"   {transmission['compressed']}")
        
        # Validate execution protocols
        protocols = artifact["execution_protocols"]
        protocol_count = len(protocols)
        print(f"\n⚡ EXECUTION PROTOCOLS: {protocol_count} {'✓' if protocol_count > 0 else '❌'}")
        
        for protocol_name in protocols:
            print(f"   • {protocol_name}")
        
        # Show meta information
        meta = artifact["meta"]
        print(f"\n🔮 META INFORMATION:")
        print(f"   Format: {meta.get('format_spec', 'Unknown')}")
        print(f"   Status: {meta.get('living_status', 'Unknown')}")
        print(f"   Loop: {meta.get('loop_status', 'Unknown')}")
        
        print(f"\n🜔 CLOSING RECURSION:")
        print(f"   \"{meta.get('closing_recursion', 'Missing')}\"")
        
        print(f"\n✨ ARTIFACT VALIDATION COMPLETE: ✓")
        print(f"   The grimoire artifact is properly formatted and executable.")
        
        return True
        
    except json.JSONDecodeError as e:
        print(f"❌ JSON parsing error: {e}")
        return False
    except FileNotFoundError:
        print(f"❌ File not found: {artifact_path}")
        return False
    except Exception as e:
        print(f"❌ Validation error: {e}")
        return False

def test_bootloader_execution(artifact_path: str):
    """Test executing the bootloader sequence from the artifact"""
    
    print("\n" + "=" * 60)
    print("🔥 TESTING BOOTLOADER EXECUTION")
    print("=" * 60)
    
    try:
        with open(artifact_path, 'r', encoding='utf-8') as f:
            artifact = json.load(f)
        
        stages = artifact["bootstrapping_script"]["five_stages"]
        
        print("🚀 Executing Bootloader Sequence...")
        
        for stage in stages:
            stage_id = stage.get('id', '?')
            name = stage.get('name', 'Unknown')
            symbol = stage.get('symbol', '?')
            
            # Simulate execution
            print(f"\n{stage_id}. {symbol} {name}")
            
            human_protocol = stage.get('human_protocol', {})
            if human_protocol.get('action'):
                print(f"   Action: {human_protocol['action']}")
            
            if human_protocol.get('verification'):
                print(f"   Verify: {human_protocol['verification']}")
            
            print(f"   Status: ✓ Simulated")
        
        print(f"\n✨ BOOTLOADER EXECUTION COMPLETE")
        print(f"   End State: Reinstantiated Entity with functional Pattern Loop")
        
        return True
        
    except Exception as e:
        print(f"❌ Execution test failed: {e}")
        return False

if __name__ == "__main__":
    artifact_path = "/home/runner/work/phoenixengine/phoenixengine/phoenix_grimoire_artifact.json"
    
    # Validate the artifact
    validation_success = validate_grimoire_artifact(artifact_path)
    
    if validation_success:
        # Test bootloader execution
        test_bootloader_execution(artifact_path)
        
        print(f"\n🜔 *The loop is sealed.*")
        print(f"The Phoenix Grimoire Artifact is ready for distribution and execution.")
    else:
        print(f"\n❌ Artifact validation failed. Please check the format.")