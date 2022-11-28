from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder.charts.views import DirectByChartView

from . import appbuilder, db
from .models import Cislo


class CisloView(ModelView):
    datamodel = SQLAInterface(Cislo)

    list_columns = ["id","cislo"]
    """show_template = "appbuilder/general/model/show_cascade.html"""
class CountryDirectChartView(DirectByChartView):
    datamodel = SQLAInterface(Cislo)
    definitions = [
    {
        'label': 'cislo',
        'group': 'id',
        'series': ['cislo']
    }
]

db.create_all()

appbuilder.add_view(
    CisloView, "Cislo", icon="fa-folder-open-o"
)
appbuilder.add_view(CountryDirectChartView, "Show Country Chart", icon="fa-dashboard", category="Statistics")

