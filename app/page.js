'use client'
import Image from "next/image";
import { useState, useEffect } from "react";
import './styles.css'; 

export default function Home() {
  const [racquets, setRacquets] = useState([]);
  const [maxPrice, setMaxPrice] = useState(201); 

  const fetchRacquets = () => {
    fetch(`api/scrape/merchant?maxPrice=${maxPrice}`)
      .then((response) => response.json())
      .then((data) => {
        setRacquets(data);
      });
  };

  useEffect(() => {
    fetchRacquets();
  }, []); 

  return (
    <div className="wrapper">
      <header className="header">
        <div className="header-inner">
          <h1>Racquet Finder</h1>
          <div className="nav">
          <div className="image-container">
            <img src="/racquetfinder.png" alt="Racquet Image" />
          </div>
          </div>
        </div>
      </header>

      <div className="content">
        <div className="search-area">
          <input type="range" min="0" max="500" value={maxPrice} onChange={(e) => setMaxPrice(e.target.value)} />
          <p>Max Price: ${maxPrice}</p>
          <button onClick={fetchRacquets}>Search</button>
        </div>

        <div className="cards-container">
          {racquets.map((racquet, index) => (
            <div key={index} className="card">
              <a className = "racquet-link" href={racquet.link} target="_blank" rel="noopener noreferrer">
                <Image src={racquet.image_url} alt={racquet.name} width={200} height={200} />
                <div className="card-body">
                  <h2>{racquet.name}</h2>
                  <p>{racquet.price}</p>
                </div>
              </a>
            </div>
          ))}
        </div>
      </div>

     
    </div>
  );
}
