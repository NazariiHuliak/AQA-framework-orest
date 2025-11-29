from framework.runner import BDDRunner
import pytest
import glob

runner = BDDRunner()
feature_files = glob.glob("*.feature")

@pytest.mark.parametrize("feature_file", feature_files)
def test_feature(feature_file):
    runner = BDDRunner()
    runner.run_feature(feature_file)
