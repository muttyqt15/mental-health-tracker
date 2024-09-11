from django.forms import ModelForm
from main.models import MoodEntry

# Create DTO
class MoodEntryForm(ModelForm):
    class Meta:
        model = MoodEntry
        fields = ["mood", "feelings", "mood_intensity"]