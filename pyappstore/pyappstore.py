#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

# http://chase-seibert.github.io/blog/2014/03/21/python-multilevel-argparse.html

import argparse
import os
import sys

from Foundation import NSAppleScript


def sign_out():
    path = os.path.join(os.path.dirname(__file__), 'sign_out.scpt')
    with open(path, "r") as script:
        install = NSAppleScript.alloc().initWithSource_(script.read())
        result, err_info = install.executeAndReturnError_(None)
        print err_info


def sign_in():
    parser = argparse.ArgumentParser()
    parser.add_argument('--username', help='username')
    parser.add_argument('--password', help='password')
    args = parser.parse_args(sys.argv[2:])

    path = os.path.join(os.path.dirname(__file__), 'sign_in.scpt')
    with open(path, "r") as script:
        txt = script.read()
        txt = txt.replace("item 1 of argv", '"' + args.username + '"')
        txt = txt.replace("item 2 of argv", '"' + args.password + '"')
        install = NSAppleScript.alloc().initWithSource_(txt)
        result, err_info = install.executeAndReturnError_(None)
        print err_info
    result, err_info = install.executeAndReturnError_(None)
    print err_info


def install():
    parser = argparse.ArgumentParser()
    parser.add_argument('app', help='app')
    parser.add_argument('--company', help='company')
    args = parser.parse_args(sys.argv[2:])

    # open location "macappstore://itunes.apple.com/app/id%d?mt=12"
    url = ("macappstore://" +
           "search.itunes.apple.com" +
           "/WebObjects/MZContentLink.woa/wa/link?mt=12&path=mac")
    if args.company:
        url += "%2f" + args.company
    url += "%2f" + args.app
    print url
    install = NSAppleScript.alloc().initWithSource_('''
    tell application "System Events" to tell process "App Store"
        set frontmost to true
        --delay 5
        open location "%s"
        --keystroke "f" using command down
        --keystroke "1Password" & return
        delay 5
        set bButton to button 1 of group 1 of group 1 of UI element 1 of scroll area 1 of group 1 of group 1 of window 1
        set bDescription to description of bButton
        log bDescription

        if bDescription starts with "Install" then
            click bButton
            delay 1
            repeat until description of bButton starts with "Open"
                delay 1
            end repeat
        end if
    end tell''' % url)
    result, err_info = install.executeAndReturnError_(None)
    print err_info


def _main():
    parser = argparse.ArgumentParser(description='Install from the App Store')
    parser.add_argument('command', help='command to run')
    args = parser.parse_args(sys.argv[1:2])

    if args.command == 'sign_in':
        print 'sign_in'
        sign_in()
    elif args.command == 'sign_out':
        print 'sign_out'
        sign_out()
    elif args.command == 'install':
        print 'install'
        install()

if __name__ == '__main__':
    _main()
