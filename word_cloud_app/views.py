from django.shortcuts import render
from wordcloud import WordCloud
import docx
from datetime import datetime
from collections import Counter
from django.conf import settings

# image configurations
background_color = "#101010"
height = 720
width = 1080

# If you import NLTK stop words using from nltk.corpus import stopwords and try printing the words
# using stopwords.words('english')

# created set from list as searching set is fast
# added single space as stop word
stopwords = {'', ' ', 'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd",
             'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers',
             'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which',
             'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been',
             'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but',
             'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against',
             'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down',
             'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when',
             'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no',
             'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don',
             "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't",
             'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven',
             "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan',
             "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn',
             "wouldn't"}


# Create your views here.
def home(request):

    # template data
    data = {}

    if "POST" == request.method:
        if 'text_file' not in request.FILES:
            data['error_message'] = 'File not uploaded'

        uploaded_file = request.FILES['text_file']

        file_data = ""

        if uploaded_file.name.endswith('docx') or uploaded_file.name.endswith('doc'):
            doc = docx.Document(uploaded_file)
            full_text = []
            for para in doc.paragraphs:
                full_text.append(para.text)
            file_data = '\n'.join(full_text)
        else:
            file_data = uploaded_file.read().decode("utf-8")

        file_data = file_data.replace("\n", " ")
        file_data = file_data.replace(",", "")
        file_data = file_data.replace(".", "")

        if not file_data:
            data['error_message'] = 'No significant data in file'
            return render(request, 'word_cloud_app/home.html', data)

        words = file_data.split(" ")

        new_words = [w for w in words if w not in stopwords]

        counter = Counter(new_words)
        frequencies = dict(counter)

        # print(counter.most_common(10))
        data['common_words'] = counter.most_common(10)

        word_cloud = WordCloud(
            background_color=background_color,
            width=width,
            height=height
        )

        word_cloud.generate_from_frequencies(frequencies)

        # generate filename
        imagename = datetime.now().strftime("%Y%m%d%H%M%S%f") + ".png"
        filename = settings.MEDIA_ROOT + imagename
        print(filename)
        word_cloud.to_file(filename)

        data["media_url"] = '/media/'
        data["imagename"] = imagename

    return render(request, 'word_cloud_app/home.html', data)
