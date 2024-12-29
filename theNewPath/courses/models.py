from django.db import models
import uuid
from user.models import User

class CourseCategory(models.Model):
    category_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

class Courses(models.Model):
    course_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE, related_name="category")
    duration = models.IntegerField()
    start_date = models.DateField()
    deadline = models.DateField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Lesson(models.Model):
    lesson_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name="lessons")
    title = models.CharField(max_length=255, unique=True)
    content = models.TextField()
    lesson_type = models.CharField(
        max_length=10, choices=[("audio", "Audio"), ("video", "Video"), ("text", "Text")]
    )
    day_number = models.PositiveIntegerField()
    max_score = models.DecimalField(max_digits=5, decimal_places=2)
    media_url = models.URLField(blank=True, null=True)
    is_optional = models.BooleanField(default=False)
    start_date = models.DateField()
    deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class UserCourse(models.Model):
    user_course_id = models.UUIDField(primary_key=True, default=models.UUIDField, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="enrolled_users")
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name="courses_enrolled")
    enrolled_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(blank=True, null=True)
    completionPercentage = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    overall_course_score = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.user.email} - {self.course.title}"
    
class LessonScore(models.Model):
    lesson_score_id = models.UUIDField(primary_key=True, default=models.UUIDField, editable=False)
    user_course = models.ForeignKey(UserCourse, on_delete=models.CASCADE, related_name="lesson_scores")
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="lesson_scores_in_courses")
    score = models.DecimalField(max_digits=5, decimal_places=2)
    completed_at = models.DateTimeField()

    def __str__(self):
        return f"{self.user_course.user.email} - {self.lesson.title}"

class Quiz(models.Model):
    quizId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="quizzes")
    question = models.TextField()
    options = models.JSONField()
    correctAnswer = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Quiz for {self.lesson.title}"
