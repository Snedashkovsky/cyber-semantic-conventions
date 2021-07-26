# Proposed Cyber Semantic Convention Standards

## How to use

### Insert Objects
<img alt="Insert objects" src="img/insert_objects.png" width="600" />

- [example of inserting by a Semantic Convention](create_objects_by_semantic_convention.ipynb)  

### Read Objects

<img alt="Read objects" src="img/read_objects.png" width="600" />

## How is it solved for RDF

[R2RML: RDB to RDF Mapping Language](https://www.w3.org/2001/sw/rdb2rdf/r2rml/)  
[R2RML: RDB to RDF Mapping Language Schema](https://www.w3.org/ns/r2rml)  
[RDF Mapping Language (RML). Example: Mapping a JSON data source](https://rml.io/specs/rml/#example-JSON)  
[RDB2Graph: A Generic Framework for Modeling Relational Databases as Graphs](http://ceur-ws.org/Vol-1312/jist2014pd_paper10.pdf)  
[Schema.org](https://schema.org/docs/documents.html)  
[Schema.org (example City Type)](https://schema.org/City)  
[Web-Karma. Information Integration Tool](https://github.com/usc-isi-i2/Web-Karma)  
[OpenRefine, tool for working with messy data and improving it](https://github.com/OpenRefine/OpenRefine)  
[LOD-enabled version of OpenRefine](https://github.com/sparkica/LODRefine)

## Object Structure in cyber

<img alt="Semantic Convention Object" src="img/semantic_convention_object.png" width="600" />

- [example of a Tweet Object](#tweet-object)

## Semantic Convention cyberLinks Definition

Definition of a Semantic Convention by a multi-cyberLink transaction
```python
ipfs_hash("semantic convention") -> ipfs_hash(`semantic convention` name) # `semantic convention` name
ipfs_hash(`semantic convention` name) -> ipfs_hash(`semantic convention` standard) # `semantic convention` standard
ipfs_hash(`semantic convention` name) -> ipfs_hash(`sender` role name)    # `sender` role name
ipfs_hash(`semantic convention` name) -> ipfs_hash(`from` role name)      # `from` role name
ipfs_hash(`from` role name) -> ipfs_hash(`from` key value)                # `from` key value (optional)
ipfs_hash(`semantic convention` name) -> ipfs_hash(`to` role name)        # `to` role name
ipfs_hash(`to` role name) ->  ipfs_hash(`to` key value)                   # `to` key value (optional)
# definition for more than one cyberLink (optional)
[
ipfs_hash(`semantic convention` name) -> ipfs_hash(`from_[n]` role name)  # `from_[n]` role name
ipfs_hash(`from_[n]` role name) -> ipfs_hash(`from_[n]` key value)        # `from_[n]` key value (optional)
ipfs_hash(`semantic convention` name) -> ipfs_hash(`to_[n]` role name)    # `to_[n]` role name
ipfs_hash(`to_[n]` role name)  ->  ipfs_hash(`to_[n]` key value)          # `to_[n]` key value (optional)
]
```
![Semantic Convention Standards. cyberLink definition](img/semantic_convention_standards_cyberlinks_definition.png)  
- [example of Semantic Convention for Tweets](#tweet)

## Semantic Convention JSON Definition
Definition of a Semantic Convention by a cyberLink and JSON
### cyberLInk
```python
ipfs_hash("semantic convention") -> # `semantic convention` class
ipfs_hash(JSON)                     # `semantic convention` json
```
### JSON
```json
{
  "semantic_convention_name": `semantic convention` name,
  "semantic_convention_standard": `semantic convention` standard,
  "sender": {
    "name": `sender` name
  },
  "from": {
    "name": `from` name,
    "key_value": `from` key value
  },
  "to": {
    "name": `to` name,
    "key_value": `to` key value
  },
  # definition for more than one cyberLink (optional)
  [,  "from_[n]": {
    "name": `from_[n]` name,
    "key_value": `from_[n]` key value
    },
    "to_[n]": {
    "name": `to_[n]` name,
    "key_value": `to_[n]` key value
  }]
}
```

<img alt="Semantic Convention Standards. JSON definition" src="img/semantic_convention_standards_json_definition.png" width="600" />

- [example of Semantic Convention for Tweets](#tweet)

## Constants
IPFS address (CID) of the `semantic convention` string: `QmbCq4d3CdvSSx9NHPrVM9WxA9uj36CE5RyzY18gxfrXxS`  
CID of the `tweet` string: `QmbdH2WBamyKLPE5zu4mJ9v49qvY8BFfoumoVPMR5V4Rvx`

## Tweet
### Tweet Object
cyberLink from the IPFS address of `tweet` word to an IPFS address of a message.
Transaction sender is author of a tweet.

<img alt="Tweet Object" src="img/tweet_object.png" width="600" />
 
- [example transaction of Tweet object](https://rebyc.cyber.page/network/bostrom/tx/45DC76417B8BFC1149B6E1FD74313269A3EAFBEE53EF3097DCF02C8F88469CAA)
- [inserting Tweet object into Cyber by Semantic Convention](create_objects_by_semantic_convention.ipynb)
### cyberLinks Definition
Definition of the Tweet Semantic Convention by a multi-cyberLink transaction
```python
ipfs_hash("semantic convention") -> ipfs_hash("tweet")          # `semantic convention` name
ipfs_hash("tweet") -> ipfs_hash(`semantic convention` standard) # `semantic convention` standard
ipfs_hash("tweet") -> ipfs_hash("author")                       # `sender` role name
ipfs_hash("tweet") -> ipfs_hash("key_value")                    # `from` role name
ipfs_hash("key_value") -> ipfs_hash("tweet")                    # `from` key value
ipfs_hash("tweet") -> ipfs_hash("message")                      # `to` role name
```
![The Tweet Convention Standard. cyberLink definition](img/tweet_cyberlinks_definition.png)  
- [example transaction of Tweet Semantic Convention by cyberLinks](https://rebyc.cyber.page/network/bostrom/tx/A97A7621EFC07C0038FA5B1A9BA328FC3CCF1A5775141256855E4285A061BB27)
- [creation Tweet Semantic Convention in Cyber](create_tweet_semantic_conventions.ipynb)
### JSON Definition
Definition of the Tweet Semantic Convention by a cyberLink and JSON
##### cyberLink
```python
ipfs_hash("semantic convention") -> # `semantic convention` class
ipfs_hash(JSON)                     # `semantic convention` json
```
##### JSON
```json
{
  "semantic_convention_name": "tweet",
  "semantic_convention_standard": `semantic convention` standard,
  "sender": {
    "name": "author"
  },
  "from": {
    "name": "tweet_key_value",
    "key_value": "QmbdH2WBamyKLPE5zu4mJ9v49qvY8BFfoumoVPMR5V4Rvx"
  },
  "to": {
    "name": "message"
  }
}
```

<img alt="The Tweet Convention Standard. JSON definition" src="img/tweet_json_definition.png" width="600" />

- [example transaction of Tweet Semantic Convention by JSON](https://rebyc.cyber.page/network/bostrom/tx/3EE04317DE0AFEDAA826CC24A6062BC89339B9CF7F780E33ADC04E8A823F8EEE)
- [creation Tweet Semantic Convention in Cyber](create_tweet_semantic_conventions.ipynb)
