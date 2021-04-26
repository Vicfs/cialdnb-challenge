# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json

from itemadapter import ItemAdapter


class CialdnbPipeline:
    async def process_item(self, item, spider):
        # Print item to stdout
        print(json.dumps(item))

        # Write items to json
        with open("output.json", "a") as out_file:
            print(json.dumps(item), file=out_file)
        return item
