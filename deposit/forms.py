from django import forms

class FraudPredictionForm(forms.Form):

    job = forms.ChoiceField(choices=[('admin.', 'Admin'), ('blue-collar', 'Blue-collar'), ('entrepreneur', 'Biznesmen'), ('housemaid', 'Xonadon'), ('management', 'Menejerlik'), ('retired', 'Pensioner'), ('self-employed', 'Shaxsiy korxona egasi'), ('services', 'Xizmatkor'), ('student', 'Talaba'), ('technician', 'Texnik')], label='Ish')
    marital = forms.ChoiceField(choices=[('married', 'Uylangan'), ('single', 'Yolg\'iz')], label='Oilaviy holati')
    education = forms.ChoiceField(choices=[('primary', 'Boshlangich'), ('secondary', 'O\'rta ta''lim'), ('tertiary', 'Oliy ta\'lim')], label='Ta\'lim')
    default = forms.ChoiceField(choices=[('yes', 'Ha'), ('no', 'Yo\'q')], label='Qo\'shimcha moliyaviy masuliyat')
    housing = forms.ChoiceField(choices=[('yes', 'Ha'), ('no', 'Yo\'q')], label='Uy egasi')
    loan = forms.ChoiceField(choices=[('yes', 'Ha'), ('no', 'Yo\'q')], label='Kredit olish')
    contact = forms.ChoiceField(choices=[('cellular', 'Mobil'), ('telephone', 'Telefon')], label='Aloqa usuli')
    month = forms.ChoiceField(choices=[('jan', 'Yanvar'), ('feb', 'Fevral'), ('mar', 'Mart'), ('apr', 'Aprel'), ('may', 'May'), ('jun', 'Iyun'), ('jul', 'Iyul'), ('aug', 'Avgust'), ('sep', 'Sentabr'), ('oct', 'Oktabr')], label='Oyni tanlang')
    day_of_week = forms.ChoiceField(choices=[('mon', 'Dushanba'), ('tue', 'Seshanba'), ('wed', 'Chorshanba'), ('thu', 'Payshanba'), ('fri', 'Juma')], label='Hafta kuni')
    duration = forms.IntegerField(label='Aloqa davomiyligi')
    campaign = forms.IntegerField(label='Kampaniya')
    pdays = forms.IntegerField(label='Oxirgi aloqa kunlari')
    previous = forms.IntegerField(label='Oldingi kampaniya sanasi')
    poutcome = forms.ChoiceField(choices=[('nonexistent', 'Mavjud emas'), ('failure', 'Muvaffaqiyatsiz')], label='Oldingi kampaniya natijasi')
    amount = forms.IntegerField(label='Summa')
