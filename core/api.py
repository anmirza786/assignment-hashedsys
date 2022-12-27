# from django.urls import path
# from core.views import *


# urlpatterns = [
#     path('requisition/',
#          RequisitionViewSet.as_view({'get': 'list', 'post': 'create'})),
#     path('requisition/<int:pk>/',
#          RequisitionViewSet.as_view({'get': 'retrieve', 'delete': 'destroy', 'put': 'update',  'patch': 'partial_update'})),
#     path('filters/', ParentClassLevelViewSet.as_view({'get': 'list'})),
#     path('resume/', ResumeHeaderViewSet.as_view({'get': 'list'})),
#     path('count/requisition/',
#          CountRequisitionView.as_view()),
#     path('discipline/', DisciplineView.as_view()),
#     path('occupation/', OccupationView.as_view()),
#     path('speciality/', SpecialityView.as_view()),
#     path('subspeciality/', SubSpecialityView.as_view()),
#     path('requisition/resume/',
#          RequisitionResumeView.as_view()),
#     path('filter/education/', EducationView.as_view()),
#     path('filter/experience/', ExperienceView.as_view()),
#     path('filter/tools/', ToolsView.as_view()),
#     path('filter/skills/', SkillsFilterView.as_view()),
#     path('filter/corporate/', CorporateFilterView.as_view()),
#     path('compare/requisition/<int:pk>',
#          CompareRequsistionViewSet.as_view({'post': 'create', 'delete': 'destroy'})),
#     path('shortlist/requisition/<int:pk>',
#          RequisitionShortListViewSet.as_view({'post': 'create', 'delete': 'destroy'})),
#     path('contract/requisition/<int:pk>',
#          RequisitionContractViewSet.as_view({'post': 'create', 'delete': 'destroy'})),
#     path('compare/requisition/',
#          CompareRequsistionViewSet.as_view({'get': 'list'})),
#     path('shortlist/requisition/',
#          RequisitionShortListViewSet.as_view({'get': 'list'})),
#     path('contract/requisition/',
#          RequisitionContractViewSet.as_view({'get': 'list'})),






# ]
