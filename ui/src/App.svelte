<script lang="ts">
	import DefaultPage from "./components/DefaultPage.svelte";
	import 'leaflet/dist/leaflet.css'

	// import { current_screen_store, HomeScreen } from "./store";

  //   let current_screen: HomeScreen;
  //   current_screen_store.subscribe(screen => {current_screen = screen});

</script>

<main>
	<DefaultPage />
</main>

<style>
	main{
		width: 100%;
		height: 100vh;
		background-color: #1E1E1E;
		display: grid;
	}

</style>