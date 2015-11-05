#!/usr/bin/python
# -*- coding: utf8 -*-

import os, sys, traceback

usr, psw = os.getenv('LOGIN', 'user:pass').split(':')
print usr, psw
dbg = True
porn = True
url = 'http://zelka.org'

__resource__ = os.path.join(  os.getcwd(), 'resources', 'lib' )
sys.path.insert(0, __resource__)
from zelka import zelka

if __name__ == '__main__':
  if len(sys.argv) != 2:
    sys.exit('wrong argument')
  try:
    z = zelka(
                xxx=True,
                base_url=url,
                usr=usr,
                passwd=psw,
                path=os.path.join(os.getcwd(), '', 'tmp'),
                dbg=True)
    for i in z.index():
      print i

    for r in z.page(0, '0', sys.argv[1]):
      if r['path'] != 'next_page':
        print r['path']

  except Exception, e:
    traceback.print_exc()
    print '%s, %s' % (str(e.args[0]), sys.exc_info())
    pass
