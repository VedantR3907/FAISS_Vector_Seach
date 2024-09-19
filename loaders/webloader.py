from llama_index.readers.web import MainContentExtractorReader

loader = MainContentExtractorReader()
documents = loader.load_data(urls=["https://docs.llamaindex.ai/en/latest/understanding/loading/loading/"])

with open('./documents/text2.txt', 'w', encoding = 'utf8') as f:
    f.write(documents[0].text)


# from crawl4ai import WebCrawler

# # Create an instance of WebCrawler
# crawler = WebCrawler()

# # Warm up the crawler (load necessary models)
# crawler.warmup()

# # Run the crawler on a URL
# result = crawler.run(url="https://lilianweng.github.io/posts/2023-06-23-agent/")

# # Print the extracted content
# with open('./text.txt', 'w', encoding = 'utf8') as f:
#     f.write(result.markdown)