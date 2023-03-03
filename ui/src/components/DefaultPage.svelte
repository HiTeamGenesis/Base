<script lang="ts">
  import { current_screen_store, Status } from "../store";
  import AutonomousPage from "./AutonomousPage.svelte";
  import BiologyPage from "./BiologyPage.svelte";
  import DeliveryPage from "./DeliveryPage.svelte";

  let buttons = [{active: true, cam: 1}, {active: false, cam: 2}]
  let arms = true;

  let current_screen: Status
  current_screen_store.subscribe(screen => {current_screen = screen});

  function handleScreen(e) {
    e.preventDefault()
    const screen = e.target.innerText.toUpperCase();
    switch (screen) {
      case "BIOLOGY":
        current_screen_store.set(Status.BIOLOGY)
        arms = false;
        break;

      case "AUTONOMY":
        current_screen_store.set(Status.AUTONOMY)
        break;

      case "DELIVERY":
        current_screen_store.set(Status.DELIVERY)
        arms = false
        break;
      
      default:
        current_screen_store.set(Status.HOME)
        arms = true;
        break;
      }
  }

  function toggleCameras(e) {
    e.preventDefault();
    const cam = parseInt(e.target.innerText.split("Cam")[1])
    if(!buttons[cam - 1].active) {
      buttons[cam - 1].active = true;
    } else {
      buttons[cam - 1].active = false;
    }
  }
</script>

<main class="home-page">
  <div class="cameras">
    <!-- svelte-ignore a11y-click-events-have-key-events -->
    <div class="home-btn" on:click={handleScreen}>
      <img src="/home.svg"/>
    </div>
    {#if arms} 
      <div class="arms">
        <div class="arm-camera"></div>
        <div class="arm-principal"></div>
      </div>
    {/if}
    {#each buttons as btn}
      {#if btn.active}
        <div class="cameras-item">
          <iframe src="192.168.1.10:8000"/>
          </div>
      {/if} 
    {/each}
    <div class="controls">
      <button class="controls-item" on:click={toggleCameras}>Cam1</button>
      <button class="controls-item" on:click={toggleCameras}>Cam2</button>
    </div>
  </div>
  {#if Status[current_screen] == "HOME"}
  <div class="utils">
    <div class="missions">
      <!-- svelte-ignore a11y-click-events-have-key-events -->
      <div class="missions-item" on:click={handleScreen}>
        <h1>Biology</h1>
      </div>
      <!-- svelte-ignore a11y-click-events-have-key-events -->
      <div class="missions-item" on:click={handleScreen}>
        <h1>Autonomy</h1>
      </div>
      <!-- svelte-ignore a11y-click-events-have-key-events -->
      <div class="missions-item" on:click={handleScreen}>
        <h1>Delivery</h1>
      </div>
    </div>
    <div class="settings">
      <div class="settings-item battery">
        <img src="/energy.svg" />
      <h1>Battery</h1>
      <p>100%</p>
    </div>
    <div class="settings-item signal">
      <img src="signal.svg"/>
      <h1>Signal</h1>
      <p>98%</p>
    </div>
    <div class="settings-item process">
      <img src="alarm.svg"/>
      <h1>Processes</h1>
      <p>0</p>
    </div>
    <div class="settings-item sensor">
      <img src="processor.svg"/>
      <h1>Sensors</h1>
      <p>5/8</p>
    </div>
  </div>
</div>
  {:else if Status[current_screen] == "AUTONOMY"}
  <AutonomousPage />
  {:else if Status[current_screen] == "BIOLOGY"}
    <BiologyPage />
  {:else if Status[current_screen] == "DELIVERY"}
    <DeliveryPage />
  {/if}
</main>

<style>
  main {
    width: 100%;
    height: 100vh;
    display: flex;
    flex-direction: column;
    gap: 2rem;
    justify-content: center;
    align-items: center;
  }

  .cameras {
    width: 100vw;
    height: 70vh;
    display: flex;
    flex-direction: row;
    position: relative;
    justify-content: center;
    align-items: center;
  }

  .home-btn {
    position: absolute;
    right: 2rem;
    top: 2rem;
  }

  .home-btn img {
    width: 2.8rem;
    cursor: pointer;
    filter: invert(83%) sepia(0%) saturate(187%) hue-rotate(191deg) brightness(100%) contrast(92%);
  }

  .controls {
    width: 15%;
    height: 2.4rem;
    position: absolute;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    gap: 1rem;
    bottom: 2rem;
    right: 2rem;
  }

  .controls-item {
    background-color: #d9d9d9;
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: .4rem;
    border: none;
    cursor: pointer;
  }

  .arms {
    width: 24%;
    height: 6rem;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    top: 2rem;
    left: 2rem;
    position: absolute;
    gap: 1rem;
  }
  
  .arms > div {
    background-color: #d9d9d9d9;
    border: 1px solid black;
    height: 100%;
    width: 100%;
    border-radius: .8rem;
  }

  .cameras-item {
    width: 100%;
    height: 100%;
    background-color: #1f1f1f;
    border: 1px black solid;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #cccccc;
  }

  .cameras-item iframe {
    width: 100%;
    height: 100%;
  }

  .utils {
    width: 90%;
    height: 20vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;

  }

  .settings {
    width: 100%;
    display: grid;
    grid-template-columns: repeat(4, .25fr);
    gap: 1.6rem;
  }

  .settings-item {
    display: flex;
    height: 4rem;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    background-color: #222222;
    border-radius: .8rem;
    gap: .6rem;
    cursor: pointer;
  }

  .settings-item h1 {
    font-size: 1.6rem;
    font-weight: 500;
    color: #cccccc;
  }

  .settings-item p {
    font-size: 1.6rem;
    font-weight: 500;
    color: #cccccc;
  }

  .settings-item img {
    width: 2.8rem;
  }

  .battery img {
    filter: invert(91%) sepia(12%) saturate(6345%) hue-rotate(331deg) brightness(105%) contrast(101%);
  }

  .signal img {
    filter: invert(73%) sepia(43%) saturate(768%) hue-rotate(55deg) brightness(99%) contrast(92%);
  }

  .process img {
    width: 2.6rem;
    filter: invert(31%) sepia(77%) saturate(2024%) hue-rotate(339deg) brightness(115%) contrast(109%);
  }

  .sensor img {
    filter: invert(37%) sepia(43%) saturate(4330%) hue-rotate(216deg) brightness(100%) contrast(101%);
  }

  .missions {
    width: 100%;
    height: 100%;
    display: grid;
    grid-template-columns: repeat(3, .333fr);
    padding-bottom: 2rem;
    gap: 1.6rem;
  }

  .missions-item {
    height: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    background-color: #222222;
    border-radius: .8rem;
    cursor: pointer;
  }
  
  .missions-item h1 {
    font-size: 1.4rem;
    color: #cccccc;
  }

</style>