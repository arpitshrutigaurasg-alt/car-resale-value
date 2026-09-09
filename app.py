from flask import Flask, request, render_template_string, send_from_directory
import numpy as np

from model import model, poly


# ==========================================
# FLASK APP
# ==========================================

app = Flask(__name__)


# ==========================================
# BACKGROUND IMAGE
# ==========================================

@app.route("/car_background.png")
def car_background():

    return send_from_directory(
        app.root_path,
        "car_background.png"
    )


# ==========================================
# HTML + CSS
# ==========================================

HTML = """

<!DOCTYPE html>

<html>

<head>

    <meta charset="UTF-8">

    <meta name="viewport"
          content="width=device-width, initial-scale=1.0">

    <title>Cars | Resale Price Predictor</title>


    <style>

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }


        body {

            font-family: Arial, Helvetica, sans-serif;

            min-height: 100vh;

            color: white;

            background: #020711;

            overflow-x: hidden;
        }


        /* =====================================
           BACKGROUND IMAGE
        ===================================== */

        .background {

            position: fixed;

            inset: 0;

            width: 100%;
            height: 100%;

            background-image:

                linear-gradient(
                    rgba(1, 7, 18, 0.55),
                    rgba(1, 7, 18, 0.90)
                ),

                url("/car_background.png");

            background-size: cover;

            background-position: center;

            background-repeat: no-repeat;

            z-index: -3;

            animation:
                backgroundMove 15s
                ease-in-out infinite alternate;
        }


        @keyframes backgroundMove {

            0% {

                transform: scale(1);

                background-position:
                    center center;
            }

            100% {

                transform: scale(1.06);

                background-position:
                    52% center;
            }
        }


        /* =====================================
           BLUE LIGHT EFFECT
        ===================================== */

        .blue-glow {

            position: fixed;

            width: 500px;

            height: 500px;

            border-radius: 50%;

            background:
                rgba(0, 110, 255, 0.12);

            filter: blur(110px);

            top: 20%;

            left: 5%;

            z-index: -2;

            animation:
                glowMove 8s
                ease-in-out infinite alternate;
        }


        @keyframes glowMove {

            from {

                transform:
                    translate(0, 0);
            }

            to {

                transform:
                    translate(100px, 50px);
            }
        }


        /* =====================================
           NAVBAR
        ===================================== */

        nav {

            height: 75px;

            display: flex;

            align-items: center;

            justify-content: space-between;

            padding: 0 6%;

            background:
                rgba(2, 8, 20, 0.78);

            border-bottom:
                1px solid
                rgba(255,255,255,0.08);

            backdrop-filter:
                blur(15px);
        }


        .logo {

            display: flex;

            align-items: center;

            gap: 12px;

            font-size: 22px;

            font-weight: bold;
        }


        .logo-icon {

            width: 43px;

            height: 43px;

            display: flex;

            align-items: center;

            justify-content: center;

            border-radius: 12px;

            background:
                rgba(0, 130, 255, 0.15);

            border:
                1px solid
                rgba(0, 150, 255, 0.35);

            font-size: 24px;
        }


        .blue {

            color: #2495ff;
        }


        .nav-right {

            color: #91a0b8;

            font-size: 13px;
        }


        .nav-dot {

            color: #1688ff;

            margin: 0 10px;
        }


        /* =====================================
           MAIN
        ===================================== */

        .main {

            min-height:
                calc(100vh - 75px);

            display: flex;

            justify-content: space-between;

            align-items: center;

            gap: 70px;

            padding: 50px 7%;
        }


        /* =====================================
           LEFT SECTION
        ===================================== */

        .left {

            width: 48%;

            animation:
                leftAppear 1s ease;
        }


        @keyframes leftAppear {

            from {

                opacity: 0;

                transform:
                    translateX(-60px);
            }

            to {

                opacity: 1;

                transform:
                    translateX(0);
            }
        }


        .badge {

            display: inline-block;

            padding:
                9px 17px;

            border-radius: 30px;

            color: #4daaff;

            background:
                rgba(0, 120, 255, 0.13);

            border:
                1px solid
                rgba(0, 140, 255, 0.35);

            font-size: 12px;

            letter-spacing: 1.5px;

            margin-bottom: 22px;
        }


        .left h1 {

            font-size: 58px;

            line-height: 1.08;

            letter-spacing: -2px;

            margin-bottom: 22px;
        }


        .blue-text {

            color: #168cff;

            text-shadow:
                0 0 30px
                rgba(22,140,255,0.45);
        }


        .description {

            max-width: 520px;

            color: #aab8cd;

            font-size: 16px;

            line-height: 1.7;

            margin-bottom: 35px;
        }


        /* =====================================
           FEATURES
        ===================================== */

        .features {

            display: flex;

            gap: 18px;

            flex-wrap: wrap;
        }


        .feature {

            display: flex;

            align-items: center;

            gap: 9px;

            color: #a9b6ca;

            font-size: 12px;

            padding-right: 18px;

            border-right:
                1px solid
                rgba(255,255,255,0.1);
        }


        .feature:last-child {

            border-right: none;
        }


        .feature-icon {

            width: 35px;

            height: 35px;

            display: flex;

            align-items: center;

            justify-content: center;

            border-radius: 50%;

            background:
                rgba(0,120,255,0.15);

            border:
                1px solid
                rgba(0,140,255,0.25);

            font-size: 17px;
        }


        /* =====================================
           PREDICTION CARD
        ===================================== */

        .card {

            width: 490px;

            padding: 32px;

            border-radius: 24px;

            background:
                rgba(3, 12, 28, 0.82);

            border:
                1px solid
                rgba(39, 145, 255, 0.55);

            backdrop-filter:
                blur(20px);

            box-shadow:

                0 25px 80px
                rgba(0,0,0,0.5),

                0 0 50px
                rgba(0,100,255,0.12);

            animation:
                cardAppear 1s ease;
        }


        @keyframes cardAppear {

            from {

                opacity: 0;

                transform:
                    translateX(60px)
                    scale(0.96);
            }

            to {

                opacity: 1;

                transform:
                    translateX(0)
                    scale(1);
            }
        }


        /* =====================================
           CARD HEADER
        ===================================== */

        .card-header {

            display: flex;

            align-items: center;

            gap: 15px;

            padding-bottom: 22px;

            margin-bottom: 25px;

            border-bottom:
                1px solid
                rgba(255,255,255,0.08);
        }


        .card-car-icon {

            width: 50px;

            height: 50px;

            display: flex;

            align-items: center;

            justify-content: center;

            border-radius: 14px;

            background:
                rgba(0,120,255,0.13);

            border:
                1px solid
                rgba(0,140,255,0.35);

            font-size: 28px;
        }


        .card-header h2 {

            font-size: 23px;

            margin-bottom: 5px;
        }


        .card-header p {

            color: #7f90a8;

            font-size: 12px;
        }


        /* =====================================
           INPUT GRID
        ===================================== */

        .input-grid {

            display: grid;

            grid-template-columns:
                1fr 1fr;

            gap: 18px;
        }


        .input-group label {

            display: block;

            color: #aebbd0;

            font-size: 12px;

            font-weight: bold;

            margin-bottom: 8px;
        }


        .input-wrapper {

            position: relative;
        }


        .input-icon {

            position: absolute;

            left: 14px;

            top: 50%;

            transform:
                translateY(-50%);

            color: #268fff;

            font-size: 16px;

            z-index: 1;
        }


        input {

            width: 100%;

            height: 48px;

            padding:
                0 12px 0 40px;

            border-radius: 10px;

            border:
                1px solid
                rgba(255,255,255,0.12);

            background:
                rgba(255,255,255,0.045);

            color: white;

            outline: none;

            font-size: 14px;

            transition:
                all 0.3s ease;
        }


        input::placeholder {

            color: #52647d;
        }


        input:focus {

            border-color:
                #238fff;

            background:
                rgba(10,45,85,0.45);

            box-shadow:
                0 0 18px
                rgba(35,143,255,0.18);
        }


        /* =====================================
           BUTTON
        ===================================== */

        .predict-button {

            width: 100%;

            height: 53px;

            margin-top: 25px;

            border: none;

            border-radius: 12px;

            color: white;

            font-size: 15px;

            font-weight: bold;

            cursor: pointer;

            background:
                linear-gradient(
                    90deg,
                    #087cff,
                    #2868ff
                );

            box-shadow:
                0 10px 30px
                rgba(0,110,255,0.25);

            transition:
                all 0.3s ease;
        }


        .predict-button:hover {

            transform:
                translateY(-3px);

            box-shadow:
                0 15px 40px
                rgba(0,110,255,0.45);
        }


        .predict-button:active {

            transform:
                translateY(0);
        }


        /* =====================================
           RESULT
        ===================================== */

        .result {

            margin-top: 22px;

            padding: 20px;

            border-radius: 15px;

            background:
                linear-gradient(
                    135deg,
                    rgba(0,200,170,0.11),
                    rgba(0,80,130,0.13)
                );

            border:
                1px solid
                rgba(0,210,180,0.38);

            animation:
                resultAppear 0.6s ease;
        }


        @keyframes resultAppear {

            from {

                opacity: 0;

                transform:
                    translateY(15px)
                    scale(0.95);
            }

            to {

                opacity: 1;

                transform:
                    translateY(0)
                    scale(1);
            }
        }


        .result-top {

            display: flex;

            justify-content: space-between;

            align-items: center;

            margin-bottom: 8px;
        }


        .result-label {

            color: #8799b0;

            font-size: 12px;
        }


        .result-icon {

            color: #18dfb5;

            font-size: 20px;
        }


        .price {

            color: #18dfb5;

            font-size: 32px;

            font-weight: bold;

            text-shadow:
                0 0 20px
                rgba(24,223,181,0.25);
        }


        /* =====================================
           ERROR
        ===================================== */

        .error {

            margin-top: 18px;

            padding: 13px;

            border-radius: 10px;

            background:
                rgba(255,50,50,0.10);

            border:
                1px solid
                rgba(255,80,80,0.35);

            color: #ff7777;

            font-size: 12px;
        }


        /* =====================================
           FOOTER
        ===================================== */

        .footer {

            text-align: center;

            margin-top: 22px;

            color: #586a82;

            font-size: 10px;

            letter-spacing: 0.5px;
        }


        /* =====================================
           RESPONSIVE
        ===================================== */

        @media (max-width: 1000px) {

            .main {

                flex-direction: column;

                padding:
                    50px 25px;
            }


            .left {

                width: 100%;

                text-align: center;
            }


            .description {

                margin-left: auto;

                margin-right: auto;
            }


            .features {

                justify-content: center;
            }


            .card {

                width: 100%;

                max-width: 500px;
            }

        }


        @media (max-width: 600px) {

            nav {

                padding:
                    0 20px;
            }


            .nav-right {

                display: none;
            }


            .left h1 {

                font-size: 40px;
            }


            .input-grid {

                grid-template-columns:
                    1fr;
            }


            .card {

                padding: 22px;
            }

        }

    </style>

</head>


<body>


    <!-- BACKGROUND -->

    <div class="background"></div>

    <div class="blue-glow"></div>



    <!-- NAVBAR -->

    <nav>


        <div class="logo">


            <div class="logo-icon">

                🚗

            </div>


            <div>

                <span class="blue">
                    Cars
                </span>

                Resale Predictor

            </div>


        </div>



        <div class="nav-right">

            Smarter Decisions

            <span class="nav-dot">
                •
            </span>

            Better Deals

        </div>


    </nav>



    <!-- MAIN -->

    <div class="main">


        <!-- LEFT SECTION -->

        <div class="left">


            <div class="badge">

                ✦ AI POWERED

            </div>



            <h1>

                Know Your Car's

                <br>

                <span class="blue-text">

                    True Value

                </span>

            </h1>



            <p class="description">

                Enter your car details and get an
                instant resale price prediction
                powered by Machine Learning.

            </p>



            <!-- FEATURES -->

            <div class="features">


                <div class="feature">

                    <div class="feature-icon">
                        ⚡
                    </div>

                    Fast
                    <br>
                    Prediction

                </div>



                <div class="feature">

                    <div class="feature-icon">
                        ◎
                    </div>

                    Accurate
                    <br>
                    Results

                </div>



                <div class="feature">

                    <div class="feature-icon">
                        🧠
                    </div>

                    Smart
                    <br>
                    Model

                </div>



                <div class="feature">

                    <div class="feature-icon">
                        ✓
                    </div>

                    Trusted
                    <br>
                    Analysis

                </div>


            </div>


        </div>



        <!-- RIGHT CARD -->

        <div class="card">


            <div class="card-header">


                <div class="card-car-icon">

                    🚘

                </div>


                <div>

                    <h2>

                        Car Resale Price

                    </h2>


                    <p>

                        Enter your car details below

                    </p>

                </div>


            </div>



            <!-- FORM -->

            <form method="POST">


                <div class="input-grid">


                    <!-- AGE -->

                    <div class="input-group">


                        <label>

                            Car Age (Years)

                        </label>


                        <div class="input-wrapper">


                            <div class="input-icon">

                                ◷

                            </div>


                            <input

                                type="number"

                                name="age"

                                placeholder="e.g. 3"

                                min="0"

                                step="any"

                                required

                            >


                        </div>


                    </div>



                    <!-- KM -->

                    <div class="input-group">


                        <label>

                            Kilometers Driven

                        </label>


                        <div class="input-wrapper">


                            <div class="input-icon">

                                ◉

                            </div>


                            <input

                                type="number"

                                name="km"

                                placeholder="e.g. 35000"

                                min="0"

                                step="any"

                                required

                            >


                        </div>


                    </div>



                    <!-- ENGINE -->

                    <div class="input-group">


                        <label>

                            Engine CC

                        </label>


                        <div class="input-wrapper">


                            <div class="input-icon">

                                ⚙

                            </div>


                            <input

                                type="number"

                                name="engine"

                                placeholder="e.g. 1500"

                                min="1"

                                step="any"

                                required

                            >


                        </div>


                    </div>



                    <!-- OWNER -->

                    <div class="input-group">


                        <label>

                            Owner Count

                        </label>


                        <div class="input-wrapper">


                            <div class="input-icon">

                                ♙

                            </div>


                            <input

                                type="number"

                                name="owner"

                                placeholder="e.g. 1"

                                min="0"

                                step="1"

                                required

                            >


                        </div>


                    </div>


                </div>



                <!-- BUTTON -->

                <button

                    type="submit"

                    class="predict-button"

                >

                    ✨ Predict Resale Price
                    &nbsp; →

                </button>


            </form>



            <!-- RESULT -->

            {% if result %}


            <div class="result">


                <div class="result-top">


                    <div class="result-label">

                        ESTIMATED RESALE PRICE

                    </div>


                    <div class="result-icon">

                        ✓

                    </div>


                </div>


                <div class="price">

                    {{ result }}

                </div>


            </div>


            {% endif %}



            <!-- ERROR -->

            {% if error %}


            <div class="error">

                {{ error }}

            </div>


            {% endif %}



            <div class="footer">

                Powered by Ridge Regression
                • Polynomial Features

            </div>


        </div>


    </div>


</body>

</html>

"""


# ==========================================
# HOME ROUTE
# ==========================================

@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    error = None


    if request.method == "POST":

        try:

            # Get values from website

            age = float(
                request.form["age"]
            )

            km = float(
                request.form["km"]
            )

            engine = float(
                request.form["engine"]
            )

            owner = float(
                request.form["owner"]
            )


            # Validation

            if age < 0:

                error = (
                    "Car age cannot be negative."
                )


            elif km < 0:

                error = (
                    "Kilometers cannot be negative."
                )


            elif engine <= 0:

                error = (
                    "Engine CC must be greater than 0."
                )


            elif owner < 0:

                error = (
                    "Owner count cannot be negative."
                )


            else:

                # Create input array

                user_input = np.array([
                    [
                        age,
                        km,
                        engine,
                        owner
                    ]
                ])


                # Polynomial transformation

                user_poly = poly.transform(
                    user_input
                )


                # Prediction

                prediction = model.predict(
                    user_poly
                )[0]


                # Display result

                result = (
                    f"₹ {prediction:.2f} Lakh"
                )


        except Exception as e:

            print(
                "ERROR:",
                e
            )

            error = f"Error: {e}"


    return render_template_string(
        HTML,
        result=result,
        error=error
    )


# ==========================================
# RUN APP
# ==========================================

if __name__ == "__main__":

    app.run(
        debug=True
    )
