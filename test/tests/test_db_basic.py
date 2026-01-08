# tests/test_db_basic.py

import unittest
import sqlite3
import os


class TestDatabaseBasics(unittest.TestCase):

    def test_rental_db_exists(self):
        """
        Check that the database file 'rental.db' exists in the project.
        """
        self.assertTrue(
            os.path.exists("rental.db"),
            "rental.db file is missing"
        )

    def test_can_connect_and_list_tables(self):
        """
        Check that:
        - we can connect to the database
        - the database contains at least one table
        - the 'rentals' table exists
        """
        # Open connection using context manager
        with sqlite3.connect("rental.db") as conn:
            cur = conn.cursor()

            # Get all table names
            cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = [row[0] for row in cur.fetchall()]

        # Assert there is at least one table
        self.assertTrue(
            len(tables) > 0,
            "No tables found in the database"
        )

        # Assert the expected 'rentals' table exists
        self.assertIn(
            "rentals",
            tables,
            "'rentals' table not found in the database"
        )
