# Cyber Semantic Conventions
Semantic conventions allow you to describe data structures recorded in the cyber knowledge graph for use in one or 
more applications.

## [Proposed Cyber Semantic Convention Standards](semantic-convention-standards.md)

## Tweet
### Constants
IPFS address (CID) of the `tweet` string: `QmbdH2WBamyKLPE5zu4mJ9v49qvY8BFfoumoVPMR5V4Rvx` 
### cyberLinks
Tweet object is cyberLink:
- CID of the `tweet` string -> CID of a message  

Transaction sender is author of a tweet.  

[Example cyberLink of Tweet object](https://rebyc.cyber.page/network/bostrom/tx/45DC76417B8BFC1149B6E1FD74313269A3EAFBEE53EF3097DCF02C8F88469CAA)    
[Create Tweet object by the Tweet Semantic Convention](create_objects_by_semantic_convention.ipynb)    
[Create Tweet object directly](create_objects_directly.ipynb)  

![Tweet Object](img/tweet_object.png)

## Tweet Answer (current convention)
### Constants
None
### cyberLinks
Tweet Answer is cyberLink:
- CID of a tweet message -> CID of an answer message  

Transaction sender is author of an answer message.

[Example cyberLink of Tweet Answer object](https://rebyc.cyber.page/network/bostrom/tx/96832D383D88A3D1E3A4CA177BAAE3799D0514BB2FF7E6A183EDA3171CBF219E)  
[Create Tweet Answer object directly](create_objects_directly.ipynb)  

![Tweet Answer Object](img/tweet_answer_object.png)
  
## Tweet Answer (proposed convention)
It is suggested to add an additional link to recognize answer to a tweet.
### Constants
CID of the `tweet answer` string: `QmXxCVgN8WZi6QtF8x8u1pQsvVgLpi81pgjjwtHt1kQ8Ax`
### cyberLinks
Tweet Answer object is two cyberLinks:
- CID of a tweet message -> CID of an answer message
- CID of the `tweet answer` string -> CID of an answer message

Transaction sender is author of an answer message.

[Example cyberLinks of Tweet Answer object (proposed convention)](https://rebyc.cyber.page/network/bostrom/tx/7B88195911C18C40EDF8D74F24B94CAE57CBFC82BB620A003F929739580ADB4B)  
[Create Tweet Answer object directly](create_objects_directly.ipynb)  

![Tweet Answer Object (proposed convention)](img/tweet_answer_object(proposed).png)  

## Follow
### Constants
CID of the `follow` string: `QmPLSA5oPqYxgc8F7EwrM8WS9vKrr1zPoDniSRFh8HSrxx`
### cyberLinks
Follow object is cyberLink:
- CID of the `follow` string -> CID of a cyber account address

Transaction sender is a subscriber.

[Example cyberLink of Follow object](https://rebyc.cyber.page/network/bostrom/tx/13D76B4F9F7BDDFC11EDA25887E225E31EE59C2C67CD884D1789C638EEB3D110)  
[Create Follow object directly](create_objects_directly.ipynb#follow)  

![Follow Object](img/follow_object.png)

## Unfollow
### Constants
CID of the `unfollow` string: `QmRsRWy8K9Sb5bsHDzTUD1mtXjk5rgtXM2xi4dqmN529kM`
### cyberLinks
Unfollow object is cyberLink:
- CID of the `unfollow` string -> CID of a cyber account address

Transaction sender is an unsubscribed subscriber.

[Example cyberLink of Unfollow object](https://rebyc.cyber.page/network/bostrom/tx/F8A5BAB4C7A7F26453A5B4F3448C45D8DEF6A47E3372AF123A44A31466DA82A1)  
[Create Unfollow object directly](create_objects_directly.ipynb)  

![Unfollow Object](img/unfollow_object.png)

## Avatar 
### Constants
CID of the `avatar` string: `Qmf89bXkJH9jw4uaLkHmZkxQ51qGKfUPtAMxA8rTwBrmTs`  
CID of the `avatar pic` string: `QmSWnQSqwmovA8o3xPuhfD4HEg19JYzQuoStrp8xFXWU2x`  
CID of the `avatar name` string: `QmbteQvDFdMLS7Uf24F7j4rAZNSqinT74yygUhNWr2RaC2`  
CID of the `avatar account` string: `QmS1pivhZ9NPpA7CoyF7ZpuvK5RCLafBq9FtpnquoBmx18`  
### cyberLinks
Avatar class is cyberLinks:
- CID of `avatar` string -> CID of `avatar {class}` string  

The `pic`, `name` and `account` avatar classes have been set as constants, and you can skip creating them.

[Example cyberLink of Avatar Class](https://rebyc.cyber.page/network/bostrom/tx/FE15AF00777264712C633D3B4C22BFCD979BE3C646745226BCCEE09D3B31531F)  
[Create Avatar class directly](create_objects_directly.ipynb)  

![Avatar Class](img/avatar_class.png)

Avatar object is cyberLink:
- CID of `avatar {class}` string -> CID of a pic, name or account

[Example cyberLink of Avatar object](https://rebyc.cyber.page/network/bostrom/tx/72DDEE4104007DD1EAFC6A6436F192740C5AAAFEE3CB7DAD9EEBD8FABE12543C)  
[Create Avatar object directly](create_objects_directly.ipynb)  

![Avatar Object](img/avatar_object.png)
  
## Favorites
### Constants
CID of the `favorite` string: `QmRU8Tz93jmiHEJcTz7GbmuJ6N3DxS8jzqDAp2c9UAK4mR`  
CID of the `favorite name` string: `QmbWLFqpQo1fUPnTsM4jP9aipugMXNAKSDovQLVNV4a4ai`  
CID of the `favorite label` string: `QmQuN7KtLjYGX4m4gon73Pitm8942hkwD1usQYAFghH5d5`  
CID of the `favorite tag` string: `QmcYCv1bpzTmxcfkkxUv8bBW23UCBgVMkVkPCeZ2Q5kJnb` 
### cyberLinks
Favorite class is cyberLink:
- CID of the `favorite` -> CID of `favorite {name|label|tag}`  

The `name`, `label` and `tag` favorite classes have been set as constants, and you can skip creating them.

[Example cyberLink of Favorite Class](https://rebyc.cyber.page/network/bostrom/tx/E0E09C89C5EF320F28865F9059AE16CF3B97FF64D89B9FBC6A725F20875A51C6)  
[Create Favorite class directly](create_objects_directly.ipynb)

![Favorite Class](img/favorite_class.png)

Favorite object is a cyberLink:
- CID of `favorite {class}` -> CID of an object

[Example cyberLink of Favorite object](https://rebyc.cyber.page/network/bostrom/tx/735AF99AE9C1678A7C5DD855383497182AFA842CF5BD7A317FD7BCB6B2D1D78C)  
[Create Favorite object directly](create_objects_directly.ipynb)  

![Favorite Object](img/favorite_object.png)

## Data Type 
### Constants
CID of the `data type` string: `QmRU8Tz93jmiHEJcTz7GbmuJ6N3DxS8jzqDAp2c9UAK4mR`
### cyberLinks
Initialize of a data type: 
- CID of the `data type` -> CID of a data type

[Example cyberLink of Data Type Class](https://rebyc.cyber.page/network/bostrom/tx/43666E5C5E0716C87A663786A71E226613AD566633DEEF220D862FB1E8FB868F)   
[Initialize of a Data Type directly](create_objects_directly.ipynb)  

![Data Type Class](img/data_type_class.png)
  
Link object with a data type:
- CID of a data type -> CID of an object

[Example cyberLink of Data Type object](https://rebyc.cyber.page/network/bostrom/tx/)  
[Link object with a Data Type directly](create_objects_directly.ipynb)  

![Data Type Object](img/data_type_object.png)

## Price Verified 
- CID of a token contract address -> CID of a price source

## Token Data
- CID of a token contract address -> CID of a metadata