<script>
    
</script>

<main>
    <div class="container">
        <div class="header">
            <p>FRONT CAMERA</p>
        </div>
    </div>

    <div class="container">
        <div class="header">
            <p>BACK CAMERA</p>
        </div>
    </div>

    <div class="container">
        <div class="header">
            <p>ARM CAMERA</p>
        </div>
    </div>

    <div class="container">
        <div class="header">
            <p>ARM CAMERA</p>
        </div>
    </div>

    <div class="container">
        <div class="header">
            <p>JOINT CAMERA</p>
        </div>
    </div>

    <div class="container">
        <div class="header">
            <p>GRIPPER CAMERA</p>
        </div>
    </div>
</main>

<style>

    main{
        max-width: 100%;
        display: grid;
        grid-template-columns: .5fr .5fr;
        justify-content: center;
        align-items: center;
        padding: 15px;
        gap: 15px;
    }

    .container{
        width: 100%;
        height: 350px;
        border-radius: 5px;
        border: 1px solid #2D2D2D;
    }

    .header{
        background-color: #2D2D2D;
        width: 100%;
        height: 2rem;
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: center;
    }

    .header p{
        color: #858585;
        font-weight: 300;
    }

</style>