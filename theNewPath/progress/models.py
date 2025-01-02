# from django.db import models
# import uuid
# from user.models import User
# from courses.models import Lesson, UserCourse

# class LessonScore(models.Model):
#     scoreId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="lesson_scores")
#     lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="lesson_scores_in_progress")
#     score = models.DecimalField(max_digits=5, decimal_places=2)
#     createdAt = models.DateTimeField(auto_now_add=True)

# class Progress(models.Model):
#     progress_id = models.UUIDField(primary_key=True, default=models.UUIDField, editable=False)
#     user_course = models.ForeignKey(UserCourse, on_delete=models.CASCADE, related_name="progress")
#     current_lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, blank=True, null=True)
#     completion_percentage = models.DecimalField(max_digits=5, decimal_places=2)
#     started_at = models.DateTimeField()
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"{self.user_course.user.email} - {self.completion_percentage}%"
