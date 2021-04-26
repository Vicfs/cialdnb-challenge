# Cialdnb Case

My proposed solution for the challenge sent to me during the application process for a position within RGR Tecnologia/CIAL d&b.

## Usage

Make sure you have Python 3.6 or newer installed.

```shell
$ pip install -r requirements.txt
```

### Running the code

The input must be provided via stdin, one per line.

```shell
# Prints the json to stdout
$ cat websites.txt | python -m main
```

## Running via docker

```shell
# Build image
$ docker build -t cialdnb_challenge .

# Run container, redirecting stdout output to local file
$ cat websites.txt | docker run -i cialdnb_challenge > output.json
```

## Proposed solution

This was my first attempt at `Scrapy`, I am more versed in `Selenium` and `BeautifulSoup`.
Nevertheless, I found Scrapy to be a really powerful and robust framework.
In my opinion, its strengths lie within the amount of builtin tools it provides allied to its simplicity.

I encountered some problems scraping websites that have an antibot system in place.
Some solutions I tried include rotating user agents, disabling cookies, changing headers, pausing requests and rotating proxies to no avail.
Since I was time constrained(did the project over half the weekend), I left it as it is, but would most likely solve the problem with a little more time.
I also forwent writing unit tests, for the same reason(time) listed above.

This project works on a single Spider that crawls concurrently(limited to 300 global requests and 10 requests per domain) a list of websites input via stdin.
First, the Spider grabs a list of phones found on the page via regex, then it saves the website logo, which is found via xpath by the keyword "logo" inside `@src` and `@class` tags(case insensitive, using xpath's `translate` feature).
After this, the results are output do stdout in `.json` format.
All in all, this was a pretty fun challenge and I was impressed with how well `Scrapy` performs.
