<script type="ts">
    import {ConfettiExplosion} from 'svelte-confetti-explosion'

    let canClassify = true;
    let isVisible = false;
    let value = "The adventures of a female reporter in the 1890s";
    let result = "";

    async function onSubmit(e) {
        canClassify = false;
        isVisible = false;
        const formData = new FormData(e.target);
        const data = {};

        for (let field of formData) {
            const [key, value] = field;
            data[key] = value;

        }

        const res = await fetch('/evaluate', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        const json = await res.json();
        result = JSON.stringify(json);
        isVisible = true;
        canClassify = true;
    }

</script>

<div class="center">
    <hgroup>
        <h1>Intelligent movie classifier</h1>
        <h4>Made with love ❤️</h4>
    </hgroup>

    <form on:submit|preventDefault={onSubmit}>
        <p><label for="method">Machine learning method:</label></p>
        <select id="method" name="method">
            <option value="1" selected>Decision tree</option>
            <option value="2">K Neighbors</option>
            <option value="3">Logistic regression </option>
            <option value="4">Perceptron</option>
            <option value="5">Convolutional Neural Network</option>
        </select>

        <p><label for="description">Enter your movie description:</label></p>
        <textarea id="description" name="description" bind:value></textarea>
        <br/>
        {#if canClassify}
            <input type="submit" value="Pounder">
        {:else}
            <p>classifying in progress</p>
        {/if}
    </form>


    {#if isVisible}
        <p>{result}</p>
        <div>
            <ConfettiExplosion/>
        </div>
    {/if}


</div>


<style>
    * {
        margin: 0;
        padding: 0;
    }

    #description {
        min-height: 400px;
        min-width: 400px;
        width: 400px;
    }

    .center {
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
    }

    br {
        margin: 3pt;
    }

    hgroup {
        margin: 10pt;
    }

    :global(body) {
        overflow: hidden;
    }


</style>