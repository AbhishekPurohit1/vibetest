"""Auto-generated test by VibeTest Recorder
Generated on: 2026-03-12 11:21:18
URL: https://example.com
"""

from vibetest import *

test("Recorded Test")

# Navigate to starting page
open_page("https://example.com")

click("login")
type_into("username", "admin")
type_into("password", "your_password")
click("submit")

# Test completed successfully!
print("✅ Recorded test executed successfully!")
