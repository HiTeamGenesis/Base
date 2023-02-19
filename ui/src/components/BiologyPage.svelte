<script>
  let firstTime = true
  let isFinished = false
  let isTesting = true
  let STEP_INDEX = -1
  const STEPS = [{"step": "1", "description": "La muestra está siendo recogida para su análisis", "short": "Recoger muestra del suelo"},
  {"step": "2", "description": "La muestra esa sindo triturada y se depositará en el tubo falcon #", "short": "La muestra se tritura y se depositará en el tubo falcon"},
  {"step": "3", "description": "La muestra está siendo transferida a la celda de cuarzo #", "short": "La muestra se transfiere a celda de cuarzo"},
  {"step": "4", "description": "Leyendo la onda de 255nm","short": "Se lee la onda de 255nm"},
  {"step": "5", "description": "Leyendo onda de 280nm", "short": "Se lee la onda de 280nm"},
  {"step": "6", "description": "Mostrando índice UV para las ondas", "short": "Se muestra el indice UV para las ondas"}]

  function startProcess() {
    firstTime = false;
    const intervalId = setInterval(() => {
      STEP_INDEX += 1
    }, 3000)

    if (STEP_INDEX >= 6) {
      isWorking = false;
      isFinished = true;
      STEP_INDEX = -1
      clearInterval(intervalId)
      return;
    }
  
    if (isTesting) {
      STEP_INDEX += 1
      isFinished = false;
    }

  }

</script>

<main class="steps">
  <div class="steps-current">
  {#if firstTime}
    <p>Start process</p>
    <button on:click={startProcess}>Go</button>
  {:else if isFinished && STEP_INDEX < 6}
    <p>Proccess has finished</p>
    <button on:click={startProcess}>Restart</button>
  {:else if STEP_INDEX < 6}
    <p>{`Step: ${STEPS[STEP_INDEX].step}`}</p>
    <p>{STEPS[STEP_INDEX].description}</p>
  {/if}
  </div>
  <div class="steps-list">
    {#each STEPS as step}
      {#if STEP_INDEX != -1 && STEP_INDEX < 6}
      <div class="steps-list-item {STEP_INDEX + 1  > parseInt(step.step) ? 'passed' : ''} {STEP_INDEX + 1 == parseInt(step.step) ? 'active' : ''} {parseInt(step.step) > STEP_INDEX ? 'toCome' : ''} ">
        <p>Step {step.step}</p>
        <span>{step.short}</span>
      </div>
      {/if}
    {/each}
  </div>
</main>

<style>
.steps {
  width: 100%;
  height: 100%;
  display: grid;
  grid-template-rows: .8fr .2fr;
  justify-content: center;
  align-items: center;
}

.steps-current {
  width: 100%;
  height: 100%;
  text-align: center;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  font-size: 16px;
  gap: 25px;
}

.steps-current p {
  font-size: 32px;
  font-weight: 500;
  color: #a7a7a7;
}

.steps-current button {
  width: 30%;
  border-radius: 8px;
  height: 30px;
  font-size: 16px;
  border-radius: 10px;
  margin-top: 15px;
  background: rgba(66, 66, 66, 0.41);
  box-shadow: 4px 4px 4px rgba(218, 137, 247, 0.18);
  color: white;
  border: none;
  outline: none;
  cursor: pointer;
}

.steps-list {
  max-width: 100%;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: flex-start;
  gap: 18px;
}

.steps-list-item {
  width: 115px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.steps-list-item p, span {
  color: #5d5d5d
}

.toCome p {
  color: rgb(74,74,74);
  text-decoration: none;
}

.toCome span {
  color: rgb(74, 74, 74);
  text-decoration: none;
}

.active p{
  text-decoration: none;
  color: #8f8f8f;
}

.active span{
  text-decoration: none;
  color: #8f8f8f;
}

.passed p, span{
  text-decoration: line-through;
  color: rgb(80, 80, 80);
}


</style>