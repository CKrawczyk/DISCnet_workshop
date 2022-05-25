cd docs
sphinx-apidoc -MEf -o ./source ../data_transforms ../data_transforms/tests
make clean
make html
cd ..
