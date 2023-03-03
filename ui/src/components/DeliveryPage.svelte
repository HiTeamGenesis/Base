<script>
  import LeftMenu from "./LeftMenu.svelte";
  import 'leaflet/dist/leaflet.css';
  import {LeafletMap, TileLayer} from 'svelte-leafletjs';

  let map;
  let center = [39.3210, -111.0937]
  let zoom = 10;

  let mapOptions = {
    center, zoom
  }

  const tileUrl = "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png";

  const tileLayerOptions = {
    minZoom: 0,
    maxZoom: 20,
    maxNativeZoom: 19,
    attribution: "© OpenStreetMap contributors",
  };

</script>

<div class="delivery">
  <LeftMenu />
  <div class="biology-arms">
    <div class="biology-arms-item">CAM ARM</div>
    <div class="biology-arms-item">MAIN ARM</div>
  </div>
  <div class="map-container">
    <div id="map">
      <LeafletMap bind:this={map} options={mapOptions}>
        <TileLayer url={tileUrl} options={tileLayerOptions}/>
      </LeafletMap>  
    </div>
  </div>
</div>

<style>
  .delivery {
    width: 100%;
    height: 50vh;
    display: grid;
    grid-template-columns: .2fr .4fr .4fr;
    justify-content: center;
    align-items: center;
    padding-bottom: 2rem;
  }

  .biology-arms {
    width: 100%;
    height: 100%;
    display: grid;
    grid-template-columns: .5fr .5fr;
    justify-content: center;
    align-items: center;
    gap: 2rem;
  }
  
  .biology-arms-item {
    background-color: #222222;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    color: #cccccc;
    border-radius: .6rem;
  }

  .map-container {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: center;
    justify-content: center;
  }
  
  #map {height: 100%; width: 90%;
  border-radius: .6rem;
  }

</style>