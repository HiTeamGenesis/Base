<script>
  export let coordinates = [];
  let lat
  let lng

  function handleInput(e) {
    e.preventDefault()

    if (lat==null || lng==null || lat==0 || lng==0 || lat==0 && lng==0) {
      alert("Remember to set the lat and lng")
      return
    }

    $coordinates = [...$coordinates, [lat, lng]]

    lat = 0
    lng = 0
  }

</script>

<form class="coordinate" on:submit={handleInput}>
  <div class="cordInput">
    <label for="latitude">Latitude:</label>
    <input type="number" name="latitude" id="latitude" bind:value={lat}>
  </div>
  <div class="cordInput">
    <label for="longitude">Longitude:</label>
    <input type="number" name="longitude" id="latitude" bind:value={lng}>
  </div>
  <button on:click={handleInput}>Add coordinate</button>
</form>

<style>
  .coordinate {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 70%;
  }
  
  .cordInput {
    display: flex;
    width: 100%;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    text-align: left;
    margin-bottom: 12px;
  }

  .cordInput label {
    color: white;
    font-size: 16px;
    margin-bottom: 8px;
  }
  .cordInput input {
    width: 100%;
    font-size: 16px;
    height: 30px;
    color: white;
    padding: 2px 0 2px 6px;
    margin-bottom: 6px;
    border-radius: 10px;
    background-color: rgba(66, 66, 66, 0.41);
    box-shadow: 4px 4px 4px rgba(137, 207, 247, 0.18);
    border: none;
    outline: none;
  }

  .cordInput input:hover {
    background-color: rgba(70, 70, 70, 0.41);
  }

  .coordinate button {
    width: 100%;
    height: 42px;
    font-size: 16px;
    border-radius: 10px;
    margin-top: 15px;
    background: rgba(66, 66, 66, 0.41);
    box-shadow: 4px 4px 4px rgba(137, 207, 247, 0.18);
    color: white;
    border: none;
    outline: none;
  }

  .coordinate button:hover {
    cursor: pointer;
    transform: scale(1.05);
  }

</style>