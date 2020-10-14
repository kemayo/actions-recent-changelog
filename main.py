#!/usr/bin/env python

import sys
import os.path

def main(full_changelog, output):
	if not os.path.isfile(full_changelog):
		sys.exit("Input file doesn't exist")
	with open(full_changelog, 'r') as f, open(output, 'w') as out:
		matching = False
		for line in f:
			if line.startswith('##') and not line.startswith('###'):
				if matching:
					print("Wrote changelog to", output)
					return
				matching = True
			if matching:
				out.write(line)
	sys.exit("Couldn't write changelog")

if __name__ == '__main__':
	main(sys.argv[1], sys.argv[2])
