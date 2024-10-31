# Medium RSS Aggregator

A simple FastAPI application to aggregate Medium articles by tags into a single RSS feed.

## Usage

- Deploy the backend with FastAPI and an HTML frontend interface that lets users specify tags.
- Access \`/medium_rss\` with \`?tags=your-tags\` to generate an RSS feed based on selected Medium tags.

## Installation

1. Clone the repository:

   \`\`\`bash
   git clone https://github.com/yourusername/medium-rss-aggregator.git
   cd medium-rss-aggregator
   \`\`\`

2. Install dependencies:

   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

3. Run the application:

   \`\`\`bash
   uvicorn app.main:app --reload
   \`\`\`

## Running with Docker

1. Build the Docker Image:

   ```bash
   docker build -t medium-rss-aggregator .
   ```

2. Run the Docker Container:

   ```bash
   docker run -d -p 8000:8000 medium-rss-aggregator
   ```

The application will now be available at http://localhost:8000.
