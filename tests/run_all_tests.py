from framework.runner import BDDRunner
import pytest
import glob
import os

runner = BDDRunner()

feature_dir = os.path.join(os.path.dirname(__file__), "features")
feature_files = glob.glob(os.path.join(feature_dir, "*.feature"))

if not feature_files:
    raise FileNotFoundError(f"No .feature files found in {feature_dir}")

@pytest.mark.parametrize(
    "feature_file",
    feature_files,
    ids=[os.path.basename(f) for f in feature_files]
)
def test_feature(feature_file):
    runner.run_feature(feature_file)
