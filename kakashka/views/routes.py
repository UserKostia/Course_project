from kakashka.views.Router import Router, DataStrategyEnum
from kakashka.views.index_view import index_view
from kakashka.views.patients_view import patiens_view
from kakashka.views.settings_view import SettingsView
from kakashka.views.doc_records import doc_records_view

router = Router(DataStrategyEnum.QUERY)

router.routes = {
  "/": index_view,
  "/doc_rec": doc_records_view,
  "/patient": patiens_view,
  "/settings": SettingsView,
}
