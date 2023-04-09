function greet() {
    alert("working");
}

function search() {
    var item = document.getElementById('searchbar').value
    var url = "https://www.youtube.com/results?search_query=" + item;
    window.open(url, "_parent");
}

function showLinks() {
    var links = document.getElementById('mylinks');
    if (links.style.display === "none") {
        links.style.display = "block";
    } else {
        links.style.display = "none";
    }
}

function showWebsites() {
    return (
        <html>
        <div class="websites">
            <h2>We have following websites to attack:</h2>
            <ul>
                <a class="link" href="http://127.0.0.1:5500/index_1.html">Dummy</a>
            </ul>
            <ul>
                <a class="link" href="" target="_blank">Yet to come</a>
            </ul>
        </div>
        </html>
    )
}