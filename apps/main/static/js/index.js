document.addEventListener('DOMContentLoaded', function() {
    const delay = ms => new Promise(res => setTimeout(res, ms))

    function decodeHtml(html) {
        var txt = document.createElement("textarea");
        txt.innerHTML = html;
        return txt.value;
    }

    async function typewrite(inputText, target) {
        textLength = inputText.length
        for (let letter of inputText) {
            await delay(50 - textLength)
            target.innerHTML += letter
        }
    }

    async function processTypewrites(){
        typewriteList = document.getElementsByClassName('typewrite')
        typewriteElementsInner = []

        for (textElement of typewriteList) {
            typewriteElementsInner.push(textElement.innerHTML)
            textElement.innerHTML = ''
        }

        for (textElement of typewriteElementsInner) {
            i = typewriteElementsInner.indexOf(textElement)
            text = decodeHtml(textElement)
            await typewrite(text, typewriteList[i])
        }
    }

    async function handleAnimation() {
        await processTypewrites()
        document.querySelector('article#PersonalStatement').classList.add('display')
    }

    handleAnimation()
})
