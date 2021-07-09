# Cyber Semantic Conventions
Semantic conventions allow you to describe data structures recorded in the cyber knowledge graph for use in one or 
more applications.
![Semantic Conventions](img/semantic_conventions.png)
## Cyber Semantic Convention Standards

### cyberLinks Definition

Definition of a Semantic Convention by a multi-cyberLink transaction
```python
ipfs_hash("semantic convention") -> ipfs_hash(`semantic convention` name) # `semantic convention` name
ipfs_hash(`semantic convention` name) -> ipfs_hash(`semantic convention` standard) # `semantic convention` standard
ipfs_hash(`semantic convention` name) -> ipfs_hash(`sender` name)         # `sender` name
ipfs_hash(`semantic convention` name) -> ipfs_hash(`from` name)           # `from` name
ipfs_hash(`from` name) -> ipfs_hash(`from` default value)                 # `from` default value
ipfs_hash(`semantic convention` name) -> ipfs_hash(`to` name)             # `to` name
ipfs_hash(`to` name) ->  ipfs_hash(`to` default value)                    # `to` default value
# definition for more than one cyberLink
[
ipfs_hash(`semantic convention` name) -> ipfs_hash(`from_[n]` name)       # `from_[n]` name
ipfs_hash(`from_[n]` name) -> ipfs_hash(`from_[n]` default value)         # `from_[n]` default value
ipfs_hash(`semantic convention` name) -> ipfs_hash(`to_[n]` name)         # `to_[n]` name
ipfs_hash(`to_[n]` default value)  ->  ipfs_hash(`to_[n]` default value)  # `to_[n]` default value
] 
```
example for the Tweet Semantic Convention:
```python
ipfs_hash("semantic convention") -> ipfs_hash("tweet")          # `semantic convention` name
ipfs_hash("tweet") -> ipfs_hash(`semantic convention` standard) # `semantic convention` standard
ipfs_hash("tweet") -> ipfs_hash("author")                       # `sender` name
ipfs_hash("tweet") -> ipfs_hash("key_value")                    # `from` name
ipfs_hash("key_value") -> ipfs_hash("tweet")                    # `from` default value
ipfs_hash("tweet") -> ipfs_hash("message")                      # `to` name
ipfs_hash("message") -> ipfs_hash("any")                        # `to` default value
```
### JSON Definition
Definition of the Tweet Semantic Convention by a cyberLink and JSON
##### cyberLInk
```python
ipfs_hash("semantic convention") -> # `semantic convention` class
ipfs_hash(JSON)                     # `semantic convention` json
```
##### JSON
```json
{
  "semantic_convention_name": `semantic convention` name,
  "semantic_convention_standard": `semantic convention` standard,
  "sender": {
    "name": `sender` name
  },
  "from": {
    "name": `from` name,
    "constant_value": `from` default value
  },
  "to": {
    "name": `to` name,
    "constant_value": `to` default value
  },
  # definition for more than one cyberLink
  [,  "from_[n]": {
    "name": `from_[n]` name,
    "constant_value": `from_[n]` default value
    },
    "to_[n]": {
    "name": `to_[n]` name,
    "constant_value": `to_[n]` default value
  }]        
}
```
example for the Tweet Semantic Convention:
```json
{
  "semantic_convention_name": "tweet",
  "semantic_convention_standard": `semantic convention` standard,
  "sender": {
    "name": "author"
  },
  "from": {
    "name": "key_value",
    "constant_value": "QmbdH2WBamyKLPE5zu4mJ9v49qvY8BFfoumoVPMR5V4Rvx"
  },
  "to": {
    "name": "message"
  }
}
```
## Constants
IPFS address of the `semantic convention`: `QmbCq4d3CdvSSx9NHPrVM9WxA9uj36CE5RyzY18gxfrXxS`  
IPFS address of the `tweet` word: `QmbdH2WBamyKLPE5zu4mJ9v49qvY8BFfoumoVPMR5V4Rvx`  
IPFS address of the `follow` word: `QmPLSA5oPqYxgc8F7EwrM8WS9vKrr1zPoDniSRFh8HSrxx`

## Tweet
cyberLink from the IPFS address of `tweet` word to an IPFS address of a message.  
Transaction sender is author of a tweet.  
### cyberLinks Definition
Definition of the Tweet Semantic Convention by a multi-cyberLink transaction
```python
ipfs_hash("semantic convention") -> ipfs_hash("tweet")          # `semantic convention` name
ipfs_hash("tweet") -> ipfs_hash(`semantic convention` standard) # `semantic convention` standard
ipfs_hash("tweet") -> ipfs_hash("author")                       # `sender` name
ipfs_hash("tweet") -> ipfs_hash("key_value")                    # `from` name
ipfs_hash("key_value") -> ipfs_hash("tweet")                    # `from` default value
ipfs_hash("tweet") -> ipfs_hash("message")                      # `to` name
ipfs_hash("message") -> ipfs_hash("any")                        # `to` default value
```
### JSON Definition
Definition of the Tweet Semantic Convention by a cyberLink and JSON
##### cyberLInk
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
    "name": "key_value",
    "constant_value": "QmbdH2WBamyKLPE5zu4mJ9v49qvY8BFfoumoVPMR5V4Rvx"
  },
  "to": {
    "name": "message"
  }
}
```

## Tweet Answer
cyberLink from a IPFS tweet message address to an IPFS address of an answer message.  
Transaction sender is author of an answer message.

## Follow
cyberLink from the IPFS address of `follow` word to an IPFS address of a cyber account address.  
Transaction sender is a subscriber.