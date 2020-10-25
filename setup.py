from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
	name='pytyper',
	version='0.1.2',
	author='Greyson Murray',
	author_email='greysonmurray.dev@gmail.com',
	description='Typing statistics calculations, string comparison, and formatting',
	long_description=long_description,
	long_description_content_type="text/markdown",
	url='https://github.com/greysonDEV/pytyper',
	license='MIT',
	classifiers=[
		"License :: OSI Approved :: MIT License",
		"Programming Language :: Python :: 3.8",
		"Topic :: Games/Entertainment",
		"Operating System :: MacOS",
		"Intended Audience :: Developers",
		"Intended Audience :: Education",
		"Natural Language :: English"
	],
	include_package_data=True,
	python_requires='>=3.8',
	packages=['pytyper'],
	zip_safe=False
	)