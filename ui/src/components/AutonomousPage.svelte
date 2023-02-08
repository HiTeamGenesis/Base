<script>
  import CoordinateInput from './CoordinateInput.svelte';
  import {writable} from 'svelte/store'
  import 'leaflet/dist/leaflet.css'  
  import * as L from 'leaflet';
  let map;
  let coordinates = writable([])
  let center = [39.3210, -111.0937]

  let markers = coordinates

  function createMap(container) {
    let m = L.map(container).setView([39.3210, -111.0937], 8);
     L.tileLayer(
      'https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png',
      {
        maxZoom: 14,
      }
    ).addTo(m);

    return m
  }  

  function markerIcon() {
    let html = `<div class="map-marker"> <div> <svg style="width:30px;height:30px" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" stroke="currentColor"><path d="M8 14v3m4-3v3m4-3v3M3 21h18M3 10h18M3 7l9-4 9 4M4 10h16v11H4V10z"></path></svg> </div></div>`
    return L.divIcon({
      html, className:"map-marker"
    })
  }

  function createMarker(loc) {
    const icon = markerIcon();
    const marker = L.marker(loc, {icon});
    return marker
  }

  let markerLayers

  function mapAction(container) {
    map = createMap(container);
    markerLayers = L.layerGroup()
    for(let location of $markers) {
      let m = createMarker(location)
      markerLayers.addLayer(m)
    }
    markerLayers.addTo(map)
    return {
      destroy: () => {
        map.remove()
      }
    }
  }


</script>

<svelte:head>
   <!-- In the REPL you need to do this. In a normal Svelte app, use a CSS Rollup plugin and import it from the leaflet package. -->
   <link rel="stylesheet" href="https://unpkg.com/leaflet@1.6.0/dist/leaflet.css"
   integrity="sha512-xwE/Az9zrjBIphAcBb3F6JVqxf46+CDLwfLMHloNu6KEQCAWi6HcDUbeOfBIptF7tcCzusKFjFw2yuvEpDL9wQ=="
   crossorigin=""/>
</svelte:head>

<main>
  <div class="map-container">
    <div id="map" use:mapAction></div>
    <div class="map-input">
      <div class="coords">
        {#each $coordinates as coord, index}
          <p>{index + 1} | LAT: {coord[0]} / LNG: {coord[1]}</p>
        {:else}
          <p>Insert a new coordinate</p>
        {/each}
      </div>
      <CoordinateInput coordinates={coordinates}/>
    </div>
  </div>
  <div class="cam-container">
    <h1>camera</h1>
  </div>
</main>

<style>
  .map-container {
    display: grid;
    grid-template-columns: 1fr 1fr;
    width: 100%;
    height: 50vh;
  }
  .coords p {
    color: white;
    margin-bottom: 20px;
  }
  .map-input {
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 30px 0;
    overflow-y: scroll;
  }
  #map {height: 100%; width: 100%;}

  .cam-container {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 45vh;
    background-color: rgb(54, 54, 54);
  }
</style>