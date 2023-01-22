<script lang="ts">
    import { current_screen_store, HomeScreen } from "../store";

    let current_screen: HomeScreen;
    current_screen_store.subscribe(screen => {current_screen = screen});

</script>

<main>
    <img class="logo" src="/logopng.png" alt="logo" />

    <div class="options">

        <button on:click={() => {current_screen_store.set(HomeScreen.DEFAULT)}} class={current_screen == HomeScreen.DEFAULT? "option gradient1" : "option"}>
            <p>Default</p>
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width={1.5} stroke="white">
                <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 12l8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25" />
            </svg>
        </button>

        <button on:click={() => {current_screen_store.set(HomeScreen.SERVICE)}}  class={current_screen == HomeScreen.SERVICE? "option gradient2" : "option"}>
            <p>Service</p>
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="white">
                <path stroke-linecap="round" stroke-linejoin="round" d="M11.42 15.17L17.25 21A2.652 2.652 0 0021 17.25l-5.877-5.877M11.42 15.17l2.496-3.03c.317-.384.74-.626 1.208-.766M11.42 15.17l-4.655 5.653a2.548 2.548 0 11-3.586-3.586l6.837-5.63m5.108-.233c.55-.164 1.163-.188 1.743-.14a4.5 4.5 0 004.486-6.336l-3.276 3.277a3.004 3.004 0 01-2.25-2.25l3.276-3.276a4.5 4.5 0 00-6.336 4.486c.091 1.076-.071 2.264-.904 2.95l-.102.085m-1.745 1.437L5.909 7.5H4.5L2.25 3.75l1.5-1.5L7.5 4.5v1.409l4.26 4.26m-1.745 1.437l1.745-1.437m6.615 8.206L15.75 15.75M4.867 19.125h.008v.008h-.008v-.008z" />
              </svg>
        </button>

        <button on:click={() => {current_screen_store.set(HomeScreen.DELIVERY)}}  class={current_screen == HomeScreen.DELIVERY? "option gradient1" : "option"}>
            <p>Delivery</p>
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="white">
                <path stroke-linecap="round" stroke-linejoin="round" d="M21 7.5l-9-5.25L3 7.5m18 0l-9 5.25m9-5.25v9l-9 5.25M3 7.5l9 5.25M3 7.5v9l9 5.25m0-9v9" />
            </svg>
        </button>

        <button on:click={() => {current_screen_store.set(HomeScreen.AUTONOMOUS)}}  class={current_screen == HomeScreen.AUTONOMOUS? "option gradient2" : "option"}>
            <p>Autonomy</p>
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="white">
                <path stroke-linecap="round" stroke-linejoin="round" d="M8.25 3v1.5M4.5 8.25H3m18 0h-1.5M4.5 12H3m18 0h-1.5m-15 3.75H3m18 0h-1.5M8.25 19.5V21M12 3v1.5m0 15V21m3.75-18v1.5m0 15V21m-9-1.5h10.5a2.25 2.25 0 002.25-2.25V6.75a2.25 2.25 0 00-2.25-2.25H6.75A2.25 2.25 0 004.5 6.75v10.5a2.25 2.25 0 002.25 2.25zm.75-12h9v9h-9v-9z" />
            </svg>
        </button>

        <button on:click={() => {current_screen_store.set(HomeScreen.BIOLOGY)}}  class={current_screen == HomeScreen.BIOLOGY? "option gradient1" : "option"}>
            <p>Biology</p>
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="white">
                <path stroke-linecap="round" stroke-linejoin="round" d="M9.75 3.104v5.714a2.25 2.25 0 01-.659 1.591L5 14.5M9.75 3.104c-.251.023-.501.05-.75.082m.75-.082a24.301 24.301 0 014.5 0m0 0v5.714c0 .597.237 1.17.659 1.591L19.8 15.3M14.25 3.104c.251.023.501.05.75.082M19.8 15.3l-1.57.393A9.065 9.065 0 0112 15a9.065 9.065 0 00-6.23-.693L5 14.5m14.8.8l1.402 1.402c1.232 1.232.65 3.318-1.067 3.611A48.309 48.309 0 0112 21c-2.773 0-5.491-.235-8.135-.687-1.718-.293-2.3-2.379-1.067-3.61L5 14.5" />
            </svg>
        </button>

        <button on:click={() => {current_screen_store.set(HomeScreen.TEST)}}  class={current_screen == HomeScreen.TEST? "option gradient2" : "option"}>
            <p>Test</p>
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="white">
                <path stroke-linecap="round" stroke-linejoin="round" d="M3.75 13.5l10.5-11.25L12 10.5h8.25L9.75 21.75 12 13.5H3.75z" />
            </svg>
        </button>

        <button on:click={() => {current_screen_store.set(HomeScreen.SETTINGS)}}  class={current_screen == HomeScreen.SETTINGS? "option gradient1" : "option"}>
            <p>Settings</p>
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="white">
                <path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12a7.5 7.5 0 0015 0m-15 0a7.5 7.5 0 1115 0m-15 0H3m16.5 0H21m-1.5 0H12m-8.457 3.077l1.41-.513m14.095-5.13l1.41-.513M5.106 17.785l1.15-.964m11.49-9.642l1.149-.964M7.501 19.795l.75-1.3m7.5-12.99l.75-1.3m-6.063 16.658l.26-1.477m2.605-14.772l.26-1.477m0 17.726l-.26-1.477M10.698 4.614l-.26-1.477M16.5 19.794l-.75-1.299M7.5 4.205L12 12m6.894 5.785l-1.149-.964M6.256 7.178l-1.15-.964m15.352 8.864l-1.41-.513M4.954 9.435l-1.41-.514M12.002 12l-3.75 6.495" />
            </svg>
        </button>
    </div>

</main>

<style>
    main {
        width: 30vw;
        min-height: 100vh;
        background-color: #161616;
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .logo{
        width: 5vw;
        margin-top: 5vh;
    }

    .options{
        display: flex;
        flex-direction: column;
        margin-top: 10vh;
        width: 100%;
        justify-content: center;
        align-items: center;
    }

    .option{
        display: flex;
        flex-direction: row;
        user-select: none;
        align-items: center;
        cursor: pointer;
        /* padding: 0.5rem 2.5rem; */
        padding: 0.5rem 0rem;
        width: 80%;
        align-items: center;
        justify-content: center;
        border-radius: 2rem;
        margin-top: 1rem;
        border: none;
        background-color: transparent;
    }

    .option p{
        font-size: 1.3rem;
        color: white;
        font-weight: 300;
        margin-right: 1rem;
    }

    .option svg{
        width: 1.5rem;
    }

    .gradient1{
        background: linear-gradient(to right, #B562E9, #F6C271);
    }
    .gradient2{
        background: linear-gradient(#CA9BDE, #9DD0F7);
    }
</style>
