<script>
  import LeftMenu from "./LeftMenu.svelte";

  let firstTime = true
  let isFinished = false
  let isTesting = true
  let STEP_INDEX = -1
  const STEPS = [{"step": "1", "description": "La muestra está siendo recogida para su análisis", "short": "Recoger muestra del suelo"},
  {"step": "2", "description": "La muestra esa sindo triturada y se depositará en el tubo falcon #", "short": "La muestra se tritura y se depositará en el tubo falcon"},
  {"step": "3", "description": "La muestra está siendo transferida a la celda de cuarzo #", "short": "La muestra se transfiere a celda de cuarzo"},
  {"step": "4", "description": "Leyendo la onda de 255nm","short": "Se lee la onda de 255nm"},
  {"step": "5", "description": "Leyendo onda de 280nm", "short": "Se lee la onda de 280nm"},
  {"step": "6", "description": "Mostrando índice UV para las ondas", "short": "Se muestra el indice UV para las ondas"}];

</script>

<div class="biology">
  <LeftMenu />
  <div class="biology-arms">
    <div class="biology-arms-item">CAM ARM</div>
    <div class="biology-arms-item">MAIN ARM</div>
  </div>
  <div class="steps">
    <div class="steps-current">
      <h3>STEPS</h3>
      <div class="steps-current-numbers">
        <p>1</p>
        <p>2</p>
        <p>3</p>
        <p>4</p>
      </div>
    </div>
    <div class="steps-list">
      <h3>Process 3/6</h3>
      <p>Lorem ipsum dolor sit amet consectetur, adipsicing elit. </p>
    </div>
  </div>
</div>

<style>

.biology {
  width: 100%;
  height: 50vh;
  display: grid;
  grid-template-columns: .2fr .6fr .2fr;
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
  background-color: green;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  border-radius: .6rem;
}

.steps {
  display: grid;
  height: 100%;
  grid-template-rows: .5fr .5fr;
  justify-content: center;
  align-items: center;
  gap: 2rem;
  padding: 0 2rem;
}

.steps-current {
  text-align: center;
  display: flex;
  flex-direction: column;
  height: 100%;
  width: 100%;
  justify-content: center;
  align-items: center;
  font-size: .8rem;
  background-color: rebeccapurple;
  border-radius: .6rem;
  gap: 1rem;
}

.steps-current h3 {
  font-size: 1.6rem;
}

.steps-current p {
  font-size: 1.6rem;
  border-radius: 100%;
  background-color: brown;
  padding: .4rem;
}

.steps-current-numbers {
  display: flex;
  flex-direction: row;
  gap: 1.4rem;
}

.steps-list {
  height: 100%;
  width: 100%;
  text-align: center;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  font-size: .8rem;
  background-color: rebeccapurple;
  border-radius: .6rem;
  gap: 1rem;
}

.steps-list h3 {
  font-size: 1.6rem;
}

.steps-list p {
  font-size: 1.2rem;
}

</style>