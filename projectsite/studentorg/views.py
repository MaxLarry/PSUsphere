from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from studentorg.models import Organization, Student, OrgMember, College, Program
from studentorg.forms import OrganizationForm, StudentForm, OrgMemberForm, CollegeForm, ProgramForm
from django.urls import reverse_lazy

from typing import Any
from django.db.models.query import QuerySet
from django.db.models import Q

class HomePageView(ListView):
    model = Organization
    contextobject_name = 'home'
    template_name = "home.html"

class OrganizationList(ListView):
    model = Organization
    context_object_name = 'organization'
    template_name = 'organization/org_list.html'
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):
        qs = super (OrganizationList, self).get_queryset(*args, **kwargs)
        if self.request.GET.get("q") != None:
            query = self.request.GET.get('q')
            qs = qs.filter(Q(name__icontains=query) |
                        Q (description___icontains=query))
        return qs

class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'organization/org_add.html'
    success_url = reverse_lazy('organization-list')

class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'organization/org_edit.html'
    success_url = reverse_lazy('organization-list')

class OrganizationDeleteView(DeleteView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'organization/org_del.html'
    success_url = reverse_lazy('organization-list')


#student ---------------------------------------------------------------

class StudentList(ListView):
    model = Student
    context_object_name = 'student'
    template_name = 'student/stud_list.html'
    paginate_by = 10

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student/stud_add.html'
    success_url = reverse_lazy('student-list')

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'student/stud_edit.html'
    success_url = reverse_lazy('student-list')

class StudentDeleteView(DeleteView):
    model = Student
    form_class = StudentForm
    template_name = 'student/stud_del.html'
    success_url = reverse_lazy('student-list')



#Organization Members ---------------------------------------------------------------

class OrgMemberList(ListView):
    model = OrgMember
    context_object_name = 'orgmember'
    template_name = 'org_member/orgmem_list.html'
    paginate_by = 10

class OrgMemberCreateView(CreateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = 'org_member/orgmem_add.html'
    success_url = reverse_lazy('orgmem-list')

class OrgMemberUpdateView(UpdateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = 'org_member/orgmem_edit.html'
    success_url = reverse_lazy('orgmem-list')

class OrgMemberDeleteView(DeleteView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = 'org_member/orgmem_del.html'
    success_url = reverse_lazy('orgmem-list')



#College ---------------------------------------------------------------

class CollegeList(ListView):
    model = College
    context_object_name = 'college'
    template_name = 'college/college_list.html'
    paginate_by = 10

class CollegeCreateView(CreateView):
    model = College
    form_class = CollegeForm
    template_name = 'college/college_add.html'
    success_url = reverse_lazy('college-list')

class CollegeUpdateView(UpdateView):
    model = College
    form_class = CollegeForm
    template_name = 'college/college_edit.html'
    success_url = reverse_lazy('college-list')

class CollegeDeleteView(DeleteView):
    model = College
    form_class = CollegeForm
    template_name = 'college/college_del.html'
    success_url = reverse_lazy('college-list')


#Program ---------------------------------------------------------------

class ProgramList(ListView):
    model = Program
    context_object_name = 'program'
    template_name = 'program/program_list.html'
    paginate_by = 10

class ProgramCreateView(CreateView):
    model = Program
    form_class = ProgramForm
    template_name = 'program/program_add.html'
    success_url = reverse_lazy('program-list')

class ProgramUpdateView(UpdateView):
    model = Program
    form_class = ProgramForm
    template_name = 'program/program_edit.html'
    success_url = reverse_lazy('program-list')

class ProgramDeleteView(DeleteView):
    model = Program
    form_class = ProgramForm
    template_name = 'program/program_del.html'
    success_url = reverse_lazy('program-list')