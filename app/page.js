'use client'
import Image from "next/image";
import { useState, useEffect } from "react";
import './styles.css'; 

export default function Home() {
  const [racquets, setRacquets] = useState([]);
  const [maxPrice, setMaxPrice] = useState(201); 

  
  const fetchRacquets = () => {
    fetch(`api/scrape/merchant?maxPrice=${maxPrice}`)
    ///api/scrape/merchant?maxPrice=${maxPrice}
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        setRacquets(data);
      });
  };

  
  useEffect(() => {
    fetchRacquets();
  }, []); 

  return (
    <main className="main">
      <header className="header">
        <h1>Racquet Finder</h1>
      </header>
      
      <input type="range" min="0" max="500" value={maxPrice} onChange={(e) => setMaxPrice(e.target.value)} />
      <p>Max Price: ${maxPrice}</p>
      
      <button onClick={fetchRacquets}>Search</button>
      <div className="grid">
        {racquets.map((racquet, index) => (
          <div key={index} className="card">
            <a href={racquet.link} target="_blank" rel="noopener noreferrer">
              <h2 className="title">{racquet.name}</h2>
            </a>
            <p>{racquet.price}</p>
            <div className="imageContainer">
              <Image src={racquet.image_url} alt={racquet.name} width={200} height={200} layout="responsive" />
            </div>
          </div>
        ))}
      </div>
    </main>
  );
}
