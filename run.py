from app import create_app, db
app=create_app()
if __name__=="__main__":
    with app.app_context():
        db.create_all()
        # from app.models import User, Post
        # user_1 =User(username='tysjtyjstyjtyjs', email='tysjytjtyj@demo.com', password='pass')
        # db.session.add(user_1)
        # db.session.commit()
        # User.query.all()
    app.run(debug=True)