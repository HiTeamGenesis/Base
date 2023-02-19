<script lang="ts">

</script>

<main>
        <div class="info">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="white">
                <path stroke-linecap="round" stroke-linejoin="round" d="M8.288 15.038a5.25 5.25 0 017.424 0M5.106 11.856c3.807-3.808 9.98-3.808 13.788 0M1.924 8.674c5.565-5.565 14.587-5.565 20.152 0M12.53 18.22l-.53.53-.53-.53a.75.75 0 011.06 0z" />
            </svg>
              
            <p>Connection: <span class="good">GOOD</span></p>
        </div>

        <div class="info">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="white">
                <path stroke-linecap="round" stroke-linejoin="round" d="M21 10.5h.375c.621 0 1.125.504 1.125 1.125v2.25c0 .621-.504 1.125-1.125 1.125H21M4.5 10.5h6.75V15H4.5v-4.5zM3.75 18h15A2.25 2.25 0 0021 15.75v-6a2.25 2.25 0 00-2.25-2.25h-15A2.25 2.25 0 001.5 9.75v6A2.25 2.25 0 003.75 18z" />
            </svg>
              
            <p>Batteries: <span class="warning">2 LOW</span></p>
        </div>

        <div class="info">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="white">
                <path stroke-linecap="round" stroke-linejoin="round" d="M17.25 6.75L22.5 12l-5.25 5.25m-10.5 0L1.5 12l5.25-5.25m7.5-3l-4.5 16.5" />
            </svg>
            <p>Processes: <span class="error">1 CRASHED</span></p>
        </div>

        <div class="info">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="white">
                <path stroke-linecap="round" stroke-linejoin="round" d="M8.25 3v1.5M4.5 8.25H3m18 0h-1.5M4.5 12H3m18 0h-1.5m-15 3.75H3m18 0h-1.5M8.25 19.5V21M12 3v1.5m0 15V21m3.75-18v1.5m0 15V21m-9-1.5h10.5a2.25 2.25 0 002.25-2.25V6.75a2.25 2.25 0 00-2.25-2.25H6.75A2.25 2.25 0 004.5 6.75v10.5a2.25 2.25 0 002.25 2.25zm.75-12h9v9h-9v-9z" />
              </svg>
            <p>Sensors: <span class="good">ALL GOOD</span></p>
        </div>

    <button class="off">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="white">
            <path stroke-linecap="round" stroke-linejoin="round" d="M5.636 5.636a9 9 0 1012.728 0M12 3v9" />
        </svg>

        <p>OFF</p>
    </button>

</main>

<style>
    main{
        max-width: 100%;
        height: 5vh;
        background-color: #161616;
        display: flex;
        flex-direction: row;
        justify-content: space-between;
    }


    .info{
        display: flex;
        flex-direction: row;
        align-items: center;
        user-select: none;
    }

    .info p{
        color: rgba(255, 255, 255, 0.651);
        margin-right: 0.5rem;
        font-size: 0.8rem;
    }

    .good{
        color: green;
    }

    .warning{
        color: #FFAC4F;
    }

    .error{
        color: #fa2169;
    }

    .info svg{
        width: 0.8rem;
        margin-right: 0.5rem;
        padding-left: 1vw;
    }

    .off{
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: center;
        padding: 0 8px;
        background-color: #2D2D2D;
        border: none;
        align-items: center;
        cursor: pointer;
    }

    .off:hover{
        background-color: #fa2169;
    }

    .off p{
        color: white;
    }

    .off svg{
        width: 1rem;
        margin-right: 0.8rem;
    }


</style>