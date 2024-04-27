import { parse } from 'url';

export async function GET(request) {

  const { query } = parse(request.url, true);
  const maxPrice = query.maxPrice;

    const flaskApiUrl = `${process.env.NEXT_PUBLIC_MERCHANT}?maxPrice=${maxPrice}`;
    // `${process.env.NEXT_PUBLIC_DISPLAY_FETCH_QUIZ}?questionId=${questionId}`
    // `https://racquetfinder-8c8b6e21eb36.herokuapp.com/api/scrape/merchant?maxPrice=${maxPrice}`
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
  