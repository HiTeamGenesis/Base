<script lang="ts">
  import AutonomousPage from "./components/AutonomousPage.svelte";
	import DefaultPage from "./components/DefaultPage.svelte";
import Menu from "./components/Menu.svelte";
	import QuickInfo from "./components/QuickInfo.svelte";

	import { current_screen_store, HomeScreen } from "./store";

    let current_screen: HomeScreen;
    current_screen_store.subscribe(screen => {current_screen = screen});

</script>

<main>
	<Menu></Menu>

	<div class="right-panel">
		<QuickInfo></QuickInfo>
		<div></div>

		{#if current_screen == HomeScreen.DEFAULT}
			<DefaultPage></DefaultPage>
		{:else if current_screen == HomeScreen.AUTONOMOUS}
			<AutonomousPage></AutonomousPage>
		{/if}
	</div>
</main>

<style>
	main{
		width: 100vw;
		min-height: 100vh;
		background-color: #1E1E1E;
		display: flex;
		flex-direction: row;
	}

	.right-panel{
		display: flex;
		flex-direction: column;
	}
</style>