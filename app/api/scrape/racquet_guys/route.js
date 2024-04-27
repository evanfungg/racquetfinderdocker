

export async function GET() {
  const flaskApiUrl = 'http://localhost:5328/api/scrape/racquet_guys';

  try {
    const flaskResponse = await fetch(flaskApiUrl);
    const data = await flaskResponse.json();

   
    return new Response(JSON.stringify(data), {
      status: 200,
      headers: {
        'Content-Type': 'application/json',
      },
    });
  } catch (error) {
    console.error('Failed to fetch from Flask API:', error);
    return new Response(JSON.stringify({ message: 'Failed to fetch data' }), {
      status: 500,
      headers: {
        'Content-Type': 'application/json',
      },
    });
  }
}
