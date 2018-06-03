#!/usr/bin/env python
#
# Show credentials if any

file=open('.credentials')

user = ""
passwd = ""

for line in file:
  if line.startswith('username'):
    user = line.split()[-1]
  if line.startswith('password'):
    passwd = line.split()[-1]

if user and passwd:
  print "User:", user, "has password:", passwd
