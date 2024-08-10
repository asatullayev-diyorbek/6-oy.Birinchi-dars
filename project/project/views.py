from django.http import HttpResponse

style = """
            <style>
            *{
                margin: 0;
            }
            body{
                background-color: #1B1B1B;
                display: flex;
                justify-content: center;
                align-items: center;
                flex-direction: column;
                height: 100vh;
                width: 100%;
                }
            a{
                text-decoration: none;
                color: #E6EDF3;
                }
            a:hover{
                color: yellow;
                }
            h1, h3, p{
                padding: .5rem;
                text-align: center;
                color: yellow;
                }
            input{
                margin-top: 10px;
                width: 200px;
                height: 40px;
                padding: .5rem
                }
            .button {
                background-color: #4CAF50;
                color: white;
                padding: 10px 20px;
                border: none;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;
                cursor: pointer;
                border-radius: 4px;
              }
            
              /* Example 2: Adding a hover effect to a button */
              .button:hover {
                background-color: #45a049;
              }
            </style>
        """


def homepage(request):
    global style
    html_template = """
                <h1>Hello, This is homepage</h1>
                <h3><a href="first-url/">1. Birinchi url (Salomlashish)</a></h3>
                <h3><a href="second-url/">2. Ikkinchi url (Calculator: qo'shish)</a></h3>
                <h3><a href="third-url/">3. Uchinchi url (Calculator: ayirish)</a></h3>
                <h3><a href="fourth-url/">4. To'rtinchi url (Calculator: ko'paytirish)</a></h3>
                <h3><a href="fifth-url/">5. Beshinchi url (Calculator: bo'lish)</a></h3>
                <h3><a href="sixth-url/">6. Oltinchi url</a></h3>
                <h3><a href="seventh-url/">7. Yettinchi url</a></h3>
                <h3><a href="eighth-url/">8. Sakkizinchi url</a></h3>
                <h3><a href="ninth-url/">9. To'qqizinchi url</a></h3>
                <h3><a href="tenth-url/">10. O'ninchi url</a></h3>
            """

    html_template += style

    return HttpResponse(html_template)


def first_url(request):
    global style
    html_template = """
                <h1>This is 1 - url</h1>
                <h3>Salomlashish</h3>
                <input id="first_name" type="text" name='first_name' placeholder="Ismingiz...">
                <input type="button" class="button" value="Salomlashish" onclick="hello()">
                <p id="result"></p>
                <h3><a href="/">Back to homepage</a></h3>

                <script>
                    function hello() {
                        let name =document.getElementById('first_name').value;
                        document.getElementById('result').innerText='Assalomu alaykum, ' + name;
                    }
                </script>
                    """
    html_template += style
    return HttpResponse(html_template)


def second_url(request):
    global style
    html_template = """
        <h1>This is 2 - url</h1>
        <h3>Calculator (Qo'shish)</h3>
        <input id="value1" type="number" name='value1' placeholder="1-sonni kiriting">
        <input id="value2" type="number" name='value2' placeholder="2-sonni kiriting">
        <input type="button" class="button" value="Hisoblash" onclick="calculate()">
        <p id="result"></p>
        <h3><a href="/">Back to homepage</a></h3>

        <script>
            function calculate() {
                var value1 = parseFloat(document.getElementById('value1').value);
                var value2 = parseFloat(document.getElementById('value2').value);
                var result = value1 + value2;
                document.getElementById('result').innerText = 'Natija: ' + value1 + ' + ' + value2 + ' = ' + result;
            }
        </script>
        """
    html_template += style
    html_template += style
    return HttpResponse(html_template)


def third_url(request):
    global style
    html_template = """
            <h1>This is 3 - url</h1>
            <h3>Calculator (Ayirish)</h3>
            <input id="value1" type="number" name='value1' placeholder="1-sonni kiriting">
            <input id="value2" type="number" name='value2' placeholder="2-sonni kiriting">
            <input type="button" class="button" value="Hisoblash" onclick="calculate()">
            <p id="result"></p>
            <h3><a href="/">Back to homepage</a></h3>

            <script>
                function calculate() {
                    var value1 = parseFloat(document.getElementById('value1').value);
                    var value2 = parseFloat(document.getElementById('value2').value);
                    var result = value1 - value2;
                    document.getElementById('result').innerText = 'Natija: ' + value1 + ' - ' + value2 + ' = ' + result;
                }
            </script>
            """
    html_template += style
    return HttpResponse(html_template)


def fourth_url(request):
    global style
    html_template = """
                <h1>This is 4 - url</h1>
                <h3>Calculator (Ko'paytirish)</h3>
                <input id="value1" type="number" name='value1' placeholder="1-sonni kiriting">
                <input id="value2" type="number" name='value2' placeholder="2-sonni kiriting">
                <input type="button" class="button" value="Hisoblash" onclick="calculate()">
                <p id="result"></p>
                <h3><a href="/">Back to homepage</a></h3>

                <script>
                    function calculate() {
                        var value1 = parseFloat(document.getElementById('value1').value);
                        var value2 = parseFloat(document.getElementById('value2').value);
                        var result = value1 * value2;
                        document.getElementById('result').innerText='Natija: '+value1+' * '+value2 + ' = ' + result;
                    }
                </script>
                """
    html_template += style
    return HttpResponse(html_template)


def fifth_url(request):
    global style
    html_template = """
                <h1>This is 5 - url</h1>
                <h3>Calculator (Bo'lish)</h3>
                <input id="value1" type="number" name='value1' placeholder="1-sonni kiriting">
                <input id="value2" type="number" name='value2' placeholder="2-sonni kiriting">
                <input type="button" class="button" value="Hisoblash" onclick="calculate()">
                <p id="result"></p>
                <h3><a href="/">Back to homepage</a></h3>

                <script>
                    function calculate() {
                        var value1 = parseFloat(document.getElementById('value1').value);
                        var value2 = parseFloat(document.getElementById('value2').value);
                        var result = value1 / value2;
                        document.getElementById('result').innerText='Natija: '+value1+' : '+value2 + ' = ' + result;
                    }
                </script>
                """
    html_template += style
    return HttpResponse(html_template)


def sixth_url(request):
    global style
    html_template = """
                <h1>This is 6 - url</h1>
                <h3><a href="/">Back to homepage</a></h3>
                """
    html_template += style
    return HttpResponse(html_template)


def seventh_url(request):
    global style
    html_template = """
                <h1>This is 7 - url</h1>
                <h3><a href="/">Back to homepage</a></h3>
                    """
    html_template += style
    return HttpResponse(html_template)


def eighth_url(request):
    global style
    html_template = """
                <h1>This is 8 - url</h1>
                <h3><a href="/">Back to homepage</a></h3>
                    """
    html_template += style
    return HttpResponse(html_template)


def ninth_url(request):
    global style
    html_template = """
                <h1>This is 9 - url</h1>
                <h3><a href="/">Back to homepage</a></h3>
                    """
    html_template += style
    return HttpResponse(html_template)


def tenth_url(request):
    global style
    html_template = """
                <h1>This is 10 - url</h1>  
                <h3><a href="/">Back to homepage</a></h3>
                    """
    html_template += style
    return HttpResponse(html_template)

