<script>
  export let coordinates = [];
  let lat
  let lng

  function handleInput() {
    coordinates.update(coordinates => [...coordinates, [lat, lng]])
    lat = 0
    lng = 0
  }

</script>

<div class="coordinate">
  <input type="number" bind:value={lat}>
  <input type="number" bind:value={lng}>
  <button on:click={handleInput}>Add coordinate</button>
</div>

<style>
  .coordinate {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
  }

  .coordinate input {
    width: 70%;
    height: 30px;
    margin-bottom: 6px;
    border-radius: 8px;
  }

  .coordinate button {
    width: 70%;
    height: 30px;
    border-radius: 8px;
    margin-top: 15px;
  }

</style>