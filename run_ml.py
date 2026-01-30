import sys
import traceback
from pathlib import Path

log_file = Path("run_log.txt")

try:
    with log_file.open("w", encoding="utf-8") as log:
        log.write("Starting titanicml.py execution...\n")
        log.flush()
        
        # Redirect stdout and stderr to capture all output
        import io
        output_capture = io.StringIO()
        
        # Run the main script
        with open("titanicml.py", "r", encoding="utf-8") as f:
            code = f.read()
        
        exec(code)
        
        log.write("\n\nScript completed successfully!\n")
        
except Exception as e:
    with log_file.open("a", encoding="utf-8") as log:
        log.write("\n\nERROR OCCURRED:\n")
        log.write(str(e))
        log.write("\n\nFull traceback:\n")
        log.write(traceback.format_exc())
    print(f"Error occurred! Check {log_file} for details")
    sys.exit(1)

print(f"Check {log_file} for execution details")
