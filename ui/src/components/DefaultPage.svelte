<script>
    
</script>

<main>
    <div class="container-list">
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
    </div>

</main>

<style>

    main{
        display: flex;
        flex-direction: row;
    }

    .container-list{
        display: flex;
        flex-direction: row;
        padding-left: 5vw;
        padding-top: 5vh;
        flex-wrap: wrap;

    }

    .container{
        width: 330px;
        height: 350px;
        border-radius: 5px;
        border: 1px solid #2D2D2D;
        margin-right: 5vw;
        margin-bottom: 5vh;

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