import sys,subprocess,os

def formatting_migrations(filename):
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        abs_dir = os.path.join(os.path.dirname(script_dir), filename)

        subprocess.run(
            [sys.executable, '-m', 'ruff', 'format', str(abs_dir), '--fix', '--line-length', '120'],
            check=True,
            capture_output=True,
        )
        print('success formatting')
    except subprocess.CalledProcessError as e:
        print('failed formatting')
if __name__ == '__main__':
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        formatting_migrations(filename)
    else:
        print('No filename given')