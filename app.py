from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///images.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Images(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    file_path =         db.Column(db.String(50), nullable=False)
    scientific_name =   db.Column(db.String(50), nullable=True)
    common_name =       db.Column(db.String(20), nullable=True)
    price =             db.Column(db.Float, nullable=True)
    light =             db.Column(db.String(4), nullable=True)
    size =              db.Column(db.String(6), nullable=True)
    toxic =             db.Column(db.String(3), nullable=True)

    def __repr__(self):
        return '<%r>' % self.scientific_name


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        light = request.form['light']
        size = request.form['size']
        toxic = request.form['toxic']

        results = get_custom_plant(size, light, toxic)

        return render_template('results.html', results=results)

    else:
        all_plants = Images.query.all()
        return render_template('index.html', plants=all_plants)

@app.route('/search', methods=['POST', 'GET'])
def search():
    if request.method == 'POST':
        entry = request.form['search']
        entry = entry.strip()
        entry = '%{}%'.format(entry)
        print(entry)
        results = Images.query.filter(Images.scientific_name.like(entry)).all()
        print(results)

        return render_template('results.html', results=results)
    else:
        return 'GET for search'



def get_custom_plant(size, light, toxic):
    size_plants = None
    light_plants = None
    toxic_plants = None

    if size == 'any':
        size_plants = Images.query.all()
    else:
        size_plants = Images.query.filter(Images.size.like(size)).all()

    if light == 'varied':
        light_plants = Images.query.all()
    else:
        light_plants =  Images.query.filter(Images.light.like(light)).all()

    if toxic == 'yes':
        toxic_plants =  Images.query.all()
    else:
        toxic_plants = Images.query.filter(Images.toxic.like(toxic)).all()

    results = list(set.intersection(*map(set, [light_plants, size_plants, toxic_plants])))
    
    return results
        

def init_db():
    imgs = [
        Images(
            file_path='/static/images/AquilegiaFormosa.jpg', 
            scientific_name='Aquilegia formosa', 
            common_name='Western Columbine',
            price=14.00,
            light='high',
            size='small',
            toxic='no'),
        
        Images(
            file_path='/static/images/ARABIS_Hirsuta.jpg', 
            scientific_name='Arabis hirsuta', 
            common_name='White-flowered Rockcress',
            price=92.00,
            light='high',
            size='small',
            toxic='yes'),   

        Images(
            file_path='/static/images/Arnica_chamissonis_03.JPG', 
            scientific_name='Arnica chamissonis', 
            common_name='Meadow Arnica',
            price=20.00,
            light='high',
            size='medium',
            toxic='no'),   

        Images(
            file_path='/static/images/Aruncus_dioicus_1549.JPG', 
            scientific_name='Aruncus dioicus', 
            common_name='Bride’s Feathers',
            price=18.00,
            light='high',
            size='medium',
            toxic='yes'),  
            
        Images(
            file_path='/static/images/Showy_Aster_Plant.gif', 
            scientific_name='Aster conspicuus', 
            common_name='Showy Aster',
            price=32.00,
            light='high',
            size='large',
            toxic='no'),    

        Images(
            file_path='/static/images/Balsamorhiza_sagittata_9337.JPG', 
            scientific_name='Balsamorhiza sagittata', 
            common_name='Arrowleaf Balsamroot',
            price=15.00,
            light='high',
            size='large',
            toxic='yes'), 

        Images(
            file_path='/static/images/Boykinia_occidentalis_9501.JPG', 
            scientific_name='Boykinia occidentalis', 
            common_name='Coastal Brookfoam',
            price=30.00,
            light='low',
            size='small',
            toxic='no'), 

        Images(
            file_path='/static/images/Clintonia_uniflora_9062.JPG', 
            scientific_name='Clintonia uniflora', 
            common_name='Queen’s Cup',
            price=28.00,
            light='low',
            size='small',
            toxic='yes'),

        Images(
            file_path='/static/images/Dodecatheon_pulchellum_5423.JPG', 
            scientific_name='Dodecatheon pulchellum', 
            common_name='Pretty Shooting Star',
            price=28.00,
            light='low',
            size='medium',
            toxic='no'),

        Images(
            file_path='/static/images/Dodecatheon_hendersonii.jpg', 
            scientific_name='Dodecatheon hendersonii', 
            common_name='Shooting Star',
            price=28.00,
            light='low',
            size='medium',
            toxic='yes'),

        Images(
            file_path='/static/images/Erigeron_speciosus_01.jpg', 
            scientific_name='Erigeron speciosus', 
            common_name='Showy Daisy',
            price=28.00,
            light='low',
            size='large',
            toxic='no'),

        Images(
            file_path='/static/images/Eriogonum_umbellatum_17009.JPG', 
            scientific_name='Eriogonum umbellatum', 
            common_name='Sulphur Buckwheat',
            price=28.00,
            light='low',
            size='large',
            toxic='yes'),

        Images(
            file_path='/static/images/Eriophyllum_lanatum_kz02.jpg', 
            scientific_name='Eriophyllum lanatum', 
            common_name='Oregon Sunshine',
            price=28.00,
            light='none',
            size='small',
            toxic='no'),
        
        Images(
            file_path='/static/images/parnassia-fimbriata1.jpg', 
            scientific_name='Parnassia fimbriata', 
            common_name='Grass-of-Parnassus',
            price=28.00,
            light='none',
            size='small',
            toxic='yes'),
        
        Images(
            file_path='/static/images/Penstemon_davidsonii_6271.JPG', 
            scientific_name='Penstemon davidsonii', 
            common_name='Davidson’s Penstemon',
            price=28.00,
            light='none',
            size='medium',
            toxic='no'),

        Images(
            file_path='/static/images/Potentilla_gracilis_2.jpg', 
            scientific_name='Potentilla gracilis', 
            common_name='Graceful Cinquefoil',
            price=28.00,
            light='none',
            size='medium',
            toxic='yes'),

        Images(
            file_path='/static/images/prunella-vulgaris-1296x728-feature.jpg', 
            scientific_name='Prunella vulgaris', 
            common_name='Heal-All',
            price=28.00,
            light='none',
            size='large',
            toxic='no'),

        Images(
            file_path='/static/images/Sanguisorba-menziesii.jpg', 
            scientific_name='Sanguisorba menziesii', 
            common_name='Menzies’ Burnet',
            price=28.00,
            light='none',
            size='large',
            toxic='yes'),
  
    ]

    for i in imgs:
        try:
            db.session.add(i)
            db.session.commit()
            print('added ' + i.file_path) 
        except:
            print('\n\nissue adding ' + i.scientific_name)


if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    init_db()
    app.run(debug=True)