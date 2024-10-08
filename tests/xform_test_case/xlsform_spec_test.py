# -*- coding: utf-8 -*-
"""
Some tests for the new (v0.9) spec is properly implemented.
"""
import codecs
import os
import unittest

import pyxform
from pyxform.errors import PyXFormError
from tests import example_xls, test_expected_output
from tests.xform_test_case.base import XFormTestCase


class MainTest(XFormTestCase):
    maxDiff = None

    def runTest(self):
        filename = "xlsform_spec_test.xlsx"
        self.get_file_path(filename)
        expected_output_path = os.path.join(
            test_expected_output.PATH, self.root_filename + ".xml"
        )

        # Do the conversion:
        warnings = []
        json_survey = pyxform.xls2json.parse_file_to_json(
            self.path_to_excel_file, default_name="xlsform_spec_test", warnings=warnings
        )
        survey = pyxform.create_survey_element_from_dict(json_survey)
        survey.print_xform_to_file(self.output_path, warnings=warnings)
        # print warnings
        # Compare with the expected output:
        with codecs.open(expected_output_path, "rb", encoding="utf-8") as expected_file:
            with codecs.open(self.output_path, "rb", encoding="utf-8") as actual_file:
                self.assertXFormEqual(expected_file.read(), actual_file.read())


class FlatXlsformTest(XFormTestCase):
    maxDiff = None

    def runTest(self):
        filename = "flat_xlsform_test.xlsx"
        self.get_file_path(filename)
        expected_output_path = os.path.join(
            test_expected_output.PATH, self.root_filename + ".xml"
        )

        # Do the conversion:
        warnings = []
        json_survey = pyxform.xls2json.parse_file_to_json(
            self.path_to_excel_file, default_name="flat_xlsform_test", warnings=warnings
        )
        survey = pyxform.create_survey_element_from_dict(json_survey)
        survey.print_xform_to_file(self.output_path, warnings=warnings)
        # print warnings
        # Compare with the expected output:
        with codecs.open(expected_output_path, "rb", encoding="utf-8") as expected_file:
            with codecs.open(self.output_path, "rb", encoding="utf-8") as actual_file:
                self.assertXFormEqual(expected_file.read(), actual_file.read())


class TestNewWidgets(XFormTestCase):
    maxDiff = None

    def runTest(self):
        filename = "widgets.xls"
        self.get_file_path(filename)
        expected_output_path = os.path.join(
            test_expected_output.PATH, self.root_filename + ".xml"
        )

        # Do the conversion:
        warnings = []
        json_survey = pyxform.xls2json.parse_file_to_json(
            self.path_to_excel_file, default_name="widgets", warnings=warnings
        )
        survey = pyxform.create_survey_element_from_dict(json_survey)
        survey.print_xform_to_file(self.output_path, warnings=warnings)
        # print warnings
        # Compare with the expected output:
        with codecs.open(expected_output_path, "rb", encoding="utf-8") as expected_file:
            with codecs.open(self.output_path, "rb", encoding="utf-8") as actual_file:
                self.assertXFormEqual(expected_file.read(), actual_file.read())


class CalculateWithoutCalculationTest(unittest.TestCase):
    """
    Just checks that calculate field without calculation raises a PyXFormError.
    """

    def runTest(self):
        filename = "calculate_without_calculation.xls"
        path_to_excel_file = os.path.join(example_xls.PATH, filename)
        self.assertRaises(
            PyXFormError, pyxform.xls2json.parse_file_to_json, path_to_excel_file
        )


class PullDataTest(XFormTestCase):
    maxDiff = None

    def runTest(self):
        filename = "pull_data.xlsx"
        self.get_file_path(filename)
        expected_output_path = os.path.join(
            test_expected_output.PATH, self.root_filename + ".xml"
        )

        # Do the conversion:
        warnings = []
        json_survey = pyxform.xls2json.parse_file_to_json(
            self.path_to_excel_file, default_name="pull_data", warnings=warnings
        )
        survey = pyxform.create_survey_element_from_dict(json_survey)
        survey.print_xform_to_file(self.output_path, warnings=warnings)

        # Compare with the expected output:
        with codecs.open(expected_output_path, "rb", encoding="utf-8") as expected_file:
            with codecs.open(self.output_path, "rb", encoding="utf-8") as actual_file:
                self.assertXFormEqual(expected_file.read(), actual_file.read())

        # cleanup
        os.remove(self.output_path)


class SeachAndSelectTest(XFormTestCase):
    maxDiff = None

    def runTest(self):
        filename = "search_and_select.xlsx"
        self.get_file_path(filename)
        expected_output_path = os.path.join(
            test_expected_output.PATH, self.root_filename + ".xml"
        )

        # Do the conversion:
        warnings = []
        json_survey = pyxform.xls2json.parse_file_to_json(
            self.path_to_excel_file, default_name="search_and_select", warnings=warnings
        )
        survey = pyxform.create_survey_element_from_dict(json_survey)
        survey.print_xform_to_file(self.output_path, warnings=warnings)

        # Compare with the expected output:
        with codecs.open(expected_output_path, "rb", encoding="utf-8") as expected_file:
            with codecs.open(self.output_path, "rb", encoding="utf-8") as actual_file:
                self.assertXFormEqual(expected_file.read(), actual_file.read())

        # cleanup
        os.remove(self.output_path)


class DefaultSurveySheetTest(XFormTestCase):
    maxDiff = None

    def runTest(self):
        filename = "survey_no_name.xlsx"
        self.get_file_path(filename)
        expected_output_path = os.path.join(
            test_expected_output.PATH, self.root_filename + ".xml"
        )

        warnings = []
        json_survey = pyxform.xls2json.parse_file_to_json(
            self.path_to_excel_file, warnings=warnings
        )
        survey = pyxform.create_survey_element_from_dict(json_survey)
        survey.print_xform_to_file(self.output_path, warnings=warnings)

        with codecs.open(expected_output_path, "rb", encoding="utf-8") as expected_file:
            with codecs.open(self.output_path, "rb", encoding="utf-8") as actual_file:
                self.assertXFormEqual(expected_file.read(), actual_file.read())


if __name__ == "__main__":
    unittest.main()
