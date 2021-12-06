#!/usr/bin/env python3

import os
import argparse
import modulesbuilder as mb

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("module", help="modulefile config", type=str)
    parser.add_argument("-p", "--prefix", default="/usr/local/Modules",
                        help="modules prefix, the path to mount point")
    parser.add_argument("-o", "--output-dir", default="modules",
                        help="build modules in output directory")
    parser.add_argument("-v", "--verbose",
                        help="increase output verbosity",
                        action="store_true")
    parser.add_argument("-f", "--force",
                        help="force rebuild of docker images",
                        action="store_true")
    parser.add_argument("--os", help="target os name", default="ubuntu")
    parser.add_argument("--os-vers", help="target os version", default="16.04")
    args = parser.parse_args()
    yamlFile = args.module
    modulePath = os.path.dirname(os.path.abspath(yamlFile))
    moduleDir = args.output_dir
    modulesPrefix = args.prefix
    verbosity = args.verbose
    force = args.force
    os_name = args.os
    os_vers = args.os_vers
    mb.build(config=yamlFile, path=moduleDir, prefix=modulesPrefix, verbose=verbosity, debug=False, force=force, target_os="%s:%s"%(os_name,os_vers))
