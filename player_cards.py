import pandas as pd
import dash

from dash import Dash, html

app = Dash()

app.layout = (
    #container for whole web page
    html.Div (
            #HEADER
    [html.H1("UNC MEN'S BASKETBALL ROSTER 24-25")], className="header"),

        #CONTAINER FOR ALL PLAYER CARDS
        html.Div([

        #CONTAINER FOR CARD 1
        html.Div([
            #FRONT-BACK OF CARD FUNCTINOALITY
            html.Div(
                [
                    # FRONT OF CARD FUNCTIONALITY
                    html.Div(
                        [
                            #HEADSHOT FOR PLAYER 1
                            html.Img(
                                src="https://images.sidearmdev.com/crop?url=https%3A%2F%2Fdxbhsrqyrr690.cloudfront.net%2Fsidearm.nextgen.sites%2Func.sidearmsports.com%2Fimages%2F2024%2F10%2F2%2FCadeau_Elliot.mb.21_5bsCH.JPG&width=180&height=270&type=webp",
                                style={"width": "220px", "height": "250px"},
                            )
                        ],
                        className="flip-card-front",
                    ),
                    # BACK OF CARD
                    html.Div([
                        html.H1("Elliot Cadeau"),
                        html.H3("G | So | 6\'1\" "),
                        html.H3("West Orange, N.J."),
                        html.H3("Link Academy (Branson, Mo.)")],
                        className="flip-card-back"),
                ],
                className="flip-card-inner"
            ),
        ], className="flip-card",
), #CONTAINER FOR CARD 2
        html.Div([
            #FRONT-BACK OF CARD FUNCTINOALITY
            html.Div(
                [
                    # FRONT OF CARD FUNCTIONALITY
                    html.Div(
                        [
                            #HEADSHOT FOR PLAYER 2
                            html.Img(
                                src="https://images.sidearmdev.com/crop?url=https%3A%2F%2Fdxbhsrqyrr690.cloudfront.net%2Fsidearm.nextgen.sites%2Func.sidearmsports.com%2Fimages%2F2024%2F10%2F2%2FDavis_RJ.mb.18_PjZAX.JPG&width=180&height=270&type=webp",
                                style={"width": "220px", "height": "250px"},
                            )
                        ],
                        className="flip-card-front",
                    ),
                    # BACK OF CARD
                    html.Div([
                        html.H1("RJ Davis"),
                        html.H3("G | Gr | 6\'0\""),
                        html.H3("White Plains, N.Y."),
                        html.H3("Archbishop Stepinac")
                    ], className="flip-card-back"),
                ],
                className="flip-card-inner"
            ),
        ], className="flip-card",
),
#CONTAINER FOR CARD3
        html.Div([
            #FRONT-BACK OF CARD FUNCTINOALITY
            html.Div(
                [
                    # FRONT OF CARD FUNCTIONALITY
                    html.Div(
                        [
                            #HEADSHOT FOR PLAYER 3
                            html.Img(
                                src="https://images.sidearmdev.com/crop?url=https%3A%2F%2Fdxbhsrqyrr690.cloudfront.net%2Fsidearm.nextgen.sites%2Func.sidearmsports.com%2Fimages%2F2024%2F10%2F2%2FTrimble_Seth.mb.19_80h8J.JPG&width=180&height=270&type=webp",
                                style={"width": "220px", "height": "250px"},
                            )
                        ],
                        className="flip-card-front",
                    ),
                    # BACK OF CARD
                    html.Div([
                        html.H1("Seth Trimble"),
                        html.H3("G | Jr | 6\'3\""),
                        html.H3("Menomonee Falls, Wis."),
                        html.H3("Menomonee Falls")
                    ], className="flip-card-back"),
                ],
                className="flip-card-inner"
            ),
        ], className="flip-card",
),
#CONTAINER FOR CARD 4
        html.Div([
            #FRONT-BACK OF CARD FUNCTINOALITY
            html.Div(
                [
                    # FRONT OF CARD FUNCTIONALITY
                    html.Div(
                        [
                            #HEADSHOT FOR PLAYER4
                            html.Img(
                                src="https://images.sidearmdev.com/crop?url=https%3A%2F%2Fdxbhsrqyrr690.cloudfront.net%2Fsidearm.nextgen.sites%2Func.sidearmsports.com%2Fimages%2F2024%2F10%2F2%2FPowell_Drake.mb.25_oaQV2.JPG&width=180&height=270&type=webp",
                                style={"width": "220px", "height": "250px"},
                            )
                        ],
                        className="flip-card-front",
                    ),
                    # BACK OF CARD
                    html.Div([
                        html.H1("Drake Powell"),
                        html.H3("G/F | Fr. | 6\'6\""),
                        html.H3("Pittsboro, N.C."),
                        html.H3("Northwood")
                              ], className="flip-card-back"),
                ],
                className="flip-card-inner"
            ),
        ], className="flip-card",
),
#CONTAINER FOR CARD 5
        html.Div([
            #FRONT-BACK OF CARD FUNCTINOALITY
            html.Div(
                [
                    # FRONT OF CARD FUNCTIONALITY
                    html.Div(
                        [
                            #HEADSHOT FOR PLAYER5
                            html.Img(
                                src="https://images.sidearmdev.com/crop?url=https%3A%2F%2Fdxbhsrqyrr690.cloudfront.net%2Fsidearm.nextgen.sites%2Func.sidearmsports.com%2Fimages%2F2024%2F10%2F2%2FJackson_Ian.mb.24_mL3O6.JPG&width=180&height=270&type=webp",
                                style={"width": "220px", "height": "250px"},
                            )
                        ],
                        className="flip-card-front",
                    ),
                    # BACK OF CARD
                    html.Div([
                        html.H1("Ian Jackson"),
                        html.H3("G | Fr. | 6\'4\""),
                        html.H3("The Bronx, N.Y."),
                        html.H3("Our Saviour Lutheran")
                              ], className="flip-card-back"),
                ],
                className="flip-card-inner"
            ),
        ], className="flip-card",
),
#CONTAINER FOR CARD6
        html.Div([
            #FRONT-BACK OF CARD FUNCTINOALITY
            html.Div(
                [
                    # FRONT OF CARD FUNCTIONALITY
                    html.Div(
                        [
                            #HEADSHOT FOR PLAYER6
                            html.Img(
                                src="https://images.sidearmdev.com/crop?url=https%3A%2F%2Fdxbhsrqyrr690.cloudfront.net%2Fsidearm.nextgen.sites%2Func.sidearmsports.com%2Fimages%2F2024%2F10%2F2%2FWashington_Jalen.mb.20_D2EoH.JPG&width=180&height=270&type=webp",
                                style={"width": "220px", "height": "250px"},
                            )
                        ],
                        className="flip-card-front",
                    ),
                    # BACK OF CARD
                    html.Div([
                        html.H1("Jalen Washington"),
                        html.H3("F| Jr. | 6\'10\""),
                        html.H3("Gary, Ind."),
                        html.H3("West Side")
                    ]
                             , className="flip-card-back"),
                ],
                className="flip-card-inner"
            ),
        ], className="flip-card",
),
#CONTAINER FOR CARD 7
        html.Div([
            #FRONT-BACK OF CARD FUNCTINOALITY
            html.Div(
                [
                    # FRONT OF CARD FUNCTIONALITY
                    html.Div(
                        [
                            #HEADSHOT FOR PLAYER7
                            html.Img(
                                src="https://images.sidearmdev.com/crop?url=https%3A%2F%2Fdxbhsrqyrr690.cloudfront.net%2Fsidearm.nextgen.sites%2Func.sidearmsports.com%2Fimages%2F2024%2F10%2F2%2FLubin_Ven.mb.15_EKqGT.JPG&width=180&height=270&type=webp",
                                style={"width": "220px", "height": "250px"},
                            )
                        ],
                        className="flip-card-front",
                    ),
                    # BACK OF CARD
                    html.Div([
                        html.H1("Ven-Allen Lubin"),
                        html.H3("F | Jr. | 6\'8\""),
                        html.H3("Orlando, Fl"),
                        html.H3("Orlando Christian")
                              ], className="flip-card-back"),
                ],
                className="flip-card-inner"
            ),
        ], className="flip-card",
),
#CONTAINER FOR CARD 8
        html.Div([
            #FRONT-BACK OF CARD FUNCTINOALITY
            html.Div(
                [
                    # FRONT OF CARD FUNCTIONALITY
                    html.Div(
                        [
                            #HEADSHOT FOR PLAYER8
                            html.Img(
                                src="https://images.sidearmdev.com/crop?url=https%3A%2F%2Fdxbhsrqyrr690.cloudfront.net%2Fsidearm.nextgen.sites%2Func.sidearmsports.com%2Fimages%2F2024%2F10%2F2%2FWithers_Jae_Lyn.mb.23_W4uWp.JPG&width=180&height=270&type=webp",
                                style={"width": "220px", "height": "250px"},
                            )
                        ],
                        className="flip-card-front",
                    ),
                    # BACK OF CARD
                    html.Div([
                        html.H1("Jae\'lyn Withers"),
                        html.H3("F | Gr. | 6\'9\""),
                        html.H3("Charlotte, N.C."),
                        html.H3("North Mecklenburg (Huntersville, N.C.)")
                              ], className="flip-card-back"),
                ],
                className="flip-card-inner"
            ),
        ], className="flip-card",
),
#CONTAINER FOR CARD 9
        html.Div([
            #FRONT-BACK OF CARD FUNCTINOALITY
            html.Div(
                [
                    # FRONT OF CARD FUNCTIONALITY
                    html.Div(
                        [
                            #HEADSHOT FOR PLAYER8
                            html.Img(
                                src="https://images.sidearmdev.com/crop?url=https%3A%2F%2Fdxbhsrqyrr690.cloudfront.net%2Fsidearm.nextgen.sites%2Func.sidearmsports.com%2Fimages%2F2024%2F10%2F2%2FClaude_Ty.mb.22_Z8zz9.JPG&width=180&height=270&type=webp",
                                style={"width": "220px", "height": "250px"},
                            )
                        ],
                        className="flip-card-front",
                    ),
                    # BACK OF CARD
                    html.Div([
                        html.H1("Ty Claude"),
                        html.H3("F | Gr. | 6\'7\""),
                        html.H3("Goldsboro, N.C."),
                        html.H3("Moravian Prep (Hudson, N.C.)")
                              ], className="flip-card-back"),
                ],
                className="flip-card-inner"
            ),
        ], className="flip-card",
),
#CONTAINER FOR CARD 10
        html.Div([
            #FRONT-BACK OF CARD FUNCTINOALITY
            html.Div(
                [
                    # FRONT OF CARD FUNCTIONALITY
                    html.Div(
                        [
                            #HEADSHOT FOR PLAYER8
                            html.Img(
                                src="https://images.sidearmdev.com/crop?url=https%3A%2F%2Fdxbhsrqyrr690.cloudfront.net%2Fsidearm.nextgen.sites%2Func.sidearmsports.com%2Fimages%2F2024%2F10%2F2%2FBrown_James.mb.26_1HjeG.JPG&width=180&height=270&type=webp",
                                style={"width": "220px", "height": "250px"},
                            )
                        ],
                        className="flip-card-front",
                    ),
                    # BACK OF CARD
                    html.Div([
                        html.H1("James Brown"),
                        html.H3("F | Fr. | 6\'10\" "),
                        html.H3("Aurora, Il."),
                        html.H3("Link Academy (Branson, Mo.")
                              ], className="flip-card-back"),
                ],
                className="flip-card-inner"
            ),
        ], className="flip-card",
),
#CONTAINER FOR CARD 11
        html.Div([
            #FRONT-BACK OF CARD FUNCTINOALITY
            html.Div(
                [
                    # FRONT OF CARD FUNCTIONALITY
                    html.Div(
                        [
                            #HEADSHOT FOR PLAYER8
                            html.Img(
                                src="https://images.sidearmdev.com/crop?url=https%3A%2F%2Fdxbhsrqyrr690.cloudfront.net%2Fsidearm.nextgen.sites%2Func.sidearmsports.com%2Fimages%2F2024%2F10%2F2%2FTyson_Cade.mb.17_nrdTr.JPG&width=180&height=270&type=webp",
                                style={"width": "220px", "height": "250px"},
                            )
                        ],
                        className="flip-card-front",
                    ),
                    # BACK OF CARD
                    html.Div([
                        html.H1("Cade Tyson"),
                        html.H3("G/F | Jr. | 6\'7\""),
                        html.H3("Monroe, N.C."),
                        html.H3("Carmel Christian (Matthews, N.C.")
                              ], className="flip-card-back"),
                ],
                className="flip-card-inner"
            ),
        ], className="flip-card",
),
#CONTAINER FOR CARD 12
        html.Div([
            #FRONT-BACK OF CARD FUNCTINOALITY
            html.Div(
                [
                    # FRONT OF CARD FUNCTIONALITY
                    html.Div(
                        [
                            #HEADSHOT FOR PLAYER8
                            html.Img(
                                src="https://images.sidearmdev.com/crop?url=https%3A%2F%2Fdxbhsrqyrr690.cloudfront.net%2Fsidearm.nextgen.sites%2Func.sidearmsports.com%2Fimages%2F2024%2F10%2F2%2FDavis_Elijah.mb.14_dAnSa.JPG&width=180&height=270&type=webp",
                                style={"width": "220px", "height": "250px"},
                            )
                        ],
                        className="flip-card-front",
                    ),
                    # BACK OF CARD
                    html.Div([
                        html.H1("Elijah Davis"),
                        html.H3("G/F | Sr. | 6\'3\""),
                        html.H3("Chapel Hill, N.C."),
                        html.H3("Jordan (Durham, N.C.)"),
                              ], className="flip-card-back"),
                ],
                className="flip-card-inner"
            ),
        ], className="flip-card",
),
#CONTAINER FOR CARD 13
        html.Div([
            #FRONT-BACK OF CARD FUNCTINOALITY
            html.Div(
                [
                    # FRONT OF CARD FUNCTIONALITY
                    html.Div(
                        [
                            #HEADSHOT FOR PLAYER8
                            html.Img(
                                src="https://images.sidearmdev.com/crop?url=https%3A%2F%2Fdxbhsrqyrr690.cloudfront.net%2Fsidearm.nextgen.sites%2Func.sidearmsports.com%2Fimages%2F2024%2F10%2F2%2FHawkins_Russ.mb.13_c1xif.JPG&width=180&height=270&type=webp",
                                style={"width": "220px", "height": "250px"},
                            )
                        ],
                        className="flip-card-front",
                    ),
                    # BACK OF CARD
                    html.Div([
                        html.H1("Russell Hawkins"),
                        html.H3("G | So. | 6\'1\""),
                        html.H3("Charlotte, N.C."),
                        html.H3("Mallard Creek")
                              ], className="flip-card-back"),
                ],
                className="flip-card-inner"
            ),
        ], className="flip-card",
),
#CONTAINER FOR CARD 14
        html.Div([
            #FRONT-BACK OF CARD FUNCTINOALITY
            html.Div(
                [
                    # FRONT OF CARD FUNCTIONALITY
                    html.Div(
                        [
                            #HEADSHOT FOR PLAYER8
                            html.Img(
                                src="https://images.sidearmdev.com/crop?url=https%3A%2F%2Fdxbhsrqyrr690.cloudfront.net%2Fsidearm.nextgen.sites%2Func.sidearmsports.com%2Fimages%2F2024%2F10%2F2%2FHolbrook_John.mb.12_tW0uX.JPG&width=180&height=270&type=webp",
                                style={"width": "220px", "height": "250px"},
                            )
                        ],
                        className="flip-card-front",
                    ),
                    # BACK OF CARD
                    html.Div([
                        html.H1("John Holbrook"),
                        html.H3("F | Fr. | 6\'8\""),
                        html.H3("Hickory, N.C."),
                        html.H3("Hickory")
                              ], className="flip-card-back"),
                ],
                className="flip-card-inner"
            ),
        ], className="flip-card",
),
#CONTAINER FOR CARD 14
        html.Div([
            #FRONT-BACK OF CARD FUNCTINOALITY
            html.Div(
                [
                    # FRONT OF CARD FUNCTIONALITY
                    html.Div(
                        [
                            #HEADSHOT FOR PLAYER8
                            html.Img(
                                src="https://images.sidearmdev.com/crop?url=https%3A%2F%2Fdxbhsrqyrr690.cloudfront.net%2Fsidearm.nextgen.sites%2Func.sidearmsports.com%2Fimages%2F2024%2F10%2F2%2FMayo_Dante.mb.27_wygLS.JPG&width=180&height=270&type=webp",
                                style={"width": "220px", "height": "250px"},
                            )
                        ],
                        className="flip-card-front",
                    ),
                    # BACK OF CARD
                    html.Div([
                        html.H1("Dante Mayo Jr."),
                        html.H3("G | Fr. | 6\'1\""),
                        html.H3("Gaithersburg, Md."),
                        html.H3("Richard Montgomery")
                              ], className="flip-card-back"),
                ],
                className="flip-card-inner"
            ),
        ], className="flip-card",
)

    ], className="card-container"),

    html.Div([html.Footer("\u00A9 IceeCodee")], className="footer"

    ),
)

if __name__ == '__main__':
    app.run(debug=True)
