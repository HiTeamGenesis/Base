<script>

</script>

<main class="settings">
  <div class="settings-section">
    <div class="settings-section-header">
      <p>SIGNALS</p>
    </div>
    <div class="settings-section-signals">
      <div class="signals-channel">
        <p>2.4Ghz channel</p>
        <form>
          <div>
            <label class="radio-control" for="channel1">
              <input type="radio" id="channel1" name="channel" value={1}>
              1
            </label>
          </div>
          <div>
            <label class="radio-control" for="channel2">
              <input type="radio" id="channel2" name="channel" value={2}>
              2
            </label>
          </div>
          <div>
            <label class="radio-control" for="channel3">
              <input type="radio" id="channel3" name="channel" value={3}>
              3
            </label>
          </div>
          <div>
            <label class="radio-control" for="channel4">
              <input type="radio" id="channel4" name="channel" value={4}>
              4
            </label>
          </div>
          <div>
            <label class="radio-control" for="channel5">
              <input type="radio" id="channel5" name="channel" value={5}>
              5
            </label>
          </div>
          <div>
            <label class="radio-control" for="channel6">
              <input type="radio" id="channel6" name="channel" value={6}>
              6
            </label>
          </div>
        </form>
      </div>
      <div class="signals-freq">
        <p>900mhz frequency</p>
        <form>
          <div>
            <label class="radio-control" for="low">
              <input type="radio" id="low" name="freq" value="Low">
              Low
            </label>
          </div>
          <div>
            <label class="radio-control" for="medium">
              <input type="radio" id="medium" name="freq" value="Medium">
              Medium
            </label>
          </div>
          <div>
            <label class="radio-control" for="high">
              <input type="radio" id="high" name="freq" value="High">
              High
            </label>
          </div>
        </form>
      </div>
    </div>
  </div>
  <div class="settings-section">
    <div class="settings-section-header">
      <p>BIOLOGY</p>
    </div>
  </div>
  <div class="settings-section">
    <div class="settings-section-header">
      <p>AUTONOMY</p>
    </div>
  </div>
  <div class="settings-section">
    <div class="settings-section-header">
      <p>DELIVERY</p>
    </div>
  </div>
</main>

<style>
.settings {
  max-width: 100%;
  height: 100%;
  display: grid;
  grid-template-columns: .5fr .5fr;
  grid-template-rows: .5fr .5fr;
  justify-content: center;
  align-items: center;
  padding: 15px;
  gap: 15px;
}

.settings-section {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  border-radius: 5px;
  align-items: center;
  text-align: center;
  border: 3px solid #2d2d2d;
}

.settings-section-header {
  width: 100%;
  height: 2.2rem;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #2d2d2d;
}

.settings-section-header p {
  color: #c5c5c5d9;
  font-weight: 500;
}

.settings-section-signals {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 45px;
}

.settings-section-signals p {
  font-size: 22px;
  color: #a0a0a0;
  margin-bottom: 12px;
}

.settings-section-signals form{
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  justify-content: center;
  gap: 10px;
}

.radio-control {
  font-size: 20px;
  margin-left: 10px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  color: #858585;
  gap: 4px;
}

input[type="radio"] { 
  appearance: none;
  background-color: #cf95ffab;
  margin: 0;
  font: inherit;
  color: #cf95ffab;
  width: 1em;
  height: 1em;
  border: 0.15em solid #cf95ffab;
  border-radius: 50%;
  transform: translate(-0.075em);
  display: grid;
  place-content: center;
  cursor: pointer;
}

input[type="radio"]::before {
  content: "";
  width: 0.65em;
  height: 0.65em;
  border-radius: 50%;
  transform: scale(0);
  transition: 120ms transform ease-in-out;
  box-shadow: inset 1em 1em rgba(255, 184, 77, 0.862);
}

input[type="radio"]:checked::before {
  transform: scale(1);
}


</style>