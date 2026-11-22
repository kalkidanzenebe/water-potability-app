st.markdown("""
<style>

/* =========================
   GLOBAL
========================= */
.stApp{
    background: linear-gradient(135deg,#0A0F1E,#111827,#0F172A);
    color:white;
}

[data-testid="stHeader"]{
    background: transparent;
}

.main .block-container{
    max-width:1300px;
    padding-top:1rem;
    padding-bottom:1rem;
}

/* =========================
   HERO
========================= */

.hero{
    background:
    linear-gradient(
    135deg,
    rgba(0,212,255,0.15),
    rgba(255,215,0,0.08)
    );

    border:1px solid rgba(255,255,255,0.08);

    backdrop-filter: blur(20px);

    border-radius:25px;

    padding:40px;

    text-align:center;

    margin-bottom:25px;

    box-shadow:
    0 15px 40px rgba(0,0,0,0.3);
}

.hero h1{
    font-size:3rem;
    font-weight:900;
    margin-bottom:10px;

    background:
    linear-gradient(
    90deg,
    #38BDF8,
    #67E8F9,
    #FACC15
    );

    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

.hero p{
    color:#CBD5E1;
    font-size:1.1rem;
}

/* =========================
   CARDS
========================= */

.info-card{
    background:rgba(255,255,255,0.05);

    border:1px solid rgba(255,255,255,0.08);

    backdrop-filter: blur(15px);

    border-radius:20px;

    padding:20px;

    text-align:center;

    transition:.3s;
}

.info-card:hover{
    transform:translateY(-5px);
}

.info-card h2{
    color:#38BDF8;
    margin:0;
}

.info-card p{
    color:#CBD5E1;
    margin-top:10px;
}

/* =========================
   FORM
========================= */

[data-testid="stForm"]{

    background:
    rgba(255,255,255,0.05);

    border:
    1px solid rgba(255,255,255,0.08);

    border-radius:25px;

    padding:25px;

    backdrop-filter: blur(18px);

    box-shadow:
    0 10px 35px rgba(0,0,0,0.25);
}

label{
    color:#67E8F9 !important;
    font-weight:600 !important;
}

/* =========================
   INPUTS
========================= */

[data-testid="stNumberInput"] input{

    background:#111827 !important;

    color:white !important;

    border:1px solid #38BDF8 !important;

    border-radius:12px !important;
}

[data-testid="stNumberInput"] input:focus{

    border:1px solid #FACC15 !important;

    box-shadow:
    0 0 12px rgba(250,204,21,0.4);
}

/* =========================
   BUTTON
========================= */

div[data-testid="stFormSubmitButton"] button{

    width:100%;

    height:55px;

    border:none;

    border-radius:14px;

    color:white;

    font-size:18px;

    font-weight:700;

    background:
    linear-gradient(
    90deg,
    #0EA5E9,
    #06B6D4
    );

    transition:.3s;
}

div[data-testid="stFormSubmitButton"] button:hover{

    transform:translateY(-3px);

    box-shadow:
    0 12px 25px rgba(14,165,233,0.4);
}

/* =========================
   RESULT CARD
========================= */

.result-card{

    background:
    rgba(255,255,255,0.05);

    border:
    1px solid rgba(255,255,255,0.08);

    border-radius:25px;

    backdrop-filter: blur(20px);

    padding:35px;

    text-align:center;

    animation:fadeIn .8s ease;
}

.result-card h2{
    font-size:42px;
    font-weight:800;
}

.result-card p{
    font-size:17px;
    color:#E2E8F0;
}

@keyframes fadeIn{
    from{
        opacity:0;
        transform:translateY(20px);
    }
    to{
        opacity:1;
        transform:translateY(0);
    }
}

.footer{
    text-align:center;
    color:#94A3B8;
    padding:20px;
}

hr{
    border:none;
    border-top:1px solid rgba(255,255,255,0.1);
}

</style>
""", unsafe_allow_html=True)
