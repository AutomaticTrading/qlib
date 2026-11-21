"""Offline, non-publishing source-level guard for organizational workflow safety."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]

class WorkflowGuardTests(unittest.TestCase):
    def test_release_does_not_trigger_on_push(self):
        flow=(ROOT / ".github/workflows/release.yml").read_text()
        self.assertIn("  workflow_dispatch:",flow)
        self.assertNotRegex(flow,r"(?m)^  push:\s*$")
        self.assertIn("github.ref == 'refs/heads/main'",flow)
        self.assertIn("https://test.pypi.org/legacy/",flow)

if __name__ == "__main__":
    unittest.main()
