<script lang="ts">
  import AutonomousPage from "./components/AutonomousPage.svelte";
	import DefaultPage from "./components/DefaultPage.svelte";
	import Menu from "./components/Menu.svelte";
	import QuickInfo from "./components/QuickInfo.svelte";
	import 'leaflet/dist/leaflet.css'

	import { current_screen_store, HomeScreen } from "./store";
  import SettingsPage from "./components/SettingsPage.svelte";
  import BiologyPage from "./components/BiologyPage.svelte";

    let current_screen: HomeScreen;
    current_screen_store.subscribe(screen => {current_screen = screen});

</script>

<main>
	<Menu></Menu>

	<div class="right-panel">
		<QuickInfo></QuickInfo>

		{#if current_screen == HomeScreen.DEFAULT}
			<DefaultPage />
		{:else if current_screen == HomeScreen.AUTONOMOUS}
			<AutonomousPage />
		{:else if current_screen == HomeScreen.SETTINGS}
			<SettingsPage />
		{:else if current_screen == HomeScreen.BIOLOGY}
			<BiologyPage />
		{/if}
	</div>
</main>

<style>
	main{
		width: 100%;
		min-height: 100vh;
		background-color: #1E1E1E;
		display: grid;
		grid-template-columns: .2fr .8fr;
	}

	.right-panel{
		display: flex;
		flex-direction: column;
	}
</style>