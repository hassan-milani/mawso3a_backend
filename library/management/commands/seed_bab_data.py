import uuid
from django.core.management.base import BaseCommand
from library.models import Bab

class Command(BaseCommand):
    help = 'Seed database with predefined Bab data'

    def handle(self, *args, **kwargs):
        names = [
            "الباب الأول: سير الأنبياء والمرسلين وأممهم وعصورهم وبلدانهم", "الباب الثاني: سيرة أهل البيت وأعوانهم وخصومهم", "الباب الثالث: سيرة واقعة كربلاء وما يرتبط بها", "الباب الرابع: الإمام المهدي عجل الله تعالى فرجه", 
            "الباب الخامس: سير علماء الشيعة وأحوالهم وأعوانهم وخصومهم وأسرهم العلمية", "الباب السادس: سير شعراء الشيعة وأحوالهم", "الباب السابع: خطباء الشيعة وقراؤهم ومنشدوهم ومؤذنوهم وأصحاب المواكب", "الباب الثامن: دول وملوك الشيعة ووزراؤهم ورجالاتهم وخصومهم", 
            "الباب التاسع: ديموغرافيا الشيعة وبلدانهم وتاريخها", "الباب العاشر: آثار الشيعة العمرانية ومشاهدهم ومساجدهم وحسينياتهم", "الباب الحادي عشر: طقوس الشيعة وممارساتهم الدينية وعاداتهم وتقاليدهم", "الباب الثاني عشر: ملاحم الشيعة ومعاركهم واضطهادهم وسير جملة من شهدائهم",
            "الباب الثالث عشر: علوم الشيعة ومعارفهم وفنونهم", "الباب الرابع عشر: اعتقادات الشيعة في الأصول والفروع والأخلاق" 
        ]
        
        for name in names:
            # Use get_or_create to avoid duplication
            Bab.objects.get_or_create(id=uuid.uuid4(), name=name)

        self.stdout.write(self.style.SUCCESS('Successfully seeded Bab data!'))