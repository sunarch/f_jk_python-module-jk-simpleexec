#!/usr/bin/python3




import jk_simpleexec




cmdResult = jk_simpleexec.invokeCmd1(
	cmdPath = "/usr/bin/ls",
	cmdArgs = [
		"-la",
	],
	dataToPipeAsStdIn = None,							# this is the default
	workingDirectory = "/",
)

cmdResult.dump()










