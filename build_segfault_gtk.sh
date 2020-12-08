#!/bin/sh
export PATH="/usr/lib64/ccache:$PATH"

time python3 -m nuitka --unstripped --show-progress --plugin-enable=numpy --noinclude-scipy  --standalone --follow-imports  segfault_gtk.py 
cp numpy2pb.npy ./segfault_gtk.dist/ 

