console.log('Hello World')

const spinnerBox = document.getElementById('spinner-box')
const spinnerBox2 = document.getElementById('spinner-box-2')
const dataBox = document.getElementById('data-box')

// console.log(spinnerBox)
// console.log(dataBox)

$.ajax({
    type: 'GET',
    url: '/json/',
    success: function (response) {
        setTimeout(() => {
            spinnerBox.classList.add('not-visible')
            spinnerBox2.classList.add('not-visible')
            for (const item of response) {
                dataBox.innerHTML += `<b>${item.date}</b><p>${item.open}</p>`
            }

        }, 500)

    },
    error: function (error) {
        setTimeout(() => {
            dataBox.innerHTML = '<b>Failed to load the data!</b>'
        }, 500)
    }
})