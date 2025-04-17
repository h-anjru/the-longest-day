# What is the longest day?
This is a little script to determine the longest alphabetical dates between the years 1 CE to 10000 CE. The format I chose for the alphabetical dates is the way in which one may reasonably say or write a date in natural language, for example:

> Wednesday, the twenty-sixth of March, year two thousand twenty-five

From a previous exercise, I knew that the longest possible date would be a Wednesday, the twenty-seventh of September, in a year comprised of the digits 3, 7, and 8, and whose tens place was seventy. Initially, I wrote this script simply to find if there was such a year in which there was a Wednesday, 27 September. I found three such instances:

- Wednesday, the twenty-seventh of September, year eight thousand three hundred seventy-eight
- Wednesday, the twenty-seventh of September, year eight thousand seven hundred seventy-eight
- Wednesday, the twenty-seventh of September, year eight thousand eight hundred seventy-three

While the first instance of this 91-character date occurs in 8378, I suppose the title of longest day ever (at least until the year 10000 CE) should go to the final instance in 8873. The Earth's rotation about its axis is slowing, so by the time we make it to 8873, the average day will be longer than the average day in 8378.

*There is secular noise in the length of a day, but it trends downward as the Earth marches toward tidal lock with the Sun, where one hemisphere of the Earth is always facing sunward—much like the Moon's tidal lock with the Earth. One good wobble and 27 Sep 8873 could the longest day ever, in more ways than one—that is, until Thursday, the twenty-eighth of September, year eight thousand eight hundred seventy-tree (which at 89 characters is tied for the third longest length of date string, and tied for 61st place overall among all dates from 1 to 10000 CE).*

## Other notes
### Year formatting
I do not use "and" in between the hundreds and tens place. This is most common in the United States. Example: 2125 is "two thousand one hundred twenty-five." That is the best way to write such a number, and I don't care about your opinion on the matter.

I added the word "year" in the final string both for clarity and to ease the awkwardness of writing out dates such as "...the fifteenth of March, two." This choice does not affect the ranking of the length of the dates, as they all contain those characters.

I was on the fence about whether to format years in the more common manner of speaking, e.g. "twenty twenty-five" instead of "two thousand twenty-five," but...I dunno, just decided not to.

### Ordinals
What does affect their ranking, however, is my choice to use ordinal numbers for the days of the month (e.g. "first" instead of "one"). While speaking or writing with ordinals is a more natural way of stating the date, it does affect the length of a written date. For example, "seven" and "eight" are both five characters long, but "seventh" is one character longer than "eighth."

I am OK with many instances of these ordinal differences, if only because they serve as a tiebreaker of sorts. From my previous example, since "seven" has two syllables and "eight" only one, I prefer to consider "seven" the longer word. I did not check all instances of this exhaustively, however, as I was only concerned with the longest possible alphabetically written dates, which I had already figured to be a Wednesday, the 27th of September.

### Order of date elements
"`DAY OF WEEK`, `DATE` of `MONTH`, year `YEAR`" progresses from smallest to largest duration. That's not how everyone says it, but I do like the logic of that form. Other arrangements would likely yield similar results.

Other orderings, such as year-month-date-day of week, would have obviated the need to use ordinals for the date, but that's just not how people tend to talk. I have met very few people who say, for instance, "today is May fourteen" or "today is twenty twenty-five March twenty-seven, a Thursday."