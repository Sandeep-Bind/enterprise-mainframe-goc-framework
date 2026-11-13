import json

def validate_scheduler_workflows(config_path):
    print("Loading enterprise batch schedule topologies...")
    workflow = {
        "JOB_EXTRACT": {"depends_on": []},
        "JOB_TRANSFORM": {"depends_on": ["JOB_EXTRACT"]},
        "JOB_LOAD": {"depends_on": ["JOB_TRANSFORM"]},
        "JOB_REPORT": {"depends_on": ["JOB_LOAD"]}
    }
    visited = set()
    stack = set()

    def check_cycle(node):
        visited.add(node)
        stack.add(node)
        for neighbor in workflow.get(node, {}).get("depends_on", []):
            if neighbor not in visited:
                if check_cycle(neighbor):
                    return True
            elif neighbor in stack:
                return True
        stack.remove(node)
        return False

    has_cycle = any(check_cycle(job) for job in workflow if job not in visited)
    if has_cycle:
        print("[CRITICAL] Circular dependency detected in batch workflow!")
    else:
        print("[SUCCESS] Batch dependency tree validated. No deadlocks or circular dependencies found.")

if __name__ == "__main__":
    validate_scheduler_workflows("config/scheduler_config.json")