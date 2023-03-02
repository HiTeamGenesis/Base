<script lang="ts">
  import { current_screen_store, Status } from "../store";
  import AutonomousPage from "./AutonomousPage.svelte";
  let current_screen: Status
  current_screen_store.subscribe(screen => {current_screen = screen});

  function handleScreen(e) {
    e.preventDefault();
    const screen = e.target.innerText.toUpperCase();
    switch (screen) {
      case "BIOLOGY":
        current_screen_store.set(Status.BIOLOGY)
        break;

      case "AUTONOMY":
        current_screen_store.set(Status.AUTONOMY)
        break;

      case "DELIVERY":
        current_screen_store.set(Status.DELIVERY)
        break;

      default:
        current_screen_store.set(Status.HOME)
        break;
      }
  }
</script>

<div class="first-column">
  <div class="indicators">
    <div class="indicators-item battery">
      <p>100%</p>
      <img src="/energy.svg"/>
    </div>
    <div class="indicators-item signal">
      <p>100%</p>
      <img src="/signal.svg"/>
    </div>
    <div class="indicators-item process">
      <p>100%</p>
      <img src="/alarm.svg"/>
    </div>
    <div class="indicators-item sensor">
      <p>100%</p>
      <img src="/processor.svg"/>
    </div>
  </div>
  <div class="missions-btn">
    <!-- svelte-ignore a11y-click-events-have-key-events -->
    <div class="missions-btn-item" on:click={handleScreen}>
      {#if current_screen == "BIOLOGY"}
        <p>Autonomy</p>
      {:else if current_screen == "AUTONOMY"}
        <p>Biology</p>
      {:else if current_screen == "DELIVERY"}
        <p>Autonomy</p>
      {/if}
    </div>
    <!-- svelte-ignore a11y-click-events-have-key-events -->
    <div class="missions-btn-item" on:click={handleScreen}>
      {#if current_screen == "BIOLOGY"}
        <p>Delivery</p>
      {:else if current_screen == "AUTONOMY"}
        <p>Delivery</p>
      {:else if current_screen == "DELIVERY"}
        <p>Biology</p>
      {/if}
    </div>
  </div>
</div>



<style>

  .first-column {
    display: grid;
    grid-template-rows: .6fr .4fr;
    justify-content: center;
    align-items: center;
    gap: 2rem;
  }
  
  .indicators {
    display: grid;
    grid-template-columns: .5fr .5fr;
    justify-content: center;
    align-items: center;
    gap: 3rem;
    border: 1px solid black;
    padding: 2rem;
    border-radius: .6rem;
  }

  .indicators-item {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    border-radius: .8rem;
    gap: .6rem;
  }

  .indicators-item p {
    font-size: 1.4rem;
  }
  
  .indicators-item img {
    width: 2rem;
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
  
  .missions-btn {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 1.4rem;
  }

  .missions-btn-item {
    width: 100%;
    height: 2.4rem;
    background-color: blue;
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: .6rem;
    cursor: pointer;
  }

</style>