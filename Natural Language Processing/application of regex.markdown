Well, anywhere you need to check if a string matches a certain pattern and maybe extract certain information from that pattern.

For example:

    In websites where users are required to enter their email address you can validate the field using a regular expression that matches the structure of an email address.
    Like above but not necessarily restricted to emails. There are other type of data that need some structure validation, maybe a VAT number or social security number.
    When you need to parse some text and need to extract certain information that follows a known format, such as dates. A regex like (\d{4})-(\d{2})-(\d{2}) could match dates in the yyyy-mm-dd format and extract the year, month and day into different variables.
    They can be used in many other text related tasks. Extract links from html pages, strip html tags, replace tabs by spaces, compact whitespace, etc.
    They can be used to match URLs. For example both mypage.com/something/foo.html and  mypage.com/otherthing/bar.xml can be matched by the same regular expression. Web frameworks let you define your routes using regular expressions or an ad-hoc format that still uses a regex under the hood.
