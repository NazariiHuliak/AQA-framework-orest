from seleniumbase import Driver
from .parser import FeatureParser
from .context import Context
from .dsl import registry

import steps.sorting_steps
import steps.search_steps
import steps.common_steps
import steps.lang_change_steps

class BDDRunner:
    def run_feature(self, fname):
        p = FeatureParser()
        steps = p.parse(fname)

        ctx = Context()
        ctx.driver = Driver(browser="chrome", headless=True, uc=True)

        for t, txt in steps:
            func, args = registry.match(t, txt)
            func(ctx, *args)

        ctx.driver.quit()
