# -*- coding: utf-8 -*-

"""Tests for `twodolib` module."""
from __future__ import print_function, unicode_literals
import unittest
import sys

import twodolib
from twodolib import TwoDoTask

PY3 = sys.version_info > (3,)
if PY3:
    # noinspection PyUnresolvedReferences
    from urllib.parse import quote
else:
    from urllib import quote


class TestShowUrls(unittest.TestCase):
    """Test the 4 urls to show several lists in 2Do App."""

    def test_showall_url(self):
        """URL showall is correct."""
        expected_url = 'twodo://x-callback-url/showAll'
        self.assertEqual(twodolib.showall_url, expected_url)

    def test_showtoday_url(self):
        """URL showtoday is correct."""
        expected_url = 'twodo://x-callback-url/showToday'
        self.assertEqual(twodolib.showtoday_url, expected_url)

    def test_showstarred_url(self):
        """URL showstarred is correct."""
        expected_url = 'twodo://x-callback-url/showStarred'
        self.assertEqual(twodolib.showstarred_url, expected_url)

    def test_showscheduled_url(self):
        """URL showscheduled is correct."""
        expected_url = 'twodo://x-callback-url/showScheduled'
        self.assertEqual(twodolib.showscheduled_url, expected_url)


class TestGetSimpleAddUrl(unittest.TestCase):
    """Test url for adding tasks to 2Do App."""

    def test_add_task_with_title_url(self):
        """Test adding a task only with a title."""
        task_title = 'Test title of the task.'
        quoted_title = quote(task_title)
        expected_url = 'twodo://x-callback-url/add?task=' + quoted_title
        self.assertEqual(twodolib.get_add_url(task_title), expected_url)


class TestTwoDoTaskClass(unittest.TestCase):
    """Test the creation and attributes of a TwoDoTask object."""

    def test_simple_task_with_title_only(self):
        """Create a simple task only by title."""
        title = 'A simple task by title'
        task = TwoDoTask(title)
        self.assertEqual(task.task, title)

    def test_default_values_of_simple_task(self):
        """Create a task by title and check the presence of attributes."""
        task = TwoDoTask('Save the world.')
        self.assertEqual(task.task, 'Save the world.')
        self.assertEqual(task.type, TwoDoTask.TASK_TYPE)
        self.assertIsNone(task.for_list)
        self.assertIsNone(task.forParentTask)
        self.assertIsNone(task.note)
        self.assertEqual(task.priority, '0')
        self.assertEqual(task.starred, '0')
        self.assertIsNone(task.tags)
        self.assertIsNone(task.due)
        self.assertIsNone(task.dueTime)
        self.assertIsNone(task.start)
        self.assertIsNone(task.repeat)
        self.assertIsNone(task.action)
        self.assertEqual(task.ignoreDefaults, '0')


class TestGeneratedUrlsOfTwoDoTask(unittest.TestCase):
    """Test several URLs, which are generated by a TwoDoTask object."""

    def test_simple_task_url_is_correct(self):
        """The URL for a simple task is correct."""
        task_title = 'Test title of the task.'
        quoted_title = quote(task_title)
        expected_url = 'twodo://x-callback-url/add?task=' + quoted_title
        task = TwoDoTask(task_title)
        self.assertEqual(task.url(), expected_url)

    def test_project_task_url_is_correct(self):
        """The URL for a project task is correct."""
        task_title = 'Test title of the task.'
        quoted_title = quote(task_title)
        expected_url = 'twodo://x-callback-url/add?task=' + quoted_title
        expected_url += '&type=1'
        task = TwoDoTask(task_title, task_type='1')
        self.assertEqual(task.url(), expected_url)

    def test_task_for_a_list_url_is_correct(self):
        """The URL for a task for a list is correct."""
        task_title = 'Test title of the task.'
        quoted_title = quote(task_title)
        task_list = 'urgent errands'
        quoted_list = quote(task_list)
        expected_url = 'twodo://x-callback-url/add?task=' + quoted_title
        expected_url += '&for_list={}'.format(quoted_list)
        task = TwoDoTask(task_title, for_list=task_list)
        self.assertEqual(task.url(), expected_url)

    def test_task_with_a_note_url_is_correct(self):
        """The URL for a task with a note is correct."""
        task_title = 'Test title of the task.'
        quoted_title = quote(task_title)
        task_note = "A little note to this important task."
        quoted_note = quote(task_note)
        expected_url = 'twodo://x-callback-url/add?task=' + quoted_title
        expected_url += '&note={}'.format(quoted_note)
        task = TwoDoTask(task_title, note=task_note)
        self.assertEqual(task.url(), expected_url)

    def test_task_with_prio_url_is_correct(self):
        """The URL for a task with a priority is correct."""
        task_title = 'Test title of the task.'
        quoted_title = quote(task_title)
        expected_url = 'twodo://x-callback-url/add?task=' + quoted_title
        expected_url += '&priority=3'
        task = TwoDoTask(task_title, priority=3)
        self.assertEqual(task.url(), expected_url)

    def test_starred_task_url_is_correct_boolean(self):
        """The URL for a starred task is correct."""
        task_title = 'Test title of the task.'
        quoted_title = quote(task_title)
        expected_url = 'twodo://x-callback-url/add?task=' + quoted_title
        expected_url += '&starred=1'
        task = TwoDoTask(task_title, starred=True)
        self.assertEqual(task.url(), expected_url)

    def test_starred_task_url_is_correct_one(self):
        """The URL for a starred task is correct."""
        task_title = 'Test title of the task.'
        quoted_title = quote(task_title)
        expected_url = 'twodo://x-callback-url/add?task=' + quoted_title
        expected_url += '&starred=1'
        task = TwoDoTask(task_title, starred=True)
        self.assertEqual(task.url(), expected_url)

    def test_task_with_tags_url_is_correct(self):
        """The URL for a task with some tags is correct."""
        task_title = 'Test title of the task.'
        quoted_title = quote(task_title)
        task_tags = "business,important,customer"
        quoted_tags = quote(task_tags)
        expected_url = 'twodo://x-callback-url/add?task=' + quoted_title
        expected_url += '&tags={}'.format(quoted_tags)
        task = TwoDoTask(task_title, tags=task_tags)
        self.assertEqual(task.url(), expected_url)

    def test_task_with_iso_duedate_url_is_correct(self):
        """The URL for a task with a iso formatted due date is correct."""
        task_title = 'Test title of the task.'
        quoted_title = quote(task_title)
        task_due = "2015-10-02"
        quoted_due = quote(task_due)
        expected_url = 'twodo://x-callback-url/add?task=' + quoted_title
        expected_url += '&due={}'.format(quoted_due)
        task = TwoDoTask(task_title, due=task_due)
        self.assertEqual(task.url(), expected_url)

    def test_task_with_rel_duedate_url_is_correct(self):
        """The URL for a task with a relative due date is correct."""
        task_title = 'Test title of the task.'
        quoted_title = quote(task_title)
        expected_url = 'twodo://x-callback-url/add?task=' + quoted_title
        expected_url += '&due=7'
        task = TwoDoTask(task_title, due='7')
        self.assertEqual(task.url(), expected_url)

    def test_task_with_duetime_url_is_correct(self):
        """The URL for a task with a due time is correct."""
        task_title = 'Test title of the task.'
        quoted_title = quote(task_title)
        task_duetime = "12:00"
        quoted_duetime = quote(task_duetime)
        expected_url = 'twodo://x-callback-url/add?task=' + quoted_title
        expected_url += '&dueTime={}'.format(quoted_duetime)
        task = TwoDoTask(task_title, dueTime=task_duetime)
        self.assertEqual(task.url(), expected_url)

    def test_task_with_start_time_url_is_correct(self):
        """The URL for a task with a start time ist correct."""
        task_title = 'Test title of the task.'
        quoted_title = quote(task_title)
        task_start = "2015-10-01 12:00"
        quoted_start = quote(task_start)
        expected_url = 'twodo://x-callback-url/add?task=' + quoted_title
        expected_url += '&start={}'.format(quoted_start)
        task = TwoDoTask(task_title, start=task_start)
        self.assertEqual(task.url(), expected_url)

    def test_task_with_rel_start_time_url_is_correct(self):
        """The URL for a task with a relative start date ist correct."""
        task_title = 'Test title of the task.'
        quoted_title = quote(task_title)
        task_start = "14"
        quoted_start = quote(task_start)
        expected_url = 'twodo://x-callback-url/add?task=' + quoted_title
        expected_url += '&start={}'.format(quoted_start)
        task = TwoDoTask(task_title, start=task_start)
        self.assertEqual(task.url(), expected_url)

    def test_task_with_daily_repeat_url_is_correct(self):
        """The URL for a task with daily repetition is correct."""
        task_title = 'Test title of the task.'
        quoted_title = quote(task_title)
        expected_url = 'twodo://x-callback-url/add?task=' + quoted_title
        expected_url += '&repeat={}'.format(TwoDoTask.DAILY)
        task = TwoDoTask(task_title, repeat='1')
        self.assertEqual(task.url(), expected_url)


class TestTwoDoTaskValidation(unittest.TestCase):
    """Test the validation of arguments, when creating a TwoDoTask object."""

    def test_task_with_title_length_of_zero_raises_valueerror(self):
        """Create a simple task without title raises ValueError."""
        title = ''
        self.assertRaises(ValueError, TwoDoTask, title)

    def test_task_with_title_is_none_raises_valueerror(self):
        """Create a simple task with None title raises ValueError."""
        title = None
        self.assertRaises(ValueError, TwoDoTask, title)

    def test_wrong_type_raises_valueerror(self):
        """Create Task with Type invalid Type raises ValueError."""
        self.assertRaises(ValueError, TwoDoTask, 'TestTask', task_type='4')

    def test_wrong_priority_raises_valueerror(self):
        """Create Task with Type invalid priority raises ValueError."""
        self.assertRaises(ValueError, TwoDoTask, 'TestTask', priority='4')

    def test_starred_true_returns_1_value(self):
        """A True starred will be represented as '1'."""
        task = TwoDoTask('TestTask', starred=True)
        self.assertEqual(task.starred, '1')

    def test_starred_1_returns_1_value(self):
        """A 1 starred will be represented as '1'."""
        task = TwoDoTask('TestTask', starred=1)
        self.assertEqual(task.starred, '1')

    def test_starred_str_1_returns_1_value(self):
        """A '1' starred will be represented as '1'."""
        task = TwoDoTask('TestTask', starred='1')
        self.assertEqual(task.starred, '1')

    def test_starred_false_returns_0_value(self):
        """A False starred will be represented as '0'."""
        task = TwoDoTask('TestTask', starred=False)
        self.assertEqual(task.starred, '0')

    def test_starred_0_returns_0_value(self):
        """A 0 starred will be represented as '0'."""
        task = TwoDoTask('TestTask', starred=0)
        self.assertEqual(task.starred, '0')

    def test_starred_str_0_returns_0_value(self):
        """A '0' starred will be represented as '0'."""
        task = TwoDoTask('TestTask', starred='0')
        self.assertEqual(task.starred, '0')

    def test_ignoredefaults_true_returns_1_value(self):
        """A True ignoreDefaults will be represented as '1'."""
        task = TwoDoTask('TestTask', ignoreDefaults=True)
        self.assertEqual(task.ignoreDefaults, '1')

    def test_ignoredefaults_1_returns_1_value(self):
        """A 1 ignoreDefaults will be represented as '1'."""
        task = TwoDoTask('TestTask', ignoreDefaults=1)
        self.assertEqual(task.ignoreDefaults, '1')

    def test_ignoredefaults_str_1_returns_1_value(self):
        """A '1' ignoreDefaults will be represented as '1'."""
        task = TwoDoTask('TestTask', ignoreDefaults='1')
        self.assertEqual(task.ignoreDefaults, '1')

    def test_ignoredefaults_false_returns_0_value(self):
        """A False ignoreDefaults will be represented as '0'."""
        task = TwoDoTask('TestTask', ignoreDefaults=False)
        self.assertEqual(task.ignoreDefaults, '0')

    def test_ignoredefaults_0_returns_0_value(self):
        """A 0 ignoreDefaults will be represented as '0'."""
        task = TwoDoTask('TestTask', ignoreDefaults=0)
        self.assertEqual(task.ignoreDefaults, '0')

    def test_ignoredefaults_str_0_returns_0_value(self):
        """A '0' ignoreDefaults will be represented as '0'."""
        task = TwoDoTask('TestTask', ignoreDefaults='0')
        self.assertEqual(task.ignoreDefaults, '0')

    def test_correct_due_date_format_will_be_accepted(self):
        """A correct date will be stored in the task."""
        task = TwoDoTask('TestTask', due='2015-10-15')
        self.assertEqual(task.due, '2015-10-15')

    def test_correct_due_format_will_be_accepted(self):
        """A correct date will be stored in the task."""
        task = TwoDoTask('TestTask', due='14')
        self.assertEqual(task.due, '14')

    def test_correct_due_int_format_will_be_accepted(self):
        """A correct date will be stored in the task."""
        task = TwoDoTask('TestTask', due=14)
        self.assertEqual(task.due, '14')

    def test_wrong_due_format_raises_valueerror(self):
        """A wrong date format in due date raises ValueError."""
        wrong_date = '2015-XX-10'
        self.assertRaises(ValueError, TwoDoTask, 'TestTask', due=wrong_date)
        wrong_date = '15.10.2015'
        self.assertRaises(ValueError, TwoDoTask, 'TestTask', due=wrong_date)
        wrong_date = '2015......'
        self.assertRaises(ValueError, TwoDoTask, 'TestTask', due=wrong_date)

    @unittest.skip('write this after test: title=None')
    def test_task_with_wrong_duetime_raises_valueerror(self):
        """Wrong formatted due time raises ValueError."""
        task_title = 'Test title of the task.'
        task_duetime = "8pm"
        self.assertRaises(ValueError, TwoDoTask, task_title,
                          dueTime=task_duetime)

    def test_wrong_repetition_raises_valueerror(self):
        """Wrong values for repetition raise ValueError."""
        self.assertRaises(ValueError, TwoDoTask, 'TestTask', repeat=0)
        self.assertRaises(ValueError, TwoDoTask, 'TestTask', repeat='5')
