# Extension task - File converter

​

Create a file converter for converting JSON files to parquet format.

​

Parquet is a file format very commonly used in data lakes and your job is to research how to convert a JSON list and store the converted parquet files for later use. 

​

You'll then need to perform this process in a lambda function.

​

If you need any dependencies to do this conversion research how to include them in your lambda. 

​

You should create:

​

- An S3 raw data bucket that you can upload JSON files to.

- An S3 bucket to store the parquet files once they have been converted.

- A lambda function that is invoked whenever a JSON file is uploaded. It should convert the JSON file to parquet format and upload the results to the target bucket.

​

JSON uploads will be list of items sold in an online store. They will be of the form:

​

```json

[

  {

    "item_name": "1990s Gameboy",

    "description": "But mom I want one!",

    "price": 1599,

    "category_name": "Electronics"

  },

  {

    "item_name": "Antique Bookshelf",

    "description": "Makes your apartment smell like rich mahogany",

    "price": 7999,

    "category_name": "Household"

  }

]

```