from django.db import models

# Create your models here.

class year_publications(models.Model):
    year = models.IntegerField()
    publication_number = models.IntegerField()

    def __str__(self):
        return f'year : {self.year}, Publications: {self.publication_number}'

    class Meta:
        verbose_name_plural = "Year Publications"


class Publication(models.Model):

    types = (
              ("Conference Paper", "Conference Paper"),
              ("Article", "Article"),
              ("Book Chapter", "Book Chapter"),
              ("Book","Book"),
              ("Editorial", "Editorial"),
              ("Review", "Review"),
              ("Letter", "Letter"),
            )

    authors = models.CharField(max_length= 500)
    title = models.CharField(max_length=1500)
    scopus_url = models.URLField(max_length=500, blank=True, null=True)
    DOI = models.CharField(max_length=100, blank=True, null=True)
    affiliation = models.TextField(blank=True, null=True)
    publisher = models.CharField(max_length=200, blank=True, null=True)
    ISSN = models.CharField(max_length=30, blank=True, null=True)
    ISBN = models.CharField(max_length=30, blank=True, null=True)
    document_type = models.CharField(max_length=50, choices=types)
    publication_stage = models.CharField(max_length=50, blank=True, null=True)
    open_access = models.CharField(max_length=50, blank=True, null=True)
    publishing_year = models.IntegerField()
    source = models.CharField(max_length=50, blank=True, null=True)
    cited_by = models.IntegerField(blank=True, null=True)




