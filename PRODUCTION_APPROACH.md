# Production Approach

For 200 casinos updated daily, I would run the scraper as a scheduled cloud job rather than from the web server. Each casino/source would have a small scraper adapter so that changes to one website do not break the entire system. The job would check robots.txt, fetch pages with reasonable rate limits, retry temporary failures with backoff, validate the extracted fields, and record failures separately.

I would use a managed cloud environment such as a scheduled container or serverless job. The React frontend would remain a static site, while the scraper would run independently and write normalized results to a managed PostgreSQL database. I would keep the previous successful dataset so that a failed daily run does not remove the last known-good data. Database backups would be enabled through the managed provider, with periodic exports for additional protection.

The public site would use a custom domain with DNS managed through a provider such as Cloudflare. HTTPS would be handled automatically by the hosting platform. The daily scraper could be triggered using a cloud scheduler or cron service. Each run would return a success/failure status, and repeated failures would trigger an email or Slack alert so that broken sources are investigated quickly.

For a small 200-site deployment, I would expect the basic infrastructure to be in the tens of US dollars per month, excluding domain registration and variable AI/API usage. The assessment version intentionally keeps this simpler by generating JSON and serving it through a static React application.
