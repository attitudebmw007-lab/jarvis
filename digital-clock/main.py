#!/usr/bin/env python3
"""
Digital Clock - Multi-Timezone Display
A Python application that displays current time across multiple time zones
"""

import sys
import argparse
from digital_clock.clock import DigitalClock
from digital_clock.utils.logger import setup_logger

logger = setup_logger(__name__)

def main():
    """Main function to run Digital Clock."""
    parser = argparse.ArgumentParser(
        description='Digital Clock - Multi-Timezone Display',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py                              # Display default timezones
  python main.py --zones "US/Eastern" "US/Pacific"
  python main.py --format 24                  # 24-hour format
  python main.py --refresh 1                  # Refresh every 1 second
  python main.py --gui                        # Launch GUI version
        """
    )
    
    parser.add_argument(
        '--zones',
        nargs='+',
        help='List of timezones to display (e.g., US/Eastern US/Pacific)'
    )
    parser.add_argument(
        '--format',
        type=int,
        choices=[12, 24],
        default=12,
        help='Time format: 12 or 24 hour (default: 12)'
    )
    parser.add_argument(
        '--refresh',
        type=float,
        default=1.0,
        help='Refresh interval in seconds (default: 1.0)'
    )
    parser.add_argument(
        '--gui',
        action='store_true',
        help='Launch GUI version'
    )
    parser.add_argument(
        '--debug',
        action='store_true',
        help='Enable debug mode'
    )
    parser.add_argument(
        '--theme',
        choices=['dark', 'light', 'neon'],
        default='dark',
        help='Color theme for display (default: dark)'
    )
    
    args = parser.parse_args()
    
    try:
        logger.info("Starting Digital Clock application...")
        
        # Initialize Digital Clock
        clock = DigitalClock(
            timezones=args.zones,
            time_format=args.format,
            refresh_interval=args.refresh,
            debug=args.debug,
            theme=args.theme
        )
        
        # Display welcome message
        print("\n" + "="*70)
        print("  ⏰ DIGITAL CLOCK - MULTI-TIMEZONE DISPLAY")
        print("="*70)
        print(f"\n📍 Format: {'24-hour' if args.format == 24 else '12-hour'}")
        print(f"⚙️  Refresh: Every {args.refresh} second(s)")
        print(f"🎨 Theme: {args.theme.capitalize()}")
        print(f"⏱️  Press Ctrl+C to exit\n")
        
        # Run clock
        if args.gui:
            logger.info("Launching GUI version...")
            clock.run_gui()
        else:
            logger.info("Running in terminal mode...")
            clock.run_terminal()
        
    except KeyboardInterrupt:
        print("\n\n👋 Clock stopped. Goodbye!")
        logger.info("Digital Clock terminated by user")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Error: {str(e)}", exc_info=True)
        print(f"\n❌ Error: {str(e)}")
        sys.exit(1)

if __name__ == '__main__':
    main()
