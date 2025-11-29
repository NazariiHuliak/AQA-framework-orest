from .step_registry import StepRegistry

registry = StepRegistry()

def given(pattern):
    def decorator(func):
        registry.register("GIVEN", pattern, func)
        return func
    return decorator

def when(pattern):
    def decorator(func):
        registry.register("WHEN", pattern, func)
        return func
    return decorator

def then(pattern):
    def decorator(func):
        registry.register("THEN", pattern, func)
        return func
    return decorator
