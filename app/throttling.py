from rest_framework.throttling import UserRateThrottle

class StudentRateThrottle(UserRateThrottle):
    # scope = '3/minutes'
    scope = 'student_throttle'