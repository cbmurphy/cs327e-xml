diff:
	RunXML.py < RunXML.in &> RunXML.tmp
	diff RunXML.out RunXML.tmp
	rm RunXML.tmp

doc:
	pydoc -w XML

log:
	git log > XML.log

test:
	python TestXML.py &> TestXML.out

turnin-list:
	turnin --list hychyc07 cs327epj2

turnin-submit:
	turnin --submit hychyc07 cs327epj2 XML.zip

turnin-verify:
	turnin --verify hychyc07 cs327epj2

turnin:
	make log
	make doc
	make zip
	make turnin-submit
	make turnin-list
	cd ..
	make turnin-verify
	make clean

zip:
	zip -r XML.zip makefile README.txt XML.html XML.log XML.py \
	RunXML.in RunXML.out RunXML.py SphereXML.py \
	TestXML.py TestXML.out 

clean:
	rm -f *.pyc
	rm -f *.tmp
