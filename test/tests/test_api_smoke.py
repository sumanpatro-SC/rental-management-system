# tests/test_api_smoke.py

import unittest
import os
import time
import subprocess
import urllib.request
import urllib.error


class TestApiSmoke(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.port = 8000  # use int
        env = os.environ.copy()
        env["PORT"] = str(cls.port)

        # Start the Flask app as a subprocess
        cls.proc = subprocess.Popen(
            ["python", "app.py"],
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
        )

        # Wait a few seconds for the server to start
        time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        # Terminate the Flask server
        cls.proc.terminate()
        try:
            cls.proc.wait(timeout=3)
        except Exception:
            cls.proc.kill()

    def test_api_rentals_returns_200(self):
        """
        Test that GET /api/rentals returns status 200 and non-empty response
        """
        url = f"http://127.0.0.1:{self.port}/api/rentals"

        try:
            with urllib.request.urlopen(url) as resp:
                # Assert HTTP status code is 200
                self.assertEqual(resp.status, 200)

                # Assert response body is not empty
                body = resp.read().decode("utf-8")
                self.assertTrue(len(body) > 0)

        except urllib.error.URLError as e:
            self.fail(f"Could not connect to API: {e}")
