# choose-cloud-provider
Help guide which cloud platform to learn first

## API
This project uses the [JSearch API](https://rapidapi.com/letscrape-6bRBa3QguO5/api/jsearch).

## Usage

1. Clone repo
2. install dependencies: ``` pip install requirements.txt ```
3. add your API key/host to ```.env``` file
4. run ```analysis.ipynb```
P.S : change location first in ```main.py```
```python
    querystring = {
        "query": "add location here",
        ...
    }
```

## Future Development

- Extract responsibilities, analyze which technologies are more used, and what other tech to learn,...
- Add more job boards: LinkedIn, Indeed.
- Incorporate more attributes into the analysis.
- Fix check rate limit.
