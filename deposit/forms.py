from django import forms

class FraudPredictionForm(forms.Form):

    job = forms.ChoiceField(choices=[('admin.', 'Admin'), ('blue-collar', 'Blue-collar'), ('entrepreneur', 'Biznesmen'), ('housemaid', 'Xonadon'), ('management', 'Menejerlik'), ('retired', 'Pensioner'), ('self-employed', 'Shaxsiy korxona egasi'), ('services', 'Xizmatkor'), ('student', 'Talaba'), ('technician', 'Texnik')], label='Ish')
    marital = forms.ChoiceField(choices=[('married', 'Uylangan'), ('single', 'Yolg\'iz')], label='Oilaviy holati')
    education = forms.ChoiceField(choices=[('primary', 'Boshlangich'), ('secondary', 'O\'rta ta''lim'), ('tertiary', 'Oliy ta\'lim')], label='Ta\'lim')
    default = forms.ChoiceField(choices=[('yes', 'Ha'), ('no', 'Yo\'q')], label='Qarz')
    housing = forms.ChoiceField(choices=[('yes', 'Ha'), ('no', 'Yo\'q')], label='Uy egasi')
    loan = forms.ChoiceField(choices=[('yes', 'Ha'), ('no', 'Yo\'q')], label='Kredit holati')
    contact = forms.ChoiceField(choices=[('cellular', 'Mobil'), ('telephone', 'Telefon')], label='Aloqa usuli')
    month = forms.ChoiceField(choices=[('jan', 'Yanvar'), ('feb', 'Fevral'), ('mar', 'Mart'), ('apr', 'Aprel'), ('may', 'May'), ('jun', 'Iyun'), ('jul', 'Iyul'), ('aug', 'Avgust'), ('sep', 'Sentabr'), ('oct', 'Oktabr')], label='Oyni tanlang')
    day_of_week = forms.ChoiceField(choices=[('mon', 'Dushanba'), ('tue', 'Seshanba'), ('wed', 'Chorshanba'), ('thu', 'Payshanba'), ('fri', 'Juma')], label='Hafta kuni')
    duration = forms.IntegerField(label='So\'nggi aloqa davomiyligi')
    campaign = forms.IntegerField(label='Murojatlar soni')
    pdays = forms.IntegerField(label='Oxirgi aloqadan keyin o\'tgan kunlar')
    previous = forms.IntegerField(label='Aloqaga chiqilganlar soni')
    poutcome = forms.ChoiceField(choices=[('nonexistent', 'Mavjud emas'), ('failure', 'Muvaffaqiyatsiz')], label='Oldingi murojat  natijasi')
    amount = forms.IntegerField(label='Qiymat')
