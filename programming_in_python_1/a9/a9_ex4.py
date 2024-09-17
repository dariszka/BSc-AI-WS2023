import subprocess
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-p", "--program", type=str, required=True, help="name of the program to be executed")
parser.add_argument("-a", "--args", type=str, nargs='+', default=[], help="arguments to be passed to the program")
parser.add_argument("-t", "--timeout", type=float, default=60, help="timeout in seconds for the execution of the program")

args = parser.parse_args()

program = args.program
arguments = args.args
timeout = int(args.timeout) #this is so that the program outputs match the example outputs we were given, when it was specified that we should get timeout as a float
                            #otherwise it would just be
                            #timeout = args.timeout

try:
        if len(arguments) == 0:
            print(f"Running program '{program}' without any arguments with a {timeout}s timeout")
            p = subprocess.Popen([program], stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
        else:
            print(f"Running program '{program}' with arguments {arguments} with a {timeout}s timeout")
            p = subprocess.Popen([program] + arguments, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')

        try:
            outs, errs = p.communicate(timeout=timeout)
            print(f"The '{program}' finished with exit code {p.returncode}")

            if outs:
                print(f"The '{program}' produced the following standard output:\n{outs}")
            if errs:
                print(f"The '{program}' produced the following error output:\n{errs}")

        except subprocess.TimeoutExpired:
            p.kill()
            print("The program execution timed out")

except FileNotFoundError:
    print(f"The specified program '{program}' could not be found")



