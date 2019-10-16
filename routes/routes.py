from flask import Blueprint

router = Blueprint("router", __name__)

@router.route("/check")
def check():
    return "Congratulations! Your app works. :)"
@router.route("/hello")
def hello():
    return "(hello IEEE)";
@router.route("/add", methods=["POST"])
def add():
   
    return :
    
