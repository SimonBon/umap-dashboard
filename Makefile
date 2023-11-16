# Define the default message
m ?= project update

# Define the package name
PACKAGE_NAME = your_package_name

# Define the commit target
commit:
	git add .
	git commit -m "$(m)"
	git push