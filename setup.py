import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(name='personal_assistant',
                 version='0.0.1',
                 author='Yaroslav Maniukh, Valeriy Topchiy, Polina Yarova',
                 author_email='manyukhy@gmail.com, wellkswell@gmail.com, polinaya777@gmail.com',
                 description='Console script for working with Contacts lists, Notes and sorting files in the folders',
                 long_description=long_description,
                 long_description_content_type="text/markdown",
                 url='https://github.com/Personal-Assistant-Project/ProjectHelper',
                 keywords="personal assistant helper",
                 license='MIT',
                 classifiers=[
                     "Programming Language :: Python :: 3",
                     "License :: OSI Approved :: MIT License",
                     "Operating System :: OS Independent",
                 ],
                 entry_points={'console_scripts': [
                     'helper-folder = ProjectHelper.main:main']},
                 packages=setuptools.find_packages(where="ProjectHelper"),
                 include_package_data=True,
                 python_requires=">=3.6",
                 )
