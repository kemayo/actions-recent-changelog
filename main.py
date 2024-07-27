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
					return output
				matching = True
			if matching:
				out.write(line)
	if matching:
		# There was only one version in the changelog, so we hit the end of
		# the file while still matching
		return output
	sys.exit("Couldn't write changelog")

if __name__ == '__main__':
	output = main(sys.argv[1], sys.argv[2])
	print("Wrote changelog to", output)
