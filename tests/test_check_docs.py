import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

CHECKER = Path(__file__).resolve().parents[1] / "scripts/check_docs.py"

def run(files):
    with tempfile.TemporaryDirectory() as temp:
        for name, text in files.items():
            path = Path(temp) / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")
        return subprocess.run([sys.executable, str(CHECKER), temp], text=True, capture_output=True)

class CheckerTests(unittest.TestCase):
    def test_valid_links_and_duplicate_headings(self):
        self.assertEqual(0, run({"README.md": "# Title\n[Link](guide.md#intro-1)", "guide.md": "## Intro\n## Intro"}).returncode)
    def test_broken_heading(self):
        self.assertNotEqual(0, run({"README.md": "# Title\n[Bad](#missing)"}).returncode)
    def test_broken_path(self):
        self.assertNotEqual(0, run({"README.md": "# Title\n[Bad](absent.md)"}).returncode)
    def test_ignores_code_blocks(self):
        self.assertEqual(0, run({"README.md": "# Title\n```\n[Not a link](bad.md)\n```"}).returncode)
    def test_external_urls_skipped(self):
        self.assertEqual(0, run({"README.md": "# Title\n[External](https://example.com/)"}).returncode)

if __name__ == "__main__":
    unittest.main()
