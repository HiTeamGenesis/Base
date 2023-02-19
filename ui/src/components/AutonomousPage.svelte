<script>
  import CoordinateInput from './CoordinateInput.svelte';
  import {writable} from 'svelte/store';
  import 'leaflet/dist/leaflet.css';
  import {Marker, LeafletMap, TileLayer} from 'svelte-leafletjs';

  let map;

  let coordinates = writable([]);
  let center = [39.3210, -111.0937]
  let zoom = 10;

  let markers = coordinates;

  let mapOptions = {
    center, zoom
  }

  const tileUrl = "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png";

  const tileLayerOptions = {
    minZoom: 0,
    maxZoom: 20,
    maxNativeZoom: 19,
    attribution: "© OpenStreetMap contributors",
  }

  function deleteMarker(coord) {
    const index = $markers.indexOf(coord)
    $markers.splice(index, 1)
    $markers = $markers
  }

</script>


<main>
  <div class="map-container">
    <div id="map">
      <LeafletMap bind:this={map} options={mapOptions}>
        <TileLayer url={tileUrl} options={tileLayerOptions}/>
        {#each $markers as coord}
          <Marker latLng={coord} />
        {/each}
      </LeafletMap>  
    </div>
    <div class="map-input">
      <h1>Coordinates</h1>
      <CoordinateInput coordinates={coordinates} center={center}/>
      <div class="coords">
        {#each $markers as coord}
        <div class="coordItem">
          <p>LAT: {coord[0]} | LNG: {coord[1]}</p>
          <!-- svelte-ignore a11y-click-events-have-key-events -->
          <img on:click={(e) => deleteMarker(coord)} src="/delete.svg" alt="delete-icon"/>
        </div>
        {/each}
      </div>
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

  .map-input h1 {
    color: white;
    margin-bottom: 14px;
  }

  .coords {
    margin-top: 20px;
  }

  .coordItem {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    margin-bottom: 5px;
    gap: 4px;
  }

  .coordItem p {
    color: white;
    font-size: 18px;
  }

  .coordItem img {
    width: 30px;
    height: 30px;
  }

  .coordItem img:hover {
    cursor: pointer;
    transform: scale(1.05);
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