import sys
import re
from datetime import datetime

class AbendAnalyzer:
    def __init__(self, spool_log_path):
        self.spool_log_path = spool_log_path

    def parse_abend_code(self):
        print(f"[{datetime.now()}] Analyzing log: {self.spool_log_path}")
        sample_log_content = '''
        IEA995I SYMPTOM DUMP OUTPUT  
        SYSTEM COMPLETION CODE=0C4  REASON CODE=00000004
        FAILED INSTRUCTION = 58202014
        '''
        match = re.search(r"SYSTEM COMPLETION CODE=([0-9A-F]+)\s+REASON CODE=([0-9A-F]+)", sample_log_content)
        if match:
            self._diagnose_code(match.group(1), match.group(2))

    def _diagnose_code(self, abend_code, reason_code):
        kb = {
            "0C4": "Protection Exception (Segmentation Fault / Invalid memory address).",
            "322": "Maximum CPU time exceeded for job step.",
            "S806": "Load module could not be found."
        }
        print(f"Abend Code: S{abend_code} | Explanation: {kb.get(abend_code, 'Unknown')}")

if __name__ == "__main__":
    AbendAnalyzer("logs/spool_sample.log").parse_abend_code()