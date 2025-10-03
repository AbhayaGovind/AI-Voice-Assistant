import subprocess

PROJECT_DIR = "src"  # change if your source folder is different


def run(command: str):
    """Run a shell command and print output."""
    print(f"\n🔹 {command}\n")
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print("⚠️", result.stderr)


if __name__ == "__main__":
    import sys

    # Check if user wants to apply fixes or just analyze
    apply_fixes = "--fix" in sys.argv or "--apply" in sys.argv

    if apply_fixes:
        print("🚀 Fixing project issues (files will be modified)...\n")

        # 1. Remove unused imports & variables (APPLIES CHANGES)
        run(
            f"autoflake --remove-all-unused-imports --remove-unused-variables --recursive --in-place {PROJECT_DIR}"
        )

        # 2. Fix import ordering (APPLIES CHANGES)
        run(f"isort {PROJECT_DIR}")

        # 3. Format code (APPLIES CHANGES)
        run(f"black {PROJECT_DIR}")

        # 4. Complexity report (informational only)
        run(f"radon cc -s -a {PROJECT_DIR}")

        print("\n✅ All fixes applied! Source files have been modified.")
    else:
        print("🚀 Analyzing project without modifying source files...\n")
        print("💡 Run with --fix or --apply to actually modify files\n")

        # 1. Show unused imports & variables (dry-run)
        run(
            f"autoflake --remove-all-unused-imports --remove-unused-variables --recursive --check {PROJECT_DIR}"
        )

        # 2. Show import ordering issues (dry-run)
        run(f"isort {PROJECT_DIR} --check-only")

        # 3. Show formatting issues (dry-run)
        run(f"black {PROJECT_DIR} --check")

        # 4. Complexity report
        run(f"radon cc -s -a {PROJECT_DIR}")

        print("\n✅ Analysis complete. Source files unchanged.")
