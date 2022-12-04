from scrapy import Request, Spider

from AmazonCommentsSpider.items import CommentItem


class CommentSpider(Spider):

    name = "CommentSpider"

    with open("target.txt", mode="rt") as f:
        start_urls: list[str] = f.readlines()

    @staticmethod
    def slice_content(tag: str | None) -> str:
        if tag is None:
            return ""
        text = tag[tag.find(">") + 1 : tag.rfind("<")]
        return text

    @staticmethod
    def get_rate(text: str) -> float:
        rate = text[: text.find(" ")]
        return float(rate)

    def parse(self, response):  # type: ignore
        name: str = self.slice_content(
            response.css(
                ".a-unordered-list > li:nth-child(1) > span:nth-child(1) > a:nth-child(1)"
            ).get()
        )
        for review in response.css("div[id^=customer_review]"):
            rate_str: str | None = self.slice_content(review.css(".a-icon-alt").get())
            if rate_str is None:
                yield

            rate: float = self.get_rate(rate_str)

            item = CommentItem(
                friendly_name=name,
                user_name=self.slice_content(review.css(".a-profile-name").get()),
                rate=rate,
                comment=self.slice_content(
                    review.css("span[data-hook=review-body] span").get()
                ),
            )
            yield item

        next_page: None | str = response.css('li[class=a-last] a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
