<script type="ts">
    let value = "The adventures of a female reporter in the 1890s";
    let result = "";

    // todo form handling
    async function onSubmit(e) {
        const formData = new FormData(e.target);

        const data = {};
        for (let field of formData) {
            const [key, value] = field;
            data[key] = value;

        }


        console.log(data)

        const res = await fetch('/evaluate', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })


        const json = await res.json()
        result = JSON.stringify(json)
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
            <option value="1">Linear Regresion</option>
            <option value="2" selected>Convolutional Neural Network</option>
        </select>

        <p><label for="description">Enter your movie description:</label></p>
        <textarea id="description" name="description" rows="4" cols="50" bind:value></textarea>
        <br/>
        <input type="submit" value="Pounder">
    </form>

    <p>{result}</p>

</div>


<style>
    * {
        margin: 0;
        padding: 0;
    }

    #description {
        min-width: 360px;
        width: 100%;
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


</style>