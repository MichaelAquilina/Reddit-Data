The repository contains two separate folders which contain information about the posts downloaded from each subreddit and cached copies of each related page to ensure quick access and consistency of results when performing training and classification. 

A subreddits directory within the data source further contains further subdirectories named after any extracted subreddit. Using this convention allows easy checking for what subreddits are available with a simple list files command. Each subreddit directory then contains a JSON formatted file which follows the same structure as what is returned by the [Reddit API form a listing command](http://www.reddit.com/dev/api#GET_by_id_{names})⁠. The JSON file is filtered so that it only contains references to posts which were not ignored during the post extraction process to speed up processing time and save space.

Cached pages are also stored within the data source within a separate pages folder so that they can quickly and consistently be accessed when they are required for training. Only text/html files are downloaded and no referenced material from the page is downloaded alongside it (like images). Pages are stored within the pages folder in a manner that allows URLs to be easily translatable to their location within the folder. Each domain for every page downloaded is stored as a subdirectory in the pages folder. This allows the available domains to be listed using a simple list files command much in the same way as the subreddits. 
To convert a URL to a file path, consider the generic URL format of http://[domain]/[path]/[filename], then this is translated to a subdirectory within the pages folder as follows:

Original URL    http://[domain]/[[path]/[filename]
File Path       [domain]/[path]/[filename]%$%

Where the file path is always relative to the pages subdirectory in which it is stored. The "%$%" tag shown above is used to prevent clashes between file names and directories that share the same name. For example, the following two URLs are both valid but would collide without the special tag:

Original URL    http://www.example/com/bristol
File Path       example.com/bristol%$%

Original URL    http://www.example.com/bristol/travel
File Path       example.com/bristol/travel%$%

In example 1, "bristol" is a file. In example 2, "bristol" is a folder. Using the "%$%" tag allows for both to exist witin the same subdirectory and thus allows this kind of URL structure to be present within the pages directory. As can be seen, the “www” in front of a domain is removed if it is used. Alternative sub-domains are retained however as these often refer to separate web pages. Furthermore, URLs with a domain but without a path are considered to have the file name “index.html” which allows empty paths to be stored in the domain folder:

Original URL    http://www.example.com
File Path       example.com/index.html%$%

